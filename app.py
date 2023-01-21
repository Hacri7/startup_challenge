from flask import Flask, jsonify, request
import re

app = Flask(__name__)

todos = ['complete the witcher', 'complete the finals']
users = []

@app.route('/todos', methods=['GET'])
def get_all_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    task = request.json['task']
    todos.append(task)
    return jsonify({'task': task}), 201

@app.route('/todos/<int:index>', methods=['GET'])
def get_todo(index):
    if index < 0 or index >= len(todos):
        return jsonify({'error': 'Invalid index'}), 400
    return jsonify({'task': todos[index]})

@app.route('/todos/<int:index>', methods=['PUT'])
def update_todo(index):
    if index < 0 or index >= len(todos):
        return jsonify({'error': 'Invalid index'}), 400
    todos[index] = request.json['task']
    return jsonify({'task': todos[index]})

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    if index < 0 or index >= len(todos):
        return jsonify({'error': 'Invalid index'}), 400
    del todos[index]
    return jsonify({'message': 'Task deleted'})





#REGISTER AND LOGIN 
@app.route('/register', methods=['POST'])
def register():
    user = request.json
    # validating email and password
    if not re.match(r"[^@]+@[^@]+\.[^@]+", user.get('email','')):
        return jsonify({'message': 'Invalid email address'}), 400
    if len(user.get('password','')) < 8:
        return jsonify({'message': 'Password should be at least 8 characters long'}), 400
    # adding the user to the list
    users.append(user)
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    user = request.json
    email = user.get('email')
    password = user.get('password')
    # checking if the user exists
    for u in users:
        if u.get('email') == email and u.get('password') == password:
            return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid email or password'}), 401


if __name__ == '__main__':
    app.run(debug=True)
