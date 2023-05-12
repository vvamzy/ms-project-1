from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    response = requests.get('http://localhost:5002/users')
    users = response.json()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    payload = request.get_json()
    response = requests.post('http://localhost:5002/users', json=payload)
    return response.text

@app.route('/users/<email>', methods=['DELETE'])
def delete_user(email):
    response = requests.delete('http://localhost:5002/users/' + email)
    return response.text

if __name__ == '__main__':
    app.run(debug=True, port=5001)