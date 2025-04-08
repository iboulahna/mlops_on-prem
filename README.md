
# MLOps On-Prem End-to-End Project

This project demonstrates an end-to-end MLOps pipeline for machine learning deployment, executed entirely on-premises. The goal is to build, manage, and deploy machine learning models using MLOps practices, integrating data processing, model training, and orchestration into a robust workflow.

## Project Structure

```
MLOPS_ON_PREM
├── dags                    # Airflow DAGs for orchestrating workflows
│   └── etl_workflow.py      # ETL workflow for data processing
├── data                    # Raw and cleaned datasets
│   ├── cleaned_data.csv     # Cleaned data ready for modeling
│   └── raw_data.csv         # Raw input data
├── models                  # Trained models saved for deployment
│   └── logistic_model.pkl   # Logistic regression model
├── notebooks               # Jupyter Notebooks for exploratory analysis
│   └── feature_eng.ipynb    # Notebook for feature engineering
├── venv                    # Virtual environment for isolating dependencies
├── .gitignore              # Git ignore file to exclude unnecessary files
├── .pre-commit-config.yaml # Configuration for pre-commit hooks
├── README.md               # Project overview and documentation
└── requirements.txt        # List of required dependencies
```

## Project Components

1. **Airflow DAG (`etl_workflow.py`)**  
   - The core orchestration tool of this project, used to manage the ETL (Extract, Transform, Load) pipeline.
   - It runs various tasks such as data cleaning, feature engineering, and model training.

2. **Data**  
   - `raw_data.csv`: The raw dataset used for analysis and model training.
   - `cleaned_data.csv`: The preprocessed and cleaned dataset ready for feature engineering and modeling.

3. **Model**  
   - `logistic_model.pkl`: The trained logistic regression model saved using `pickle`.

4. **Notebooks**  
   - `feature_eng.ipynb`: A Jupyter notebook used for exploratory data analysis (EDA) and feature engineering. It contains code for preparing the data before feeding it into the model.

5. **Virtual Environment (`venv`)**  
   - This directory contains the isolated environment for this project. It includes all necessary libraries for running the ETL, model training, and feature engineering tasks.

## Setup Instructions

To set up this project on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd MLOPS_ON_PREM
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scriptsctivate
     ```
   - On Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up Apache Airflow (if not already installed):
   ```bash
   pip install apache-airflow
   ```

6. Run the Airflow web server and scheduler:
   ```bash
   airflow webserver -p 8080
   airflow scheduler
   ```

## Running the ETL Pipeline

- The ETL workflow is defined in `etl_workflow.py`. It can be triggered manually from the Airflow UI or scheduled for automated execution.

## Model Training

- The model training is part of the ETL pipeline. Once the cleaned data is available, the logistic regression model is trained and saved as `logistic_model.pkl`.

## Batch Processing Workflow (Synthetic Data Generation)

To trigger the `batch_processing_workflow` DAG, which generates and saves synthetic data, follow these steps:

### 1. Trigger the DAG

You can manually trigger the `batch_processing_workflow` using the following command:

```bash
airflow dags trigger batch_processing_workflow
```

## Notes

- This project is currently in its first version. Future enhancements will include model deployment, monitoring, and more sophisticated pipeline automation.
- The project is designed to run entirely on-premises with no cloud dependencies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

