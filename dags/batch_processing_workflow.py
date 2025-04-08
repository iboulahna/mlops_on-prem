from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
from sklearn.datasets import make_classification
import os

# Fonction pour générer des données synthétiques
def generate_synthetic_data():
    X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_classes=2, random_state=42)
    df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(1, 11)])
    df['churn'] = y
    return df

# Fonction pour sauvegarder les données synthétiques
def save_synthetic_data():
    df = generate_synthetic_data()
    df.to_csv('../data/synthetic_data.csv', index=False)
    print("Données synthétiques générées et sauvegardées")

# Définir les arguments du DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 3, 17),
    'retries': 0,
    'catchup': False,
}

# Créer le DAG
dag = DAG(
    'batch_processing_workflow',
    default_args=default_args,
    description='Un workflow pour générer des données synthétiques',
    schedule_interval=None,  # Peut être déclenché manuellement
)

# Définir la tâche de génération et de sauvegarde des données synthétiques
task_generate_save_synthetic_data = PythonOperator(
    task_id='generate_save_synthetic_data',
    python_callable=save_synthetic_data,
    dag=dag,
)

