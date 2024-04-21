#!/usr/bin/env python3
"""Module of Session Authentication
"""

import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session Authentication Class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = user_id
        return session_id
