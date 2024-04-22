#!/usr/bin/env python3
"""Routes for the Session Authentication
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.user import User
from api.v1.auth.session_auth import SessionAuth
from os import getenv

AUTH = SessionAuth()


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /auth_session/login
    Return:
      - User object JSON represented
    """
    email = request.form.get('email')
    if email is None:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if password is None:
        return jsonify({"error": "password missing"}), 400
    user = User()
    users = user.search({'email': email})
    if users == []:
        return jsonify({"error": "no user found for this email"}), 404
    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    session_id = AUTH.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)
    return response
