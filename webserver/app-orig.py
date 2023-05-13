from flask import Flask, render_template, request
import requests
import json

GATEWAY_URL = "http://localhost:5001"
app = Flask(__name__, template_folder='C:/Users/dell/Desktop/ms-project-1/templates', static_folder='static')
app.debug = True

@app.route('/')
def index():
    response = requests.get('http://localhost:5002/users')
    users = json.loads(response.text)
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    data = {'name': name, 'email': email}

    # make a request to the User microservice to add the data
    response = requests.post(f"{GATEWAY_URL}/users", json=data)

    # check if the request was successful
    if response.status_code == 200:
        print(response.status_code)
        print(response.text)
        return redirect('/')
    else:
        # handle the error
        return "Error: failed to add user"

@app.route('/delete', methods=['POST'])
def delete():
    email = request.form['email']
    requests.delete('http://localhost:5002/users/' + email)
    return 'success'

if __name__ == '__main__':
    app.run(debug=True, port=5000)