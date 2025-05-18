from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[!@#$%^&*()_+=\-]", password):
        strength += 1
    return "Strong" if strength >= 4 else "Weak"

def leetify(password):
    leet_map = {'a': '@', 'A': '4', 'e': '3', 'E': '3', 'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '$', 'S': '$'}
    return ''.join(leet_map.get(c, c) for c in password)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Password Strength Checker</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #2c3e50, #3498db);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            margin: 0;
            animation: fadeIn 1.5s ease-in;
        }

        @keyframes fadeIn {
            0% {opacity: 0;}
            100% {opacity: 1;}
        }

        .container {
            background-color: rgba(0, 0, 0, 0.6);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.2);
            text-align: center;
            animation: slideUp 1s ease-out;
        }

        @keyframes slideUp {
            from {transform: translateY(20px); opacity: 0;}
            to {transform: translateY(0); opacity: 1;}
        }

        input[type="text"] {
            padding: 10px;
            width: 80%;
            border: none;
            border-radius: 5px;
            margin-top: 10px;
        }

        input[type="submit"] {
            margin-top: 15px;
            padding: 10px 20px;
            background-color: #1abc9c;
            border: none;
            border-radius: 5px;
            color: white;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        input[type="submit"]:hover {
            background-color: #16a085;
        }

        .result {
            margin-top: 20px;
            font-size: 18px;
        }

        .suggestion {
            margin-top: 10px;
            font-style: italic;
            color: #f1c40f;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Password Strength Checker</h1>
        <form method="POST">
            <input type="text" name="password" placeholder="Enter password..." required>
            <br>
            <input type="submit" value="Check">
        </form>
        {% if result %}
            <div class="result">{{ result }}</div>
        {% endif %}
        {% if suggestion %}
            <div class="suggestion">{{ suggestion }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    suggestion = ''
    if request.method == 'POST':
        password = request.form['password']
        strength = check_password_strength(password)
        result = f'Password Strength: {strength}'
        if strength == "Weak":
            suggestion = f'Strong Suggestion: {leetify(password)}123!'
    return render_template_string(html_template, result=result, suggestion=suggestion)

if __name__ == '__main__':
    app.run(debug=True)
