from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

# Default arguments for the DAG
default_args = {
    'start_date': datetime(2024, 1, 1),
}

# Define the DAG with schedule_interval inside the DAG context
dag = DAG(
    'my_dag',
    default_args=default_args,
    schedule_interval='@daily'  # Place the schedule_interval directly here
)

# Task definitions
task1 = BashOperator(task_id='task1', bash_command='echo "Task 1"', dag=dag)
task2 = BashOperator(task_id='task2', bash_command='echo "Task 2"', dag=dag)

# Task dependencies (task1 must run before task2)
task1 >> task2


# task3 = BashOperator(task_id='task3', bash_command='echo "Task 3"')
# task1 >> task3


# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime
# import requests
# import pandas as pd
# from io import StringIO
# import re
# import joblib
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression

# # Définir la fonction de sauvegarde des données
# def save_data(df):
#     df.to_csv('../data/raw_data.csv', index=False)
#     print("Données sauvegardées")

# # Fonction pour extraire les données et les sauvegarder
# def extract_data():
#     url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"  # Remplacer par ton URL
#     response = requests.get(url)
#     csv = response.text
#     df = pd.read_csv(StringIO(csv), sep=",")
#     print("Données extraites")
#     return df 

# # Fonction d'extraction et de sauvegarde
# def extract_save():
#     df = extract_data()
#     save_data(df)

# # Fonction de nettoyage des colonnes
# def cleanup_column(pdf):
#     pdf.columns = [re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower().replace("__", "_") for name in pdf.columns]
#     pdf.columns = [re.sub(r'[\(\)]', '', name).lower() for name in pdf.columns]
#     pdf.columns = [re.sub(r'[ -]', '_', name).lower() for name in pdf.columns]
#     return pdf.rename(columns = {'streaming_t_v': 'streaming_tv', 'customer_i_d': 'customer_id'})

# # Fonction de préparation des données
# def prepare_data(df):
#     df = cleanup_column(df)
#     df['churn'] = pd.to_numeric(df['churn'].replace({'Yes': 1, 'No': 0}), errors='coerce')
#     df_numeric =  df.select_dtypes(include=['number'])
#     df_clean = df_numeric.dropna() 
#     return df_clean 

# # Fonction de sauvegarde des données préparées
# def prepare_save():
#     df = pd.read_csv('../data/raw_data.csv')
#     df_clean = prepare_data(df)
#     df_clean.to_csv('../data/cleaned_data.csv', index=False) 
#     print("Données préparées et sauvegardées")

# # Fonction pour entraîner un modèle simple
# def train_model():
#     df = pd.read_csv('../data/cleaned_data.csv')
#     X = df.drop('churn', axis=1)
#     y = df['churn']
    
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
#     model = LogisticRegression()
#     model.fit(X_train, y_train)
    
#     joblib.dump(model, '../models/logistic_model.pkl')
#     print("Modèle entraîné et sauvegardé")

# # Définir les arguments du DAG
# default_args = {
#     'owner': 'airflow',
#     'start_date': datetime(2025, 3, 17, 23, 30),  # Modifier la date de début pour permettre une exécution plus tôt
#     'end_date': datetime(2025, 3, 17, 23, 55),
#     'retries': 0,
#     'catchup': False,
# }

# # Définir le DAG
# dag = DAG(
#     'etl_workflow',
#     default_args=default_args,
#     description='Un workflow ETL pour extraire, préparer et entraîner un modèle',
#     schedule_interval=None,  # Aucune planification, vous pouvez exécuter manuellement
# )

# # Définir les tâches
# task_extract_save = PythonOperator(
#     task_id='extract_save',
#     python_callable=extract_save,
#     dag=dag,
# )

# task_prepare_save = PythonOperator(
#     task_id='prepare_save',
#     python_callable=prepare_save,
#     dag=dag,
# )

# task_train_model = PythonOperator(
#     task_id='train_model',
#     python_callable=train_model,
#     dag=dag,
# )

# # Définir l'ordre d'exécution des tâches
# task_extract_save >> task_prepare_save >> task_train_model
