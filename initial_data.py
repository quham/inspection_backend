EQUIPMENT_DATA = [
    # Pumps
    {
        "id": "pump-cent-1",
        "category": "Pumps",
        "type": "Centrifugal",
        "subtype": "Horizontal",
        "name": "Horizontal Centrifugal Pump",
        "image": "/placeholder.svg"
    },
    {
        "id": "pump-cent-2",
        "category": "Pumps",
        "type": "Centrifugal",
        "subtype": "Vertical",
        "name": "Vertical Centrifugal Pump",
        "image": "/placeholder.svg"
    },
    {
        "id": "pump-pos-1",
        "category": "Pumps",
        "type": "Positive Displacement",
        "subtype": "Gear",
        "name": "Gear Pump",
        "image": "/placeholder.svg"
    },
    {
        "id": "pump-pos-2",
        "category": "Pumps",
        "type": "Positive Displacement",
        "subtype": "Diaphragm",
        "name": "Diaphragm Pump",
        "image": "/placeholder.svg"
    },

    # Heat Exchangers
    {
        "id": "hx-shell-1",
        "category": "Heat Exchangers",
        "type": "Shell and Tube",
        "subtype": "Fixed Tube Sheet",
        "name": "Fixed Tube Sheet Heat Exchanger",
        "image": "/placeholder.svg"
    },
    {
        "id": "hx-shell-2",
        "category": "Heat Exchangers",
        "type": "Shell and Tube",
        "subtype": "Floating Head",
        "name": "Floating Head Heat Exchanger",
        "image": "/placeholder.svg"
    },
    {
        "id": "hx-plate-1",
        "category": "Heat Exchangers",
        "type": "Plate",
        "subtype": "Gasketed",
        "name": "Gasketed Plate Heat Exchanger",
        "image": "/placeholder.svg"
    },

    # Pressure Vessels
    {
        "id": "vessel-storage-1",
        "category": "Pressure Vessels",
        "type": "Storage",
        "subtype": "Horizontal",
        "name": "Horizontal Storage Vessel",
        "image": "/placeholder.svg"
    },
    {
        "id": "vessel-storage-2",
        "category": "Pressure Vessels",
        "type": "Storage",
        "subtype": "Vertical",
        "name": "Vertical Storage Vessel",
        "image": "/placeholder.svg"
    },
    {
        "id": "vessel-reactor-1",
        "category": "Pressure Vessels",
        "type": "Reactor",
        "subtype": "Continuous Stirred Tank",
        "name": "CSTR Reactor",
        "image": "/placeholder.svg"
    },

    # Piping
    {
        "id": "pipe-carbon-1",
        "category": "Piping",
        "type": "Carbon Steel",
        "name": "Carbon Steel Pipe",
        "image": "/placeholder.svg"
    },
    {
        "id": "pipe-ss-1",
        "category": "Piping",
        "type": "Stainless Steel",
        "name": "Stainless Steel Pipe",
        "image": "/placeholder.svg"
    },
    {
        "id": "pipe-alloy-1",
        "category": "Piping",
        "type": "Alloy",
        "name": "Alloy Pipe",
        "image": "/placeholder.svg"
    }
]

