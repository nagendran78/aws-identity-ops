"""
Author: nagendran.s

Groups Submodule Initialization

This submodule profides function for group related operations

Exposed API:
- get_groups_for_user: Retrieve Groups for a specific user from AWS Identity Center.

Modules:
- group_user: Handles retrieval of Groups for specific user 
"""

# library/groups/__init__.py
# Import specific function
from .group_user import get_groups_for_user

# Specifying explicity Public API that should be exposed
__all__ = ["get_groups_for_user"] 