from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (in-memory database)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# Home route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# Get a user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Update a user by ID
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        data = request.get_json()
        user.update(data)
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Delete a user by ID
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
