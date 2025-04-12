import pandas as pd
from sqlalchemy import create_engine
import os

# 📦 Paramètres de connexion PostgreSQL
db_user = "postgres"
db_password = "yourpassword"
db_host = "host.docker.internal"  # fonctionne sur Docker Desktop (Windows/Mac)
db_port = "5432"
db_name = "nyc_data"
table_name = "nyc_weather_taxi_2024_01"

# 📁 Chemin absolu vers le fichier CSV
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "merged_2024_01.csv")

# 📄 Lire le fichier CSV avec encodage compatible
df = pd.read_csv(csv_path, encoding="latin1")

# 🔌 Créer l'engine SQLAlchemy pour PostgreSQL
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# 🚀 Charger les données dans la table PostgreSQL
df.to_sql(table_name, engine, if_exists="append", index=False)

print(f"✅ Données chargées dans la table PostgreSQL : {table_name}")
