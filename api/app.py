from flask import Flask, jsonify, request
from sklearn.externals import joblib
from models.utils import preprocess_data

app = Flask(__name__)

# Charger le modèle pré-entraîné
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Prétraiter les données
    processed_data = preprocess_data(data)
    # Faire la prédiction
    prediction = model.predict(processed_data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
