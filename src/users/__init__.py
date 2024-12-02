"""
Author: nagendran.s

Users Submodule Initialization

This submodule profides function for Users related operations. The `__init__.py`
file imports key functions to expose them as part of the package's public API.

Exposed API:
- list_users: Retrieve the list of users from AWS Identity Center.
- export_users_to_csv: Export list of users to CSV file format.

Modules:
- users: Handles retrieval of all Users

Usage:
Import specific function or modules as needed:
    from src.users import users
    from src.users import export_users
"""

# src/users/__init__.py
# Import specific function
from .users import list_users
from .export_users import export_users_to_csv

# Specifying explicity Public API that should be exposed
__all__ = ["list_users", "export_users_to_csv"]
print("Initializing users package...")