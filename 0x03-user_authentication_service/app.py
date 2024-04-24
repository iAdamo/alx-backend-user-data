#!/usr/bin/env python3
"""Basic Flask app
"""

from flask import Flask, abort, jsonify, request
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route('/')
def basic_app() -> str:
    """Basic app
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """User registration
    """
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
