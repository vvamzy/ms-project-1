from flask import Flask, jsonify, request
import json

app = Flask(__name__)

users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    payload = request.get_json()
    users.append(payload)
    return 'success'

@app.route('/users/<email>', methods=['DELETE'])
def delete_user(email):
    for user in users:
        if user['email'] == email:
            users.remove(user)
            return 'success'
    return 'user not found'

if __name__ == '__main__':
    app.run(debug=True, port=5002)