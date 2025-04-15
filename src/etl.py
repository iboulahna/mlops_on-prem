# src/etl.py

import pandas as pd
import re
import requests
from io import StringIO
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Fonction pour extraire les données
def extract_data():
    url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"  # Remplacer par ton URL
    response = requests.get(url)
    csv = response.text
    df = pd.read_csv(StringIO(csv), sep=",")
    print("Données extraites")
    return df

# Fonction de nettoyage des colonnes
def cleanup_column(df):
    df.columns = [re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower().replace("__", "_") for name in df.columns]
    df.columns = [re.sub(r'[\(\)]', '', name).lower() for name in df.columns]
    df.columns = [re.sub(r'[ -]', '_', name).lower() for name in df.columns]
    return df.rename(columns = {'streaming_t_v': 'streaming_tv', 'customer_i_d': 'customer_id'})

# Fonction de préparation des données
def prepare_data(df):
    df = cleanup_column(df)
    df['churn'] = pd.to_numeric(df['churn'].replace({'Yes': 1, 'No': 0}), errors='coerce')
    df_numeric =  df.select_dtypes(include=['number'])
    df_clean = df_numeric.dropna() 
    return df_clean

# Fonction de sauvegarde des données
def save_data(df):
    df.to_csv('../data/raw_data.csv', index=False)
    print("Données sauvegardées")

# Fonction d'extraction, de nettoyage et de sauvegarde
def extract_save():
    df = extract_data()
    save_data(df)

# Fonction pour entraîner un modèle simple
def train_model():
    df = pd.read_csv('../data/cleaned_data.csv')
    X = df.drop('churn', axis=1)
    y = df['churn']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    joblib.dump(model, '../models/logistic_model.pkl')
    print("Modèle entraîné et sauvegardé")
