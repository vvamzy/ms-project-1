from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://localhost:5002/users')
    users = json.loads(response.text)
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    payload = {'name': name, 'email': email}
    requests.post('http://localhost:5002/users', json=payload)
    return 'success'

@app.route('/delete', methods=['POST'])
def delete():
    email = request.form['email']
    requests.delete('http://localhost:5002/users/' + email)
    return 'success'

if __name__ == '__main__':
    app.run(debug=True, port=5000)