import json
import numpy as np
import pandas as pd
import lightgbm as lgb
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path("fraud-detection-model")
    model = lgb.Booster(model_file=model_path)

def run(raw_data):
    data = json.loads(raw_data)["data"]
    input_data = pd.DataFrame(data)
    predictions = model.predict(input_data)
    return json.dumps({"predictions": predictions.tolist()})
