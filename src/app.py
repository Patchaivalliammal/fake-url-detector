# src/app.py
import os
from flask import Flask, request, render_template, jsonify
from predict import UrlDetector

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPLATES_DIR = os.path.join(ROOT_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATES_DIR)
detector = UrlDetector()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json() or request.form
    url = data.get("url", "")
    if not url:
        return jsonify({"error":"no url provided"}), 400
    result = detector.predict(url)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

