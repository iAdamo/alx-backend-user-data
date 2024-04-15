#!/usr/bin/env python3
"""Encrypting passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
