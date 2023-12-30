from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for simplicity (not suitable for production)
user_credentials = {'user1': {'password': 'password1', 'balance': 100},
                    'user2': {'password': 'password2', 'balance': 50}}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in user_credentials and user_credentials[username]['password'] == password:
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@app.route('/get_balance', methods=['GET'])
def get_balance():
    username = request.args.get('username')

    if username in user_credentials:
        balance = user_credentials[username]['balance']
        return jsonify({'success': True, 'balance': balance})
    else:
        return jsonify({'success': False, 'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
