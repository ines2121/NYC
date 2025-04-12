# 🗽 NYC Yellow Taxi – Pipeline ETL local avec PySpark + PostgreSQL

Ce projet met en place un pipeline de traitement de données local pour les trajets de taxis jaunes à New York, avec intégration des données météo.

---

## 📦 Objectif actuel

- Téléchargement des fichiers `.parquet` Yellow Taxi depuis le site NYC Open Data
- Nettoyage, enrichissement et jointure avec les données météo (CSV)
- Export des données finales (par mois) en `.csv` et `.parquet`
- Chargement des fichiers nettoyés dans une base PostgreSQL locale
- Organisation du projet en scripts Python et Jupyter Notebook
- Gestion versionnée du projet sur GitHub (en excluant les fichiers >100 Mo)

---

## 🔧 Technologies utilisées

- **Python 3.12**
- **PySpark 3.5**
- **PostgreSQL 14 (Docker)**
- **pgAdmin (Docker)**
- **Pandas / SQLAlchemy / psycopg2**
- **Jupyter Notebook (via Docker)**
- **Git + GitHub**

---

## 📂 Structure du projet

```bash
nyc-etl-pipeline/
├── app/
│   └── etl_pipeline.ipynb          # Notebook PySpark pour l'ETL complet
├── data/
│   ├── nyc_yellow_taxi_parquet/    # Fichiers bruts parquet
│   ├── nyc_weather_data/           # Fichier météo CSV
│   └── final/                      # Fichiers transformés (.csv/.parquet)
├── script-load-data/
│   └── load_csv_to_postgres.py     # Script pour charger un CSV dans PostgreSQL
├── spark-3.5.3-bin-hadoop3.tgz     # Archive Spark (ignorée par Git)
├── docker-compose.yml              # PostgreSQL + pgAdmin
├── Dockerfile                      # Spark + Jupyter
├── .env                            # Connexion à PostgreSQL
├── .gitignore                      # Fichiers à exclure du versionnement
└── README.md
```

## 🧩 À venir (prochaines étapes)

- [ ] Automatiser l’ingestion mois par mois
- [ ] Pipeline complet avec **PostgreSQL**
- [ ] Entraînement du modèle de Machine Learning dans **Google Colab** ou avec **Spark MLlib**
- [ ] Déploiement du modèle via **Flask** ou **Streamlit** (sur le **cloud GCP**)
