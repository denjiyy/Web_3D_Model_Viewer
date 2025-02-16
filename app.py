from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

# Folder where 3D models are stored
STATIC_MODELS_PATH = "static"

@app.route("/")
def index():
    return render_template("index.html")  # Your HTML file

@app.route("/models")
def list_models():
    models = [f for f in os.listdir(STATIC_MODELS_PATH) if f.endswith(".glb")]
    return jsonify(models)

if __name__ == "__main__":
    app.run(debug=True)