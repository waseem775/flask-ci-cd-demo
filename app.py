from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("POSTGRES_HOST", "localhost"),
            database=os.environ.get("POSTGRES_DB", "testdb"),
            user=os.environ.get("POSTGRES_USER", "testuser"),
            password=os.environ.get("POSTGRES_PASSWORD", "testpass"),
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Connected to PostgreSQL: {db_version}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

