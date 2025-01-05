from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS

# Initialize the Flask app and enable CORS
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database path
DB_PATH = "database.db"


# Initialize the database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS counters (
        id INTEGER PRIMARY KEY,
        value INTEGER
    )
    """)

    # Check if the row with ID 1 exists; if not, insert it
    cursor.execute("SELECT id FROM counters WHERE id = 1")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO counters (id, value) VALUES (1, 0)")

    conn.commit()
    conn.close()


# Route: Get current counter value
@app.route("/counter", methods=["GET"])
def get_counter():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM counters WHERE id = 1")
    row = cursor.fetchone()
    conn.close()

    # Respond with the counter value or 0 if no data is found
    return jsonify({"counter": row[0] if row else 0})


# Route: Increment counter
@app.route("/increment", methods=["POST"])
def increment_counter():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE counters SET value = value + 1 WHERE id = 1")
    conn.commit()

    # Fetch the updated value
    cursor.execute("SELECT value FROM counters WHERE id = 1")
    row = cursor.fetchone()
    conn.close()

    # Respond with the updated counter value
    return jsonify({"counter": row[0]})


# Run the server
if __name__ == "__main__":
    # Initialize the database on startup
    init_db()
    app.run(host="0.0.0.0", port=3000)

# The host="0.0.0.0" parameter allows the server to be accessible
# from any network interface, not just localhost.


# Best Practices for Python Projects
# 1. Virtual Environment: Always create and use a virtual environment
#    to isolate project dependencies.

# python -m venv venv
# source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate     # Windows

# 2. pip install: Use pip install to install dependencies.

# 3. Requirements File: List all dependencies in a requirements.txt file. Use:

# pip freeze > requirements.txt

# 4. Directory Structure: Keep the project organized:

# python_backend/
# ├── venv/              # Virtual environment
# ├── database.db        # SQLite database
# ├── requirements.txt   # Project dependencies
# ├── server.py          # Flask server code

# 5. Run the Project:

# Activate the virtual environment.
# Install dependencies: pip install -r requirements.txt.
# Run the backend: python server.py
