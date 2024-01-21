from fastapi import FastAPI

app = FastAPI()

csv= [
    {
        "address": "Jardin Botanique dépôt fierté (Sherbrooke / Pie-IX)",
        "latitude": 45.5567924,
        "longitude": -73.554647,
        "type": "average"
    },
    {
        "address": "Jardin Botanique Dépôt Fierté (Sherbrooke / Pie-IX)",
        "latitude": 45.5567924,
        "longitude": -73.554647,
        "type": "average"
    },
    {
        "address": "Saint-Sylvestre / Labonté",
        "latitude": 45.5354258,
        "longitude": -73.5136585,
        "type": "high"
    },
    {
        "address": "Louis-R.-Renaud / Armand-Frappier",
        "latitude": 45.5545669,
        "longitude": -73.734473,
        "type": "low"
    },
    {
        "address": "St-Timothé / Robin",
        "latitude": 45.5186318,
        "longitude": -73.5611299,
        "type": "high"
    }
]

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