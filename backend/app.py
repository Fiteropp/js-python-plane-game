from flask import Flask, jsonify

# We will probably use gunicorn library on deployment!
app = Flask(__name__, static_folder="../frontend", static_url_path="")

@app.get("/")
def index():
    return app.send_static_file("index.html")

#health check endpoint, can be pinged to check if the backend is online
@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})
