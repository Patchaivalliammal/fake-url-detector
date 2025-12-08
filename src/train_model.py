# src/train_model.py
import os
import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression

# Simple synthetic training data (keeps everything self-contained)
X = np.array([
    [10, 5, 1, 0],     # benign-like
    [50, 20, 3, 5],    # malicious-like
    [100, 50, 5, 10]   # malicious-like
])
y = np.array([0, 1, 1])

model = LogisticRegression()
model.fit(X, y)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/url_model.joblib")
print("Model trained and saved → models/url_model.joblib")
