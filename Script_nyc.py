import os
import requests
from datetime import datetime
 
def download_yellow_taxi_data(start_year=2023):
    today = datetime.today()
    current_year = today.year
    current_month = today.month
 
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "nyc_yellow_taxi_parquet")
    os.makedirs(output_dir, exist_ok=True)
 
    for year in range(start_year, current_year + 1):
        max_month = 12
        if year == current_year:
            max_month = current_month - 1  # Évite de télécharger les mois futurs
 
        for month in range(1, max_month + 1):
            file_name = f"yellow_tripdata_{year}-{month:02d}.parquet"
            url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{file_name}"
            local_path = os.path.join(output_dir, file_name)
 
            try:
                print(f"📥 Téléchargement de {file_name}...")
                response = requests.get(url, stream=True, timeout=30)
 
                if response.status_code == 200:
                    with open(local_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    print(f"✅ Fichier enregistré : {local_path}")
                else:
                    print(f"⚠️ Fichier non disponible (HTTP {response.status_code}) : {url}")
            except Exception as e:
                print(f"❌ Erreur lors du téléchargement de {file_name} : {e}")
 
# Exécution
if __name__ == "__main__":
    download_yellow_taxi_data()