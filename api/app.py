from flask import Flask, request, jsonify
from flask_cors import CORS
from src.predict import predict_url
import datetime
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# ======================
# API Endpoints
# ======================
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get("url", "").strip()

    if not url:
        return jsonify({
            "error": "Invalid URL",
            "details": "Please enter a valid URL starting with http:// or https://"
        }), 400

    try:
        prediction, confidence = predict_url(url)

        return jsonify({
            "url": url,
            "prediction": prediction,
            "confidence": confidence,
            "is_phishing": prediction.lower() == "phishing",
            "timestamp": datetime.datetime.now().isoformat(),
            "details": get_phishing_details(prediction),
            "status_code": 200
        })

    except Exception as e:
        return jsonify({
            "error": "Analysis failed",
            "details": str(e),
            "url": url,
            "status_code": 500
        }), 500

# ======================
# Helper Functions
# ======================
def get_phishing_details(prediction):
    """Generate human-readable details based on prediction."""
    details = {
        "Phishing": "This site exhibits characteristics of a phishing scam.",
        "Legitimate": "No phishing indicators detected.",
    }
    return details.get(prediction.lower(), "Analysis complete.")

# ======================
# Security & Production Setup
# ======================
if __name__ == "__main__":
    if os.environ.get('FLASK_ENV') == 'production':
        from gevent.pywsgi import WSGIServer
        http_server = WSGIServer(('0.0.0.0', 5000), app)
        http_server.serve_forever()
    else:
        app.run(host='0.0.0.0', port=5000, debug=True)