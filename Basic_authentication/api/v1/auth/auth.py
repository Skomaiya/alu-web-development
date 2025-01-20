#!/usr/bin/env python3
"""
Module for the Authentication
"""
from flask import request
from typing import List

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False, path, excluded_paths
    
    def authorization_header(self, request=None) -> str:
        return None, request
    
    def current_user(self, request=None) -> TypeVar('User'):
        return None, request