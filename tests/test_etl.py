# tests/test_etl.py

import pytest
import pandas as pd
from io import StringIO
from src.etl import extract_data, cleanup_column, prepare_data, save_data, train_model

# Test de la fonction extract_data
def test_extract_data():
    df = extract_data()
    assert isinstance(df, pd.DataFrame), "La sortie de extract_data doit être un DataFrame"
    assert not df.empty, "Les données extraites ne doivent pas être vides"

# Test de la fonction cleanup_column
def test_cleanup_column():
    data = {
        'CustomerID': [1, 2],
        'Churn': ['Yes', 'No'],
        'StreamingTV': ['No', 'Yes']
    }
    df = pd.DataFrame(data)
    cleaned_df = cleanup_column(df)
    
    assert 'customer_id' in cleaned_df.columns, "La colonne 'CustomerID' doit être renommée 'customer_id'"
    assert 'streaming_tv' in cleaned_df.columns, "La colonne 'StreamingTV' doit être renommée 'streaming_tv'"

# Test de la fonction prepare_data
def test_prepare_data():
    data = {
        'customer_id': [1, 2],
        'churn': ['Yes', 'No'],
        'age': [25, 30]
    }
    df = pd.DataFrame(data)
    prepared_df = prepare_data(df)
    
    assert 'churn' in prepared_df.columns, "La colonne 'churn' doit être présente dans les données préparées"
    assert prepared_df['churn'].iloc[0] == 1, "La valeur de 'churn' pour 'Yes' doit être 1"
    assert prepared_df['churn'].iloc[1] == 0, "La valeur de 'churn' pour 'No' doit être 0"
    
    assert prepared_df.shape[0] == 2, "Le nombre de lignes préparées doit être égal à 2"
    assert not prepared_df.isnull().values.any(), "Les données préparées ne doivent pas contenir de valeurs nulles"

# # Test de la fonction save_data (simulation de sauvegarde)
# def test_save_data(monkeypatch):
#     # Créer un DataFrame temporaire
#     data = {'customer_id': [1, 2], 'churn': [1, 0]}
#     df = pd.DataFrame(data)

#     # Simuler la sauvegarde pour vérifier que la fonction est appelée sans écrire sur le disque
#     def mock_to_csv(self, path, index):
#         assert path == '../data/raw_data.csv', f"Le chemin du fichier est incorrect, attendu '../data/raw_data.csv', obtenu {path}"
#         assert index is False, "L'index ne doit pas être sauvegardé"
    
#     monkeypatch.setattr(df, 'to_csv', mock_to_csv)
    
#     save_data(df)

# # Test de la fonction train_model
# def test_train_model(monkeypatch):
#     # Mock de joblib.dump pour ne pas écrire sur le disque
#     def mock_dump(model, path):
#         assert path == '../models/logistic_model.pkl', f"Le chemin du modèle est incorrect, attendu '../models/logistic_model.pkl', obtenu {path}"
    
#     monkeypatch.setattr(joblib, 'dump', mock_dump)
    
#     # Créer un DataFrame pour l'entraînement
#     data = {'customer_id': [1, 2], 'churn': [1, 0], 'age': [25, 30]}
#     df = pd.DataFrame(data)
#     df.to_csv('../data/cleaned_data.csv', index=False)
    
#     train_model()
