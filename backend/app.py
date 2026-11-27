import os

import pymysql
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()

app = Flask(__name__, static_folder="../frontend", static_url_path="")

def get_db():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER", "dev"),
        password=os.getenv("DB_PASSWORD", "devpassword"),
        database=os.getenv("DB_NAME", "myapp"),
        cursorclass=pymysql.cursors.DictCursor,
    )

@app.get("/")
def index():
    return app.send_static_file("index.html")

@app.get("/api/health")
def health():
    try:
        conn = get_db()
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
        conn.close()
        return jsonify({"status": "ok", "database": "connected"})
    except Exception as e:
        return jsonify({"status": "error", "detail": str(e)}), 503

if __name__ == "__main__":
    # host="0.0.0.0" is required so Flask is reachable outside the Docker container
    app.run(host="0.0.0.0", port=5000, debug=True)
