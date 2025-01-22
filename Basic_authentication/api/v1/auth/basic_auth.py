#!/usr/bin/env python3
"""
Module for the Authentication.
"""
import base64
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Class for managing Basic API authentication."""

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Extracts the base64 part of the Authorization header.

        Args:
            authorization_header (str): The Authorization header to extract.

        Returns:
            str: The Base64 part of the header, or None if invalid.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes a base64 string.

        Args:
            base64_authorization_header (str): The base64 string to decode.

        Returns:
            str: The decoded string, or None if invalid.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """
        Extracts the user email and password from the Base64 decoded value.

        Args:
            decoded_base64_authorization_header (str).

        Returns:
            Tuple[str, str]: The user email and password.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """
        Returns the User instance based on their email and password.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            User: The User instance if found and valid, or None otherwise.
        """
        # Validate email and password
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        # Perform a search for users with the given email
        try:
            users = User.search({'email': user_email})
        except Exception as e:
            # Handle unexpected issues in User.search()
            return None

        # Handle cases where no users are found
        if not users:  # Covers None and empty list
            return None

        # Validate password for each user found
        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        # No valid user found
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        header = self.authorization_header(request)
        if header is None:
            return None
        b64 = self.extract_base64_authorization_header(header)
        if b64 is None:
            return None
        decoded = self.decode_base64_authorization_header(
            b64)
        if decoded is None:
            return None
        user_info = self.extract_user_credentials(
            decoded)
        if user_info is None:
            return None
        email, pwd = user_info
        user = self.user_object_from_credentials(email, pwd)
        return user
