from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# A temporary dictionary simulating a system database to save new users
# Key: username (Registration Number), Value: password
USER_DATABASE = {
    "admin": "cutm123"  # Default fallback login account
}

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return "<h1>Registration failed. Fields cannot be empty.</h1>", 400
        
    if username in USER_DATABASE:
        return "<h1>Registration Failed: ID already exists!</h1><br><a href='http://127.0.0'>Try again</a>", 400
    
    # Save the new ID and password into our system database map
    USER_DATABASE[username] = password
    print(f"[SYSTEM DB UPDATE]: New student registered! ID: {username}")
    
    return """
    <h1>Account Created Successfully!</h1>
    <p>Your login details have been securely saved in the system.</p>
    <a href="http://127.0.0">Click here to Login</a>
    """

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Checks if the entry matches the credentials inside our user database map
    if username in USER_DATABASE and USER_DATABASE[username] == password:
        return f"<h1>Login Successful! Welcome to the CUTM Library Portal Dashboard, student {username}.</h1>"
    else:
        return "<h1>Invalid Credentials. Please check your Registration ID or Password.</h1><br><a href='http://127.0.0'>Go Back</a>", 401

if __name__ == '__main__':
    print("Python Library System Backend Server Running on http://127.0.0.1:5000")
    app.run(port=5000, debug=True)
