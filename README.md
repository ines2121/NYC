# 🔧 Pipeline de Données Local (ETL) avec PostgreSQL + Entraînement du Modèle sur Google Colab
 
---
 
## 📌 Objectif
- Mettre en place un pipeline **ETL local** avec PostgreSQL.
- Stocker les données mensuelles dans **une table par mois**.
- Effectuer l’entraînement du modèle de **machine learning sur Google Colab**.
 
---
 
## 1. 🔄 Pipeline ETL local avec PostgreSQL
 
### 📥 Extraction
- Les fichiers `.parquet` sont téléchargés en local (déjà fait).
- Utiliser `pandas` ou `pyarrow` pour lire les fichiers localement.
 
### 🧹 Transformation
- Nettoyage des données :
  - Suppression des valeurs nulles.
  - Correction des types de colonnes.
  - Filtrage des valeurs aberrantes.
- Ajout de colonnes utiles (date, heure, météo, etc.).
 
### 🧾 Chargement dans PostgreSQL
- Créer une base `nyc_taxi`.
- Créer **une table par mois** : `yellow_2023_01`, `yellow_2023_02`, etc.
- Utiliser `sqlalchemy` + `pandas.to_sql()` pour charger les données :
 
```python
from sqlalchemy import create_engine
```
 
engine = create_engine("postgresql://username:password@localhost:5432/nyc_taxi")
df.to_sql('yellow_2023_01', engine, if_exists='replace', index=False)

## 2. 🤖 Entraînement du Modèle sur Google Colab (avec PySpark MLlib)
 
### 📤 Chargement des données depuis PostgreSQL

- Connexion à la base PostgreSQL via `sqlalchemy` ou `psycopg2` depuis Google Colab.

- Récupération des tables mensuelles ou consolidation de plusieurs tables selon le besoin (via `UNION ALL` en SQL ou concaténation avec `pandas`).
 
### 📊 Préparation des données

- Séparation des colonnes explicatives (features) et de la variable cible.

- Encodage des variables catégorielles.

- Normalisation ou standardisation si nécessaire.
 
### 🧠 Modélisation (avec PySpark MLlib)

- Utilisation de **PySpark MLlib**, plus adapté aux grands volumes de données que `scikit-learn`.

- Étapes typiques de la modélisation :

  - Encodage des variables catégorielles avec `StringIndexer`

  - Vectorisation des features avec `VectorAssembler`

  - Entraînement d’un modèle de type `RandomForestRegressor`, `LinearRegression`, ou `GBTRegressor`

  - Évaluation des performances avec des métriques telles que **RMSE**, **MAE**, ou **R²**
 
### 💾 Sauvegarde du modèle

- Le modèle entraîné est sauvegardé localement dans un format standard (`.pkl`, `.onnx` ou format MLlib natif).

- Le fichier du modèle est ensuite téléchargé depuis Google Colab pour être utilisé lors du déploiement.
 
---
 
## 3. ☁️ Déploiement du Modèle sur Google Cloud Platform (GCP)
 
### 🛠️ Méthode de déploiement recommandée

- Utilisation de **Cloud Run** pour héberger une API de prédiction légère, basée sur Flask ou FastAPI.

- Le modèle est chargé depuis le stockage (Drive, GCS ou dossier local dans l’image Docker).
 
### 📦 Étapes générales du déploiement

1. **Préparation de l’API** :

   - Une API REST est développée (ex. avec Flask) pour recevoir des requêtes de prédiction.

   - L’API charge le modèle au démarrage et renvoie des prédictions à partir des données reçues en JSON.
 
2. **Création d’un conteneur Docker** :

   - Le code + modèle sont empaquetés dans une image Docker.

   - L’image est poussée sur **Google Container Registry** ou **Artifact Registry**.
 
3. **Déploiement sur Cloud Run** :

   - Cloud Run déploie automatiquement l’image et expose une URL publique (ou sécurisée).

   - L’API est alors prête à recevoir des appels HTTP pour servir des prédictions en temps réel.
 
### 🌍 Résultat attendu

- Un modèle entraîné localement avec PySpark est maintenant exposé via une API scalable sur GCP.

- L’architecture reste simple, portable, et compatible avec des intégrations futures (frontend, webhook, automatisation).
 
---
 
## ✅ Avantages de cette architecture hybride

- 💾 Données en local avec PostgreSQL : maîtrise, sécurité, contrôle.

- ⚙️ Entraînement dans Google Colab avec Spark : scalable, gratuit.

- 🌐 Déploiement cloud avec Cloud Run : rapide, maintenable, accessible via API.

- 🔄 Possibilité d’automatiser l’ensemble via des workflows (GitHub Actions, Cloud Build, Airflow...).

 