#!/usr/bin/env python3
"""
Module for the Authentication.
"""
import base64
from typing import Tuple
from api.v1.auth.auth import Auth


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
