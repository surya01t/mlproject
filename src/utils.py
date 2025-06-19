import os 
import sys

import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    """
    Saves the object to a file using pandas serialization.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)            

    except Exception as e:
        raise CustomException(e, sys)
    



def evaluate_models(X_train, y_train, X_test, y_test, models: dict):
    try:
        report = {}

        for name, model in models.items():
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            score = r2_score(y_test, preds)

            # Don't print here — just store
            report[name] = score

        return report
    except Exception as e:
        raise CustomException(e, sys)
