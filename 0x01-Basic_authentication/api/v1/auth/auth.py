#!/usr/bin/env python3
""" authentication cls """
from flask import request
from typing import List, TypeVar


class Auth:
    """ controls authentication of API """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ this function requires paths and excluded paths """
        if not path:
            return True
        if not excluded_paths or excluded_paths == []:
            return True
        if not path.endswith("/"):
            path += "/"
        if path in excluded_paths:
            return False
        for paths in excluded_paths:
            paths = paths.rstrip("*")
            if path.find(paths) != -1:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ returns none """
        if request:
            return request.headers.get("Authorization", None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Gets the current user and return none"""
        return None
