#!/usr/bin/env python3
"""Module to Manage the API Authentication
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to require the authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Method to get the authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method to get the current user
        """
        return None
