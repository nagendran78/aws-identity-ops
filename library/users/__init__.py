"""
Author: nagendran.s

Users Submodule Initialization

This submodule profides function for group related operations. The `__init__.py`
file imports key functions to expose them as part of the package's public API.

Exposed API:
- list_users: Retrieve the list of users from AWS Identity Center.

Modules:
- users: Handles retrieval of all Users

Usage:
Import specific function or modules as needed:
    from library.users import users
"""

# library/users/__init__.py
# Import specific function
from .users import list_users

# Specifying explicity Public API that should be exposed
__all__ = ["list_users"] 