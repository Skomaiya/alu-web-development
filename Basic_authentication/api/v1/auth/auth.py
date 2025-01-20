#!/usr/bin/env python3
"""
Module for the Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class for the Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method that should return True if the path is not in the list of
            strings excluded_paths
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        elif path not in excluded_paths:
            return True
        path = path.rstrip('/')
        normalized_excluded = [p.rstrip('/') for p in excluded_paths]

        if path in normalized_excluded:
            return False

    def authorization_header(self, request=None) -> str:
        """ Method that should return None - request or the value of the header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method that should return None - request or the user instance
        """
        return None
