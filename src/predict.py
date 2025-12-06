import joblib
import numpy as np
from features import extract_features

class UrlDetector:
    def __init__(self):
        self.model = joblib.load("../models/url_model.joblib")
        self.feat_order = ['url_len','host_len','dots','digits']

    def predict(self, url):
        feats = extract_features(url)
        X = np.array([feats[f] for f in self.feat_order]).reshape(1,-1)
        prob = self.model.predict_proba(X)[0][1]
        label = "malicious" if prob > 0.5 else "legitimate"
        return {"url": url, "label": label, "score": float(prob), "features": feats}
