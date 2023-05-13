from flask import Flask, render_template, request, redirect
import requests
from flask import jsonify
import json

app = Flask(__name__, template_folder='C:/Users/dell/Desktop/ms-project-1/templates', static_folder='static')
app.debug = True

users = []
GATEWAY_URL = "http://localhost:5001"

@app.route('/')
def index():
    response = requests.get(f"{GATEWAY_URL}/users")
    users = json.loads(response.text)
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(users)
@app.route('/fetch', methods=['GET'])
def fetch():
    response = requests.get(f"{GATEWAY_URL}/users")
    users = json.loads(response.text)
    return render_template('fetch.html', users=users)

@app.route('/delete', methods=['POST'])
def delete():
    email = request.form['email']
    response = requests.delete(f"{GATEWAY_URL}/users/{email}")
    print("Delete user response status code:", response.status_code)

    # check if the request was successful
    if response.status_code == 204:
        print("User deleted successfully")
        return redirect('/')
    else:
        # handle the error
        print("Failed to delete user")
        return "Error: failed to delete user"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
