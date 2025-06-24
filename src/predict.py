import joblib
import pandas as pd
from src.feature_engineering import extract_features

model = joblib.load('models/phishing_model.pkl')

def predict_url(url: str, threshold: float = 0.5):
    features = pd.Series(extract_features(url)).to_frame().T
    proba = model.predict_proba(features)[0]

    # Fix: Map probabilities to their actual class labels
    class_prob = dict(zip(model.classes_, proba))
    phishing_prob = class_prob.get(1, 0)  # Class 0 = Phishing
    legit_prob = class_prob.get(0, 0) # Class 1 = Legit
    print(phishing_prob, legit_prob)

    if phishing_prob > threshold:
        prediction = "Phishing"
        confidence = round(phishing_prob, 2)
    else:
        prediction = "Legitimate"
        confidence = round(legit_prob, 2)

    print(prediction, confidence)
    return prediction, confidence
