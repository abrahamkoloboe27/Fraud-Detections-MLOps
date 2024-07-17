import pandas as pd
from sklearn.externals import joblib
from models.utils import preprocess_data

# Charger le modèle pré-entraîné
model = joblib.load('model.pkl')

def predict(data):
    # Prétraiter les données
    processed_data = preprocess_data(data)
    # Faire la prédiction
    prediction = model.predict(processed_data)
    return prediction.tolist()
