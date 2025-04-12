import pandas as pd
import requests
import os
from datetime import datetime

# Configuration des dates
start_date = "2023-01-01"
end_date = datetime.today().strftime("%Y-%m-%d")

# Configuration de la requête
base_url = "https://www.ncei.noaa.gov/access/services/data/v1"
params = {
    "dataset": "daily-summaries",
    "stations": "USW00094728,USW00014732,USW00094789",
    "startDate": start_date,
    "endDate": end_date,
    "dataTypes": "TMIN,TMAX,PRCP",
    "format": "json",
    "includeAttributes": "true",
    "includeStationName": "true",
    "includeStationLocation": "true",
    "units": "metric"
}

# Faire la requête
response = requests.get(base_url, params=params)

# Créer le dossier de sortie s'il n'existe pas
output_folder = "./nyc_weather_data"
os.makedirs(output_folder, exist_ok=True)

# Vérifier la réponse
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df["DATE"] = pd.to_datetime(df["DATE"])

    # Sauvegarde au format CSV
    output_path = os.path.join(output_folder, "nyc_weather_2023_to_today.csv")
    df.to_csv(output_path, index=False)
    print(f"✅ Données sauvegardées dans {output_path}")
else:
    print("❌ Erreur:", response.status_code, response.text)
