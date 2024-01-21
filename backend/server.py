from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

origins = ["http://localhost:3000"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the path to the data.json file in the treat folder
path = os.path.join(script_dir, '..', 'traitement', 'data.json')

csv= []

try:
    with open(path,'r') as f:
        csv = json.load(f)
except FileNotFoundError:
    print(f"File '{path}' not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON in file '{path}': {e}")
except Exception as e:
    print(f"An error occurred: {e}")


def getType(type : str):
    return [station for station in csv if station["type"] == type]
        

@app.get("/bixi/high")
async def getStart():
    highStations = getType("high")
    if(highStations != []) :
        return highStations
    return []
    
@app.get("/bixi/average")
async def getAverage():
    averageStations = getType("average")
    if(averageStations != []) :
        return averageStations
    return []
    
@app.get("/bixi/low")
async def getStart():
    lowStations = getType("low")
    if(lowStations != []) :
        return lowStations
    return []

@app.get("/data")
async def getData():
    return csv