# Fluids data
FLUIDS_DATA = [
    # Gases
    {
        "id": "gas-natural",
        "category": "Gas",
        "name": "Natural Gas",
        "compatibleWith": ["pipe-carbon-1", "pipe-ss-1", "vessel-storage-1", "vessel-storage-2"]
    },
    {
        "id": "gas-hydrogen",
        "category": "Gas",
        "name": "Hydrogen",
        "compatibleWith": ["pipe-ss-1", "pipe-alloy-1", "vessel-storage-2"]
    },
    {
        "id": "gas-nitrogen",
        "category": "Gas",
        "name": "Nitrogen",
        "compatibleWith": ["pipe-carbon-1", "pipe-ss-1", "pipe-alloy-1", "vessel-storage-1", "vessel-storage-2"]
    },

    # Liquids - Hydrocarbons
    {
        "id": "liquid-crude",
        "category": "Liquid - Hydrocarbon",
        "name": "Crude Oil",
        "compatibleWith": ["pipe-carbon-1", "pump-cent-1", "pump-cent-2", "pump-pos-1", "vessel-storage-1"]
    },
    {
        "id": "liquid-diesel",
        "category": "Liquid - Hydrocarbon",
        "name": "Diesel",
        "compatibleWith": ["pipe-carbon-1", "pump-cent-1", "pump-cent-2", "pump-pos-1", "vessel-storage-1"]
    },
    {
        "id": "liquid-gasoline",
        "category": "Liquid - Hydrocarbon",
        "name": "Gasoline",
        "compatibleWith": ["pipe-carbon-1", "pump-cent-1", "pump-cent-2", "pump-pos-1", "vessel-storage-1"]
    },

    # Liquids - Aqueous
    {
        "id": "liquid-water",
        "category": "Liquid - Aqueous",
        "name": "Water",
        "compatibleWith": ["pipe-carbon-1", "pipe-ss-1", "pump-cent-1", "pump-cent-2", "hx-shell-1", "hx-shell-2", "hx-plate-1"]
    },
    {
        "id": "liquid-acid-hcl",
        "category": "Liquid - Aqueous",
        "name": "Hydrochloric Acid",
        "compatibleWith": ["pipe-ss-1", "pipe-alloy-1", "pump-pos-2"]
    },
    {
        "id": "liquid-acid-h2so4",
        "category": "Liquid - Aqueous",
        "name": "Sulfuric Acid",
        "compatibleWith": ["pipe-ss-1", "pipe-alloy-1", "pump-pos-2"]
    },

    # Slurries
    {
        "id": "slurry-coal",
        "category": "Slurry",
        "name": "Coal Slurry",
        "compatibleWith": ["pipe-alloy-1", "pump-pos-1", "pump-pos-2"]
    },
    {
        "id": "slurry-catalyst",
        "category": "Slurry",
        "name": "Catalyst Slurry",
        "compatibleWith": ["pipe-ss-1", "pipe-alloy-1", "pump-pos-2", "vessel-reactor-1"]
    }
]




# Deterioration data
DETERIORATION_DATA = [
    {
        "id": "corr-general",
        "name": "General Corrosion",
        "description": "Uniform thinning of material due to electrochemical reaction with environment",
        "likelihood": "Medium",
        "affectedAreas": ["Vessel Shell", "Pipe Walls", "Heat Exchanger Tubes"],
        "contributingFactors": ["Oxygen Content", "Temperature", "Fluid Chemistry", "Material Selection"],
        "comment": ""
    },
    {
        "id": "corr-pitting",
        "name": "Pitting Corrosion",
        "description": "Localized form of corrosion that results in small holes in the material",
        "likelihood": "High",
        "affectedAreas": ["Pipe Bends", "Vessel Bottom", "Welds"],
        "contributingFactors": ["Chlorides", "Stagnant Areas", "Oxygen Concentration Cells"],
        "comment": ""
    },
    {
        "id": "erosion-particle",
        "name": "Particle Erosion",
        "description": "Material removal due to impingement of solid particles entrained in fluid",
        "likelihood": "High",
        "affectedAreas": ["Pipe Bends", "Valve Internals", "Pump Impellers"],
        "contributingFactors": ["Particle Size", "Flow Velocity", "Impact Angle", "Material Hardness"],
        "comment": ""
    },
    {
        "id": "fatigue-mech",
        "name": "Mechanical Fatigue",
        "description": "Progressive damage due to cyclic loading",
        "likelihood": "Medium",
        "affectedAreas": ["Pressure Cycling Areas", "Vibration Prone Components", "Rotating Equipment"],
        "contributingFactors": ["Pressure Cycling", "Vibration", "Stress Concentrations"],
        "comment": ""
    },
    {
        "id": "crack-scc",
        "name": "Stress Corrosion Cracking",
        "description": "Formation of cracks due to simultaneous presence of tensile stress and corrosive environment",
        "likelihood": "Low",
        "affectedAreas": ["High Stress Areas", "Heat Affected Zones", "Cold Worked Regions"],
        "contributingFactors": ["Tensile Stress", "Corrosive Species", "Temperature", "Material Susceptibility"],
        "comment": ""
    },
    {
        "id": "corr-cui",
        "name": "Corrosion Under Insulation",
        "description": "Hidden corrosion occurring beneath insulation materials where moisture becomes trapped",
        "likelihood": "High",
        "affectedAreas": ["Insulated Pipelines", "Vessel Exteriors", "Heat Exchangers"],
        "contributingFactors": ["Moisture Ingress", "Damaged Insulation", "Temperature Cycling", "Inadequate Barriers"],
        "comment": ""
    },
    {
        "id": "corr-mic",
        "name": "Microbially Induced Corrosion",
        "description": "Corrosion influenced by the presence and activities of microorganisms",
        "likelihood": "Medium",
        "affectedAreas": ["Stagnant Areas", "Low Flow Regions", "Tank Bottoms", "Dead Legs"],
        "contributingFactors": ["Nutrient Availability", "Biofilm Formation", "Temperature Range", "Oxygen Level"],
        "comment": ""
    },
    {
        "id": "corr-galvanic",
        "name": "Galvanic Corrosion",
        "description": "Accelerated corrosion of less noble metal when in electrical contact with a more noble metal",
        "likelihood": "Medium",
        "affectedAreas": ["Dissimilar Metal Joints", "Flanges", "Threaded Connections"],
        "contributingFactors": ["Electrolyte Presence", "Difference in Nobility", "Area Ratio", "Conductivity"],
        "comment": ""
    },
    {
        "id": "corr-crevice",
        "name": "Crevice Corrosion",
        "description": "Localized attack in confined spaces where stagnant solution conditions develop",
        "likelihood": "Medium",
        "affectedAreas": ["Flange Faces", "Threaded Joints", "Under Deposits", "Gasket Interfaces"],
        "contributingFactors": ["Geometry", "Tight Gaps", "Oxygen Differential", "Chlorides"],
        "comment": ""
    },
    {
        "id": "erosion-fac",
        "name": "Flow Accelerated Corrosion",
        "description": "Dissolution of protective oxide layers and base metal due to high-velocity fluid flow",
        "likelihood": "High",
        "affectedAreas": ["Elbows", "T-Junctions", "Downstream of Flow Restrictions", "Steam Systems"],
        "contributingFactors": ["Flow Velocity", "pH", "Temperature", "Dissolved Oxygen", "Material Composition"],
        "comment": ""
    },
    {
        "id": "corr-deadleg",
        "name": "Dead Leg Corrosion",
        "description": "Accelerated corrosion in sections of piping with little or no flow",
        "likelihood": "Medium",
        "affectedAreas": ["Bypasses", "Infrequently Used Branches", "Drain Lines", "Relief Valve Inlet Piping"],
        "contributingFactors": ["Stagnant Conditions", "Solids Accumulation", "Chemical Concentration", "MIC"],
        "comment": ""
    },
    {
        "id": "fatigue-thermal",
        "name": "Thermal Fatigue",
        "description": "Damage from cyclic stresses due to temperature fluctuations",
        "likelihood": "Medium",
        "affectedAreas": ["Heat Exchangers", "Steam Systems", "Injection Points", "Mix Points"],
        "contributingFactors": ["Temperature Cycling Range", "Cycling Frequency", "Material Properties", "Constraints"],
        "comment": ""
    },
    {
        "id": "htha",
        "name": "High Temperature Hydrogen Attack",
        "description": "Degradation of steel due to hydrogen diffusion at elevated temperatures",
        "likelihood": "Low",
        "affectedAreas": ["Hydroprocessing Units", "Hydrogen-Containing Systems", "High Temperature Equipment"],
        "contributingFactors": ["Hydrogen Partial Pressure", "Temperature", "Carbon Content", "Material Selection"],
        "comment": ""
    },
    {
        "id": "hydrogen-damage",
        "name": "Hydrogen Induced Cracking",
        "description": "Formation of internal cracks due to hydrogen absorption and pressure",
        "likelihood": "Low",
        "affectedAreas": ["H2S Service Equipment", "Sour Water Systems", "Hydroprocessing Units"],
        "contributingFactors": ["H2S Presence", "pH", "Temperature", "Material Hardness", "Stress Level"],
        "comment": ""
    },
    {
        "id": "hydrogen-embrittle",
        "name": "Hydrogen Embrittlement",
        "description": "Loss of ductility and strength due to hydrogen absorption into metal",
        "likelihood": "Medium",
        "affectedAreas": ["High Strength Materials", "Bolting", "Welded Areas"],
        "contributingFactors": ["Material Strength", "Applied Stress", "Hydrogen Source", "Temperature"],
        "comment": ""
    },
    {
        "id": "erosion-cavitation",
        "name": "Cavitation",
        "description": "Material damage due to formation and collapse of vapor bubbles in liquid",
        "likelihood": "Medium",
        "affectedAreas": ["Pump Impellers", "Valve Trim", "Piping Downstream of Restrictions"],
        "contributingFactors": ["Pressure Drops", "Flow Velocity", "Fluid Properties", "Equipment Design"],
        "comment": ""
    },
    {
        "id": "creep",
        "name": "Creep",
        "description": "Time-dependent deformation under stress at elevated temperatures",
        "likelihood": "Medium",
        "affectedAreas": ["High Temperature Equipment", "Furnace Components", "Boiler Tubes"],
        "contributingFactors": ["Temperature", "Stress Level", "Time", "Material Properties"],
        "comment": ""
    },
    {
        "id": "brittle-fracture",
        "name": "Brittle Fracture",
        "description": "Sudden failure of material with little to no plastic deformation",
        "likelihood": "Low",
        "affectedAreas": ["Carbon Steel Components", "Pressure Vessels", "Low Temperature Service"],
        "contributingFactors": ["Low Temperature", "Material Toughness", "Stress Raisers", "Impact Loading"],
        "comment": ""
    },
    {
        "id": "corr-ammonium",
        "name": "Ammonium Chloride Corrosion",
        "description": "Corrosion due to formation of ammonium chloride deposits in hydrocarbon processing units",
        "likelihood": "Medium",
        "affectedAreas": ["Overhead Systems", "Heat Exchangers", "Condensing Zones"],
        "contributingFactors": ["Temperature", "NH3 and HCl Concentration", "Water Dew Point", "Materials"],
        "comment": ""
    },
    {
        "id": "coating-lining",
        "name": "Lining Deterioration",
        "description": "Breakdown of protective internal linings in vessels and piping",
        "likelihood": "Medium",
        "affectedAreas": ["Lined Vessels", "Storage Tanks", "Chemical Process Equipment"],
        "contributingFactors": ["Chemical Exposure", "Temperature Cycling", "Mechanical Damage", "Age"],
        "comment": ""
    },
    {
        "id": "nonmetallic-deterioration",
        "name": "Non-metallic Deterioration",
        "description": "Degradation of non-metallic components due to environmental factors",
        "likelihood": "Medium",
        "affectedAreas": ["Gaskets", "Seals", "Elastomeric Components", "Composite Materials"],
        "contributingFactors": ["Chemical Exposure", "Temperature", "UV Radiation", "Mechanical Stress"],
        "comment": ""
    }
]