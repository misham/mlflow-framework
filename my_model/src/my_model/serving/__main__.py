import os

import logging

from fastapi import FastAPI
import uvicorn

import mlflow
import numpy as np
import pandas as pd
from pydantic import BaseModel

logger = logging.getLogger(__name__)

class Size(BaseModel):
    length: float
    width: float

class PredictRequest(BaseModel):
    sepal: Size
    petal: Size


app = FastAPI()

mlflow.set_tracking_uri('http://mlflow:5000')
flower_name_by_index = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}


@app.post("/predict/{run_id}")
def predict(run_id, request: PredictRequest):

    logger.info("run_id: %s", run_id)
    
    model = mlflow.lightgbm.load_model(f'runs:/{run_id}/model')

    df = pd.DataFrame(columns=['sepal.length', 'sepal.width', 'petal.length', 'petal.width'],
                      data=[[request.sepal.length, request.sepal.width, request.petal.length, request.petal.width]])

    y_pred = np.argmax(model.predict(df))
    return {"flower": flower_name_by_index[y_pred]}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()