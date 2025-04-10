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

## 2. 🤖 Entraînement du Modèle sur Google Colab
 
### 📤 Chargement des données depuis PostgreSQL

- Connexion à PostgreSQL via `sqlalchemy` ou `psycopg2`.

- Charger une ou plusieurs tables :

  - En exécutant une requête SQL avec `UNION`

  - Ou en important chaque table séparément et en les concaténant avec `pandas`
 
### 📊 Préparation des données

- Séparer les colonnes explicatives (**features `X`**) et la variable cible (**`y`**).

- Appliquer les transformations nécessaires :

  - Encodage des variables catégorielles (`OneHotEncoder`, `LabelEncoder`, etc.)

  - Normalisation ou standardisation (`StandardScaler`, `MinMaxScaler`, etc.)
 
### 🧠 Modélisation

- Utiliser des bibliothèques comme :

  - `scikit-learn` (RandomForest, LinearRegression, etc.)

  - `xgboost` pour des modèles plus performants

  - `pyspark.ml` si les données sont très volumineuses

- Entraîner un modèle sur les données préparées

- Évaluer les performances à l’aide de métriques :

  - **RMSE** (Root Mean Squared Error)

  - **MAE** (Mean Absolute Error)

  - **R²** (Coefficient de détermination)
 
### 💾 Sauvegarde du modèle

- Sauvegarder le modèle entraîné avec :

  - `joblib.dump(model, "model.pkl")`

  - ou `pickle.dump(model, open("model.pkl", "wb"))`

- Télécharger le fichier `.pkl` depuis Colab pour l’utiliser plus tard (déploiement, test, etc.)
 
---
 
### ✅ Avantages de cette approche

- 🎯 Pipeline **maîtrisé de bout en bout en local**

- 📦 **PostgreSQL** pour un **stockage structuré, fiable et performant**

- 💻 **Google Colab** comme environnement d’entraînement ML **gratuit et simple**

- 🔄 Pipeline **évolutif** vers un déploiement dans le cloud (**GCP**, **AWS**, etc.)

 