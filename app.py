from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "TraderKit Clone Running 🚀"

@app.route("/signal", methods=["GET"])
def signal():
    return jsonify({
        "signal": random.choice(["BUY", "SELL"]),
        "confidence": random.randint(70, 95)
    })

if __name__ == "__main__":
    app.run()
