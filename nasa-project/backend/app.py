from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import requests
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/apod")
def apod():
    """Astronomy Picture of the Day"""
    try:
        params = {"api_key": NASA_API_KEY}
        response = requests.get(NASA_APOD_URL, params=params, timeout=5)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
