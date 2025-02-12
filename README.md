# fraud-detection-system:
A machine learning-based fraud detection system built using Azure Machine Learning, DeepSeek-R1 integration and deployed on Azure Kubernetes Service (AKS).

# Fraud Detection System using Azure Machine Learning

# Overview:
This project aims to detect fraudulent transactions in real-time using machine learning. The system is built using Azure Machine Learning, DeepSeek-R1 integration and deployed on Azure Kubernetes Service (AKS).This project integrates DeepSeek-R1 to provide context-aware insights for fraud detection. Insights are stored in Azure Cosmos DB for further analysis.

# Features:
-  Real-time fraud detection using a deployed API.
-  Scalable deployment on Azure Kubernetes Service (AKS).
-  Integrated with Application Insights for monitoring and alerting.
-  Optimized models using HyperDrive for hyperparameter tuning.
-  DeepSeek-R1 integration using Codes.

# Dataset:
The dataset used in this project is the [Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud) from Kaggle.

# Methodology:
1. Data Preprocessing: Handled missing values, normalized features, and split the data into training and testing sets.
2. Model Development: Trained Logistic Regression, XGBoost, and LightGBM models. Optimized hyperparameters using HyperDrive.
3. Deployment: Deployed the best-performing model (LightGBM) to AKS. Enabled Application Insights for monitoring.
4. Monitoring and Optimization: Tracked API performance, scaled the AKS cluster, and retrained the model.

# DeepSeek-R1 Integration Code using for Insights Codes:
-  deepseek_insights.py      # Generates insights using DeepSeek-R1.
-  cosmos_db.py              # Saves insights to Azure Cosmos DB.

# Usage - Install the DeepSeek-R1 library:
-  pip install deepseek-r1

# Install the required dependencies:
-  pip install -r requirements.txt

# Results:
-  Logistic Regression: AUC = 0.96, F1-Score = 0.81.
-  XGBoost: AUC = 0.98, F1-Score = 0.88.
-  LightGBM: AUC = 0.98, F1-Score = 0.88.
-  API deployed at: `http://48.217.133.143:80/api/v1/service/fraud-detection-api/score`.

# How to Use: Clone the repository:
-  git clone https://github.com/M10vir/fraud-detection-system.git
-  cd fraud-detection-system

   ```plaintext
   # Project File Structure

   \```
   fraud-detection-system/
   ├── data/
   │   └── creditcard.csv # Dataset Download CSV file - https://www.kaggle.com/mlg-ulb/creditcardfraud
   ├── notebooks/
   │   ├── data_preprocessing.ipynb
   │   ├── optimize_model.ipynb
   │   ├── deployment_model.ipynb
   │   ├── createaComputeTarget.ipynb
   │   ├── createComputeCluster.ipynb
   │   ├── hyperparameter_Tuning.ipynb
   │   ├── monitoring_scaling_improving_model.ipynb
   │   └── monitoringandOptimization.ipynb
   ├── deepseek_integration/
   │   ├── deepseek_insights.py
   │   └── cosmos_db.py
   ├── scripts/
   │   ├── score.py # Scoring script
   │   └── deploy.py # Deployment script
   ├── models/
   │   ├── LogisticRegression_model.ipynb # LogisticRegression model
   │   ├── LightGBM_model.ipynb # LightGBM model
   │   └── XGBoost_model.ipynb # XGBoost model
   ├── requirements.txt # Dependencies
   ├── README.md # Project documentation
   └── LICENSE # Open project
   \```


# Model Comparison

Here’s a comparison of the models based on performance:

Model	              AUC	  F1-Score	Training Time	Use Case
Logistic Regression	0.96	0.81	    Fast	Baseline for simple datasets
XGBoost	            0.98	0.88	    Moderate	High-performance classification
LightGBM	          0.98	0.88	    Fast	Large-scale classification

#MachineLearning #Azure #FraudDetection #DataScience #AI #CloudComputing #DeepSeekR1
