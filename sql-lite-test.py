from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "database.db"


# Create Table if not exist
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """
        )
        conn.commit()


init_db()


# Add new item
@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Missing 'name' field"}), 400

    created_at = datetime.utcnow().isoformat() + "Z"
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO items (name, created_at) VALUES (?, ?)",
            (data["name"], created_at),
        )
        item_id = cursor.lastrowid

    return jsonify({"id": item_id, "name": data["name"], "created_at": created_at}), 201


# Get the items in database
@app.route("/items", methods=["GET"])
def get_items():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, created_at FROM items")
        rows = cursor.fetchall()

    items = [{"id": r[0], "name": r[1], "created_at": r[2]} for r in rows]
    return jsonify({"count": len(items), "data": items}), 200


# Delete all items in the table
@app.route("/reset", methods=["POST"])
def reset_items():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM items")
        conn.commit()
    return jsonify({"status": "reset done"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
