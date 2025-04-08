## 📌 Étapes effectuées dans le projet

### 1. Récupération des données météo NYC (Script `Script_meteo.py`)
- Utilisation de l’API NOAA (`daily-summaries`) pour collecter les données météo quotidiennes de plusieurs stations à New York.
- Données récupérées : température minimale (TMIN), température maximale (TMAX), précipitations (PRCP).
- Période couverte : du **1er janvier 2023** jusqu’à **aujourd’hui** (mise à jour dynamique).
- Données automatiquement sauvegardées dans le dossier `nyc_weather_data/` au format `.csv`.

### 2. Automatisation de la mise à jour des données
- Le script vérifie s’il existe déjà un fichier `nyc_weather_2023_to_today.csv`.
- Si le fichier existe, seules les **nouvelles données** depuis la dernière date enregistrée sont téléchargées.
- Cela permet une exécution planifiée (via `cron` ou autre) sans duplication.

### 3. Gestion du dépôt Git
- Initialisation du dépôt Git local avec `git init`.
- Ajout de tous les fichiers avec `git add .`.

### 4. Configuration du fichier `.gitignore`
- Exclusion du dossier `nyc_yellow_taxi_parquet/` contenant des fichiers `.parquet` lourds non nécessaires dans le dépôt Git.
- Ligne ajoutée dans `.gitignore` :
  ```bash
  /nyc_yellow_taxi_parquet/
