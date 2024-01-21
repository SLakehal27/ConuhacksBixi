import pandas as pd
import zipfile
import os

# Path to the zip file (adjust if necessary)
zip_path = 'traitement/Data.zip'

# Unzip the data
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('traitement')

# Assuming the extracted file is a CSV, we'll find the first CSV file in the directory
for file in os.listdir('traitement'):
    if file.endswith('.csv'):
        data_path = os.path.join('traitement', file)
        break

# Read the data into a pandas DataFrame
df = pd.read_csv(data_path)

# Find the most visited start and end locations
# Count occurrences of each STARTSTATIONNAME and ENDSTATIONNAME
start_station_counts = df['STARTSTATIONNAME'].value_counts()
end_station_counts = df['ENDSTATIONNAME'].value_counts()

# Display the most visited locations
print("Most visited start locations:")
print(start_station_counts.head())

#recupere les longitudes et latitudes des stations les plus visitées
df_start = df[df['STARTSTATIONNAME'].isin(start_station_counts.head().index)]
df_start = df_start[['STARTSTATIONNAME','STARTSTATIONLATITUDE','STARTSTATIONLONGITUDE']]
df_start = df_start.drop_duplicates()
df_start = df_start.reset_index(drop=True)
print(df_start)

#save it in a csv file
df_start.to_csv('traitement/Most_start.csv',index=False)


print("\nMost visited end locations:")
print(end_station_counts.head())

#recupere les longitudes et latitudes des stations les plus visitées
df_end = df[df['ENDSTATIONNAME'].isin(end_station_counts.head().index)]
df_end = df_end[['ENDSTATIONNAME','ENDSTATIONLATITUDE','ENDSTATIONLONGITUDE']]
df_end = df_end.drop_duplicates()
df_end = df_end.reset_index(drop=True)
print(df_end)

#save it in a csv file
df_end.to_csv('traitement/Most_end.csv',index=False)

# find the less visited start and end locations
# Count occurrences of each STARTSTATIONNAME and ENDSTATIONNAME
start_station_counts = df['STARTSTATIONNAME'].value_counts()
end_station_counts = df['ENDSTATIONNAME'].value_counts()

# Display the less visited locations
print("\nLess visited start locations:")
print(start_station_counts.tail())

#recupere les longitudes et latitudes des stations les moins visitées
df_start = df[df['STARTSTATIONNAME'].isin(start_station_counts.tail().index)]
df_start = df_start[['STARTSTATIONNAME','STARTSTATIONLATITUDE','STARTSTATIONLONGITUDE']]
df_start = df_start.drop_duplicates()
df_start = df_start.reset_index(drop=True)
print(df_start)

# Save it in a csv file
df_start.to_csv('traitement/Least_start.csv',index=False)

print("\nLess visited end locations:")
print(end_station_counts.tail())

#recupere les longitudes et latitudes des stations les moins visitées
df_end = df[df['ENDSTATIONNAME'].isin(end_station_counts.tail().index)]
df_end = df_end[['ENDSTATIONNAME','ENDSTATIONLATITUDE','ENDSTATIONLONGITUDE']]
df_end = df_end.drop_duplicates()
df_end = df_end.reset_index(drop=True)
print(df_end)

# Save it in a csv file
df_end.to_csv('traitement/Least_end.csv',index=False)

# find all the starts and ends stations that are not in the most visited and less visited stations
# Count occurrences of each STARTSTATIONNAME and ENDSTATIONNAME
start_station_counts = df['STARTSTATIONNAME'].value_counts()
end_station_counts = df['ENDSTATIONNAME'].value_counts()

# Display the less visited locations
print("\nOther start locations:")
print(start_station_counts[~start_station_counts.index.isin(start_station_counts.head().index) & ~start_station_counts.index.isin(start_station_counts.tail().index)])

#recupere les longitudes et latitudes des stations les moins visitées
df_start = df[df['STARTSTATIONNAME'].isin(start_station_counts[~start_station_counts.index.isin(start_station_counts.head().index) & ~start_station_counts.index.isin(start_station_counts.tail().index)].index)]
df_start = df_start[['STARTSTATIONNAME','STARTSTATIONLATITUDE','STARTSTATIONLONGITUDE']]
df_start = df_start.drop_duplicates()
df_start = df_start.reset_index(drop=True)
print(df_start)

# Save it in a csv file
df_start.to_csv('traitement/Average_start.csv',index=False)

print("\nOther end locations:")
print(end_station_counts[~end_station_counts.index.isin(end_station_counts.head().index) & ~end_station_counts.index.isin(end_station_counts.tail().index)])

#recupere les longitudes et latitudes des stations les moins visitées
df_end = df[df['ENDSTATIONNAME'].isin(end_station_counts[~end_station_counts.index.isin(end_station_counts.head().index) & ~end_station_counts.index.isin(end_station_counts.tail().index)].index)]
df_end = df_end[['ENDSTATIONNAME','ENDSTATIONLATITUDE','ENDSTATIONLONGITUDE']]
df_end = df_end.drop_duplicates()
df_end = df_end.reset_index(drop=True)
print(df_end)

# Save it in a csv file
df_end.to_csv('traitement/Average_end.csv',index=False)

