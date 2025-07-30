from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

items = []


# Helper function to create a formatted item
def create_item(name):
    return {
        "id": len(items) + 1,
        "name": name,
        "created_at": datetime.utcnow().isoformat() + "Z",
    }


# Get the items in the memory
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({"status": "success", "count": len(items), "data": items}), 200


# Add new item
@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"status": "error", "message": "Missing 'name' field"}), 400

    item = create_item(data["name"])
    items.append(item)
    return jsonify({"status": "success", "data": item}), 201


# Run Api localy on port 5000
# Use host="0.0.0.0" to make the app accessible from outside the container (run localy with docker or without , with no proplems)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
