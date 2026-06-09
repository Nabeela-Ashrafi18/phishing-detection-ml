import joblib
from feature_extraction import extract_features

model = joblib.load("phishing_model.pkl")

url = "https://www.google.com"

features = [extract_features(url)]

print("Features:", features)
print("Prediction:", model.predict(features))
print("Probability:", model.predict_proba(features))