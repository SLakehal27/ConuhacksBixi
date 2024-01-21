import pandas as pd
import zipfile
import os
import matplotlib.pyplot as plt

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

# sort by ACHALENDEMENT putting the ones with the ACHALENDEMENT 'high' first and the 'low' last
achalandement_mapping = {'high': 3, 'average': 2, 'low': 1}
df['ACHALENDEMENT_SORT'] = df['ACHALENDEMENT'].map(achalandement_mapping)

# Sort by ACHALENDEMENT
df = df.sort_values(by='ACHALENDEMENT_SORT', ascending=False)

# Drop the temporary sorting column
df = df.drop(columns=['ACHALENDEMENT_SORT'])

# Filtrer les données pour les stations avec un achalandement 'high' et 'low'
high_achalandement_df = df[df['ACHALENDEMENT'] == 'high']
low_achalandement_df = df[df['ACHALENDEMENT'] == 'low']

# Créer un graphique pour les stations avec un achalandement 'high'
plt.figure(figsize=(10, 6))
plt.hist(high_achalandement_df['STARTSTATIONNAME'], bins=30, color='green')
plt.title('Nombre de Visites des Stations de Départ avec Achalandement Élevé')
plt.xlabel('Stations de Départ')
plt.ylabel('Nombre de Visites')
plt.xticks(rotation=90)
plt.tight_layout()
# Sauvegarder le graphique
plt.savefig('traitement/high_achalandement.png')
plt.close()

# Créer un graphique pour les stations avec un achalandement 'low'
plt.figure(figsize=(10, 6))
plt.hist(low_achalandement_df['STARTSTATIONNAME'], bins=30, color='red')
plt.title('Nombre de Visites des Stations de Départ avec Achalandement Faible')
plt.xlabel('Stations de Départ')
plt.ylabel('Nombre de Visites')
plt.xticks(rotation=90)
plt.tight_layout()
# Sauvegarder le graphique
plt.savefig('traitement/low_achalandement.png')
plt.close()

# Drop columns 
df = df.drop(columns=['STARTSTATIONARRONDISSEMENT'])
df = df.drop(columns=['ENDSTATIONNAME', 'ENDSTATIONLATITUDE', 'ENDSTATIONLONGITUDE'])
df = df.drop(columns=['STARTTIMEMS','ENDTIMEMS','STARTSTATION_VISIT_COUNT'])
df = df.drop(columns=['ENDSTATIONARRONDISSEMENT'])

# Save the final DataFrame to a new CSV file
df.to_csv('traitement/DonneesBixi.csv', index=False)


# Save the DataFrame to a CSV file
df.to_csv('traitement/Data.csv', index=False)