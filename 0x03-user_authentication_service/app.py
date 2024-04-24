#!/usr/bin/env python3
"""Basic Flask app
"""

from flask import Flask, abort, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


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
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Login
    """
    email = request.form.get('email')
    password = request.form.get('password')
    valid = AUTH.valid_login(email, password)
    if not valid:
        abort(401)
    session_id = AUTH.create_session(email)
    if not session_id:
        abort(401)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
