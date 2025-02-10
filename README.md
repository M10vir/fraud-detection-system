# fraud-detection-system
A machine learning-based fraud detection system built using Azure Machine Learning, DeepSeek-R1 and deployed on Azure Kubernetes Service (AKS).

# Fraud Detection System using Azure Machine Learning

## Overview
This project aims to detect fraudulent transactions in real-time using machine learning. The system is built using Azure Machine Learning and deployed on Azure Kubernetes Service (AKS).

## Features
- Real-time fraud detection using a deployed API.
- Scalable deployment on Azure Kubernetes Service (AKS).
- Integrated with Application Insights for monitoring and alerting.
- Optimized models using HyperDrive for hyperparameter tuning.

## Dataset
The dataset used in this project is the [Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud) from Kaggle.

## Methodology
1. Data Preprocessing: Handled missing values, normalized features, and split the data into training and testing sets.
2. Model Development: Trained Logistic Regression, XGBoost, and LightGBM models. Optimized hyperparameters using HyperDrive.
3. Deployment: Deployed the best-performing model (LightGBM) to AKS. Enabled Application Insights for monitoring.
4. Monitoring and Optimization: Tracked API performance, scaled the AKS cluster, and retrained the model.

## Results
- Logistic Regression: AUC = 0.96, F1-Score = 0.81.
- XGBoost: AUC = 0.98, F1-Score = 0.88.
- LightGBM: AUC = 0.98, F1-Score = 0.88.
- API deployed at: `http://48.217.133.143:80/api/v1/service/fraud-detection-api/score`.

## How to Use
1. Clone the repository:
   
   git clone https://github.com/M10vir/fraud-detection-system.git
   cd fraud-detection-system
