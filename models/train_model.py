import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.externals import joblib

# Charger les données
data = pd.read_csv('data/creditcard.csv')

# Séparer les features et la cible
X = data.drop('Class', axis=1)
y = data['Class']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiser le modèle
model = RandomForestClassifier()

# Entraîner le modèle
model.fit(X_train, y_train)

# Évaluer le modèle
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Sauvegarder le modèle
joblib.dump(model, 'model.pkl')
