#!/usr/bin/env python3
"""
Module for the Authentication
"""
from flask import request
from typing import List

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method that should return True if the path is not in the list of
            strings excluded_paths
        """
        return False, path, excluded_paths
    
    def authorization_header(self, request=None) -> str:
        """ Method that should return None - request or the value of the header
        """
        return None, request
    
    def current_user(self, request=None) -> TypeVar('User'):
        """ Method that should return None - request or the user instance
        """
        return None, request
