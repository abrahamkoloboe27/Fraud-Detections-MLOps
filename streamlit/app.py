import streamlit as st
import requests

# Définir l'URL de votre API Flask déployée
API_URL = 'http://localhost:5000/predict'  # Modifier l'URL si nécessaire

st.title('Détection de Fraudes Financières')

# Widgets pour saisir les données d'entrée
amount = st.number_input('Montant de la transaction')
time = st.number_input('Temps depuis la dernière transaction')
# Ajouter d'autres widgets pour les autres caractéristiques pertinentes

if st.button('Prédire'):
    data = {
        'Amount': amount,
        'Time': time,
        # Ajouter d'autres caractéristiques ici
    }

    # Envoyer une requête POST à l'API Flask
    response = requests.post(API_URL, json=data)

    if response.status_code == 200:
        result = response.json()
        st.write(f"Prédiction : {result['prediction']}")
    else:
        st.write("Erreur lors de la prédiction. Veuillez réessayer.")
