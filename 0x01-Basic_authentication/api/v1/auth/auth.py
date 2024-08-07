#!/usr/bin/env python3
''' authentication cls '''
from flask import request
from typing import List, TypeVar


class Auth():
    ''' controls authentication of API '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' this function requires paths and excluded paths '''
        return False
    
    def authorization_header(self, request=None) -> str:
        ''' returns none '''
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        ''' return none '''
        return None
