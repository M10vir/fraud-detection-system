import argparse
import lightgbm as lgb
import os
import joblib
from sklearn.metrics import roc_auc_score
from azureml.core import Run
import pandas as pd

# Parse hyperparameters
parser = argparse.ArgumentParser()
parser.add_argument("--learning_rate", type=float, default=0.1)
parser.add_argument("--num_leaves", type=int, default=31)
parser.add_argument("--max_depth", type=int, default=-1)
parser.add_argument("--min_child_samples", type=int, default=20)
parser.add_argument("--reg_alpha", type=float, default=0.0)
parser.add_argument("--reg_lambda", type=float, default=0.0)
args = parser.parse_args()

# Load the data
X_train = pd.read_csv("X_train.csv")
X_test = pd.read_csv("X_test.csv")
y_train = pd.read_csv("y_train.csv")
y_test = pd.read_csv("y_test.csv")

# Ensure y_train and y_test are 1D arrays
y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

# Initialize the LightGBM model
model = lgb.LGBMClassifier(
    learning_rate=args.learning_rate,
    num_leaves=args.num_leaves,
    max_depth=args.max_depth,
    min_child_samples=args.min_child_samples,
    reg_alpha=args.reg_alpha,
    reg_lambda=args.reg_lambda,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred_proba = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_pred_proba)

# Log metrics
run = Run.get_context()
run.log("AUC", auc)

# Save the model to the outputs directory
os.makedirs("outputs", exist_ok=True)
model_path = os.path.join("outputs", "model.pkl")
joblib.dump(model, model_path)

# Log the model path
run = Run.get_context()
run.upload_file("outputs/model.pkl", model_path)
print("Model saved to:", model_path)