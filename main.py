from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np
from pydantic import BaseModel

model = joblib.load('diamond_price_model.pkl')
clarity_enc = joblib.load('label_encoder_clarity.pkl')
cut_enc = joblib.load('label_encoder_cut.pkl')
color_enc = joblib.load('label_encoder_color.pkl')

app = FastAPI()

class DiamondFeatures(BaseModel):
    cut: str
    carat: float
    color: str
    clarity: str
    depth: float
    table: float
    x: float
    y: float
    z: float

@app.post('/predict')
def predict(features: DiamondFeatures):
    # Encode categorical columns
    cut_encoded = cut_enc.transform([features.cut])[0]
    color_encoded = color_enc.transform([features.color])[0]
    clarity_encoded = clarity_enc.transform([features.clarity])[0]

    # Create input dataframe
    input_data = pd.DataFrame([[
        features.carat,
        cut_encoded,
        color_encoded,
        clarity_encoded,
        features.depth,
        features.table,
        features.x,
        features.y,
        features.z
    ]], columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z'])

    # Make prediction
    prediction = model.predict(input_data)[0]

    return {'predicted_price': round(float(prediction), 2)}

