from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
from pymongo import MongoClient
import os
import json
from openai import OpenAI
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# MongoDB connection settings
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "inspection"

# Initialize OpenAI client with OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# MongoDB client instance
mongo_client = None

@app.on_event("startup")
async def startup_db_client():
    """
    Initialize database connection on startup
    """
    global mongo_client
    try:
        mongo_client = MongoClient(MONGO_URI)
        # Verify the connection
        mongo_client.admin.command('ping')
        print("Successfully connected to MongoDB!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        raise

@app.on_event("shutdown")
async def shutdown_db_client():
    """
    Close database connection on shutdown
    """
    global mongo_client
    if mongo_client:
        mongo_client.close()
        print("MongoDB connection closed.")

def get_db():
    """
    Get database instance
    """
    if not mongo_client:
        raise HTTPException(status_code=500, detail="Database connection not initialized")
    return mongo_client[DB_NAME]

@app.get("/equipment", response_model=Dict[str, List[Dict[str, Any]]])
async def get_equipment():
    """
    Returns a list of all equipment items from the database.
    """
    try:
        db = get_db()
        equipment_list = list(db.equipment.find({}, {'_id': 0}))
        return {"equipment": equipment_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching equipment data: {str(e)}")

@app.get("/fluids", response_model=Dict[str, List[Dict[str, Any]]])
async def get_fluids():
    """
    Returns a list of all fluids from the database.
    """
    try:
        db = get_db()
        fluids_list = list(db.fluids.find({}, {'_id': 0}))
        return {"fluids": fluids_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching fluids data: {str(e)}")

async def analyze_deterioration_relevance(equipment: Dict, fluid: Dict, mechanisms: List[Dict]) -> Dict[str, List[str]]:
    """
    Use OpenRouter API to analyze which deterioration mechanisms are relevant for given equipment and fluid.
    """
    # Format all mechanisms into a single string
    mechanisms_str = "\n\n".join([
        f"id: {m.get('id', 'N/A')}\n"
        f"Mechanism {i+1}:\n"
        f"- Name: {m.get('name', 'N/A')}\n"
        f"- Description: {m.get('description', 'N/A')}\n"
        f"- Affected Areas: {', '.join(m.get('affectedAreas', []))}\n"
        f"- Contributing Factors: {', '.join(m.get('contributingFactors', []))}"
        for i, m in enumerate(mechanisms)
    ])
    print("mechanisms_str", mechanisms_str)
    print("equipment", equipment)
    print("fluid", fluid)
    prompt = f"""
    Analyze which of the following deterioration mechanisms are relevant for the given equipment and fluid.
    Each line of the response should have true or false and nothing else corresponding to whether a mechanism is relevant.

    Equipment:
    - Type: {equipment.get('type', 'N/A')}
    - Material: {equipment.get('material', 'N/A')}
    - Operating Temperature: {equipment.get('operatingTemperature', 'N/A')}°C
    - Operating Pressure: {equipment.get('operatingPressure', 'N/A')} bar
    - Design Temperature: {equipment.get('designTemperature', 'N/A')}°C
    - Design Pressure: {equipment.get('designPressure', 'N/A')} bar

    Fluid:
    - Name: {fluid.get('name', 'N/A')}
    - Type: {fluid.get('type', 'N/A')}
    - pH: {fluid.get('pH', 'N/A')}
    - Temperature: {fluid.get('temperature', 'N/A')}°C
    - Pressure: {fluid.get('pressure', 'N/A')} bar

    Deterioration Mechanisms:
    {mechanisms_str}
    """
    print("asking LLM")

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct:free",
            messages=[
                {
                    "role": "system",
                    "content": """You are an expert in materials science and corrosion engineering. 
                    Analyze which deterioration mechanisms are relevant for the given equipment and fluid combination. 
                    Consider all factors including material compatibility, operating conditions, and environmental factors.
                    Each line true or false for each mechanism and nothing else.
                    only return the list and nothing else"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.1,
            response_format={ "type": "json_object" }
        )
        # print(response)
        x = response.choices[0].message.content
        # [response.choices[0].message.content.find('{'):response.choices[0].message.content.rfind('}')+1]
        # remove all character's imbetween each } and {
        # Parse the response
        print(x)
        relevant_ids = []
        # Filter and return only relevant mechanisms
        for i, line in enumerate(x.split("\n")):
            
            if i < len(mechanisms) and "true" in line.strip():
                relevant_ids.append(mechanisms[i]["id"])
        print(relevant_ids)
        return {"relevant_ids": relevant_ids}
        
    except Exception as e:
        print(f"Error in LLM analysis: {str(e)}")
        return {"relevant_ids": []}

@app.get("/deterioration", response_model=Dict[str, List[Dict[str, Any]]])
async def get_deterioration(equipment_id: str = None, fluid_id: str = None):
    """
    Returns a list of relevant deterioration types based on equipment and fluid properties.
    Uses LLM to determine relevance.
    """
    try:
        db = get_db()
        deterioration_list = list(db.deterioration.find({}, {'_id': 0}))
        
        if not equipment_id and not fluid_id:
            return {"deterioration": deterioration_list}
        
        # Get equipment and fluid data if IDs are provided
        equipment = None
        fluid = None
        
        if equipment_id:
            equipment = db.equipment.find_one({"id": equipment_id}, {'_id': 0})
            if not equipment:
                raise HTTPException(status_code=404, detail=f"Equipment with ID {equipment_id} not found")
        
        if fluid_id:
            fluid = db.fluids.find_one({"id": fluid_id}, {'_id': 0})
            if not fluid:
                raise HTTPException(status_code=404, detail=f"Fluid with ID {fluid_id} not found")
        
        # Get relevant mechanisms in a single LLM call
        relevant_deterioration = await analyze_deterioration_relevance(equipment, fluid, deterioration_list)
        
        return {"deterioration": relevant_deterioration}
        
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error fetching deterioration data: {str(e)}")

async def analyze_failure_scenarios(deterioration_ids: List[str]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Use OpenRouter API to analyze which failure scenarios are relevant for given deterioration mechanisms.
    """
    try:
        db = get_db()
        # Get deterioration data for the provided IDs
        deteriorations = list(db.deterioration.find({"id": {"$in": deterioration_ids}}, {'_id': 0}))
        
        if not deteriorations:
            return {"failure_scenarios": []}
        
        # Get all failure scenarios from database
        failure_scenarios = list(db.failure_scenarios.find({}, {'_id': 0}))
        
        if not failure_scenarios:
            return {"failure_scenarios": []}
        
        # Format deteriorations into a single string
        deteriorations_str = "\n\n".join([
            f"Deterioration {i+1}:\n"
            f"- Name: {d.get('name', 'N/A')}\n"
            f"- Description: {d.get('description', 'N/A')}\n"
            f"- Affected Areas: {', '.join(d.get('affectedAreas', []))}\n"
            f"- Contributing Factors: {', '.join(d.get('contributingFactors', []))}"
            for i, d in enumerate(deteriorations)
        ])

        # Format failure scenarios for the prompt
        scenarios_str = "\n\n".join([
            f"Scenario {i+1}:\n"
            f"- Name: {s.get('name', 'N/A')}\n"
            f"- Description: {s.get('description', 'N/A')}\n"
            f"- Affected Components: {', '.join(s.get('affectedComponents', []))}\n"
            f"- Mitigation Strategies: {', '.join(s.get('mitigationStrategies', []))}"
            for i, s in enumerate(failure_scenarios)
        ])

        prompt = f"""
        Analyze which failure scenarios are relevant for the following deterioration mechanisms.
        Each line of the response should have true or false and nothing else corresponding to whether a failure scenario is relevant.

        Deterioration Mechanisms:
        {deteriorations_str}

        Possible Failure Scenarios:
        {scenarios_str}
        """

        response = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct:free",
            messages=[
                {
                    "role": "system",
                    "content": """You are an expert in materials science and failure analysis. 
                    Analyze which failure scenarios are relevant for the given deterioration mechanisms.
                    Consider the nature of the deterioration, affected areas, and contributing factors.
                    Each line true or false for each failure scenario and nothing else.
                    only return the list and nothing else"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.1
        )

        # Parse the response
        response_text = response.choices[0].message.content
        relevant_scenarios = []
        
        for i, line in enumerate(response_text.split("\n")):
            if i < len(failure_scenarios) and "true" in line.strip().lower():
                relevant_scenarios.append(failure_scenarios[i])

        return {"failure_scenarios": relevant_scenarios}

    except Exception as e:
        print(f"Error in LLM analysis: {str(e)}")
        return {"failure_scenarios": []}

@app.get("/failure_scenarios", response_model=Dict[str, List[Dict[str, Any]]])
async def get_failure_scenarios(deterioration_ids: str):
    """
    Returns a list of relevant failure scenarios based on deterioration mechanisms.
    Uses LLM to determine relevance.
    
    Args:
        deterioration_ids: Comma-separated list of deterioration IDs
    """
    try:
        # Convert comma-separated string to list
        id_list = [id.strip() for id in deterioration_ids.split(",")]
        
        # Get relevant failure scenarios
        result = await analyze_failure_scenarios(id_list)
        return result
        
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error analyzing failure scenarios: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
