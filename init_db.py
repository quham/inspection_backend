from pymongo import MongoClient
from initial_data import EQUIPMENT_DATA, FLUIDS_DATA, DETERIORATION_DATA
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection settings
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "inspection"
# Equipment data

# Failure scenarios data
FAILURE_SCENARIOS_DATA = [
    {
        "id": "catastrophic",
        "name": "Catastrophic Failure",
        "description": "Sudden, complete failure leading to immediate loss of containment",
        "severity": "High",
        "likelihood": "Low",
        "affectedComponents": ["Pressure Vessels", "Piping Systems", "Storage Tanks"],
        "mitigationStrategies": ["Regular Inspection", "Pressure Testing", "Material Selection"]
    },
    {
        "id": "gradual-leakage",
        "name": "Gradual Leakage",
        "description": "Slow, progressive loss of containment",
        "severity": "Medium",
        "likelihood": "Medium",
        "affectedComponents": ["Flanges", "Valves", "Pump Seals"],
        "mitigationStrategies": ["Leak Detection Systems", "Preventive Maintenance", "Seal Monitoring"]
    },
    {
        "id": "structural-collapse",
        "name": "Structural Collapse",
        "description": "Loss of structural integrity",
        "severity": "High",
        "likelihood": "Low",
        "affectedComponents": ["Support Structures", "Vessel Supports", "Pipe Racks"],
        "mitigationStrategies": ["Structural Analysis", "Load Monitoring", "Corrosion Protection"]
    },
    {
        "id": "functional-failure",
        "name": "Functional Failure",
        "description": "Loss of intended function without immediate safety risk",
        "severity": "Low",
        "likelihood": "Medium",
        "affectedComponents": ["Control Systems", "Instrumentation", "Actuators"],
        "mitigationStrategies": ["Functional Testing", "Redundancy", "Preventive Maintenance"]
    },
    {
        "id": "environmental-release",
        "name": "Environmental Release",
        "description": "Release of hazardous materials to environment",
        "severity": "High",
        "likelihood": "Low",
        "affectedComponents": ["Storage Tanks", "Piping Systems", "Process Equipment"],
        "mitigationStrategies": ["Secondary Containment", "Leak Detection", "Emergency Response"]
    },
    {
        "id": "process-upset",
        "name": "Process Upset",
        "description": "Disruption of normal process conditions",
        "severity": "Medium",
        "likelihood": "Medium",
        "affectedComponents": ["Reactors", "Heat Exchangers", "Control Systems"],
        "mitigationStrategies": ["Process Monitoring", "Safety Interlocks", "Operator Training"]
    },
    {
        "id": "safety-activation",
        "name": "Safety System Activation",
        "description": "Triggering of safety systems",
        "severity": "Medium",
        "likelihood": "Low",
        "affectedComponents": ["Pressure Relief Valves", "Emergency Shutdown Systems", "Fire Protection"],
        "mitigationStrategies": ["Regular Testing", "System Redundancy", "Maintenance"]
    },
    {
        "id": "corrosion-failure",
        "name": "Corrosion-Induced Failure",
        "description": "Failure due to material degradation",
        "severity": "High",
        "likelihood": "Medium",
        "affectedComponents": ["Piping", "Vessels", "Heat Exchangers"],
        "mitigationStrategies": ["Corrosion Monitoring", "Material Selection", "Protective Coatings"]
    },
    {
        "id": "fatigue-failure",
        "name": "Fatigue Failure",
        "description": "Failure due to cyclic loading",
        "severity": "High",
        "likelihood": "Medium",
        "affectedComponents": ["Rotating Equipment", "Pressure Vessels", "Piping Systems"],
        "mitigationStrategies": ["Fatigue Analysis", "Vibration Monitoring", "Design Optimization"]
    },
    {
        "id": "erosion-failure",
        "name": "Erosion-Induced Failure",
        "description": "Failure due to material removal",
        "severity": "Medium",
        "likelihood": "Medium",
        "affectedComponents": ["Piping", "Valves", "Pump Components"],
        "mitigationStrategies": ["Erosion Monitoring", "Material Selection", "Flow Control"]
    }
]

def init_database(collection_name: str = None):
    """
    Initialize the MongoDB database with equipment, fluids, deterioration, and failure scenarios data.
    
    Args:
        collection_name (str, optional): Name of the collection to initialize. 
            If None, all collections will be initialized.
            Valid values: 'equipment', 'fluids', 'deterioration', 'failure_scenarios'
    """
    try:
        # Connect to MongoDB
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        
        # Define collection mapping
        collections = {
            'equipment': EQUIPMENT_DATA,
            'fluids': FLUIDS_DATA,
            'deterioration': DETERIORATION_DATA,
            'failure_scenarios': FAILURE_SCENARIOS_DATA
        }
        
        if collection_name:
            if collection_name not in collections:
                raise ValueError(f"Invalid collection name. Must be one of: {', '.join(collections.keys())}")
            
            # Initialize only the specified collection
            data = collections[collection_name]
            db[collection_name].drop()
            if data:
                db[collection_name].insert_many(data)
                print(f"Inserted {len(data)} {collection_name} items")
            db[collection_name].create_index("id", unique=True)
        else:
            # Initialize all collections
            for name, data in collections.items():
                db[name].drop()
                if data:
                    db[name].insert_many(data)
                    print(f"Inserted {len(data)} {name} items")
                db[name].create_index("id", unique=True)
        
        print("Database initialization completed successfully!")
        
    except Exception as e:
        print(f"Error initializing database: {str(e)}")
    finally:
        client.close()

if __name__ == "__main__":
    # import sys
    # collection_name = sys.argv[1] if len(sys.argv) > 1 else None
    init_database("deterioration")
