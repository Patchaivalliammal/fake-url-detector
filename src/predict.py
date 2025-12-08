# src/predict.py
import joblib
import numpy as np
import os
from features import extract_features

class UrlDetector:
    def __init__(self):
        # Absolute path to project root and model
        ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        MODEL_PATH = os.path.join(ROOT_DIR, "models", "url_model.joblib")

        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found at: {MODEL_PATH}")

        self.model = joblib.load(MODEL_PATH)
        # feature names must match src/features.extract_features keys
        self.feat_order = ['url_len', 'host_len', 'dots', 'digits']

    def predict(self, url):
        feats = extract_features(url)
        X = np.array([feats[f] for f in self.feat_order]).reshape(1, -1)
        prob = float(self.model.predict_proba(X)[0][1])
        label = "malicious" if prob > 0.5 else "legitimate"
        return {"url": url, "label": label, "score": prob, "features": feats}
