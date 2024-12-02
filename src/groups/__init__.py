"""
Author: nagendran.s

Groups Submodule Initialization

This submodule profides function for group related operations. The `__init__.py`
file imports key functions to expose them as part of the package's public API.

Exposed API:
- get_groups_for_user: Retrieve Groups for a specific user from AWS Identity Center.

Modules:
- group_user: Handles retrieval of Groups for specific user 

Usage:
Import specific function or modules as needed:
    from src.groups import group_user
"""

# src/groups/__init__.py
# Import specific function
from .group_user import get_groups_for_user

# Specifying explicity Public API that should be exposed
__all__ = ["get_groups_for_user"]
print("Initializing groups package...")