from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length=12, use_digits=True, use_specials=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/generate-password', methods=['POST'])
def password_api():
    data = request.json
    length = int(data.get('length', 12))
    use_digits = data.get('useDigits', True)
    use_specials = data.get('useSpecials', True)

    password = generate_password(length, use_digits, use_specials)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
