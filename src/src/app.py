from flask import Flask, request, render_template, jsonify
from predict import UrlDetector

app = Flask(__name__, template_folder='../templates')
detector = UrlDetector()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json() or request.form
    url = data.get("url", "")
    result = detector.predict(url)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
