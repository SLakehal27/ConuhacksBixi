import pandas as pd
import zipfile
import os

#delete de Data.csv and DonneesBixi.csv if they exist
if os.path.exists("traitement/Data.csv"):
    os.remove("traitement/Data.csv")
if os.path.exists("traitement/DonneesBixi.csv"):
    os.remove("traitement/DonneesBixi.csv")

# Path to the zip file (adjust if necessary)
zip_path = 'traitement/Data.zip'

# Unzip the data
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('traitement')

# Find the first CSV file in the directory
for file in os.listdir('traitement'):
    if file.endswith('.csv'):
        data_path = os.path.join('traitement', file)
        break

# Read the data into a pandas DataFrame
df = pd.read_csv(data_path)

# Count occurrences of each STARTSTATIONNAME
start_station_counts = df['STARTSTATIONNAME'].value_counts()

# Remove duplicates
df = df.drop_duplicates(subset=['STARTSTATIONNAME', 'STARTSTATIONLATITUDE', 'STARTSTATIONLONGITUDE'], keep='first')
df = df.drop_duplicates(subset=['ENDSTATIONNAME', 'ENDSTATIONLATITUDE', 'ENDSTATIONLONGITUDE'], keep='first')

# Create a mapping of station names to their visit counts
station_visit_map = start_station_counts.to_dict()

# Replace station names with their visit counts
df['STARTSTATION_VISIT_COUNT'] = df['STARTSTATIONNAME'].map(station_visit_map)

# Define categories based on visit counts
max_visit = max(station_visit_map.values())
df['ACHALENDEMENT'] = df['STARTSTATION_VISIT_COUNT'].apply(
    lambda x: 'low' if x < max_visit / 3 else 'average' if x < 2 * max_visit / 3 else 'high'
)

# Drop columns 
df = df.drop(columns=['STARTSTATIONARRONDISSEMENT'])
df = df.drop(columns=['ENDSTATIONNAME', 'ENDSTATIONLATITUDE', 'ENDSTATIONLONGITUDE'])
df = df.drop(columns=['STARTTIMEMS','ENDTIMEMS','STARTSTATION_VISIT_COUNT'])
df = df.drop(columns=['ENDSTATIONARRONDISSEMENT'])


# Save the DataFrame to a CSV file
df.to_csv('traitement/Data.csv', index=False)