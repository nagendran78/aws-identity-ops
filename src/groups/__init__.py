"""
Author: nagendran.s

Groups Submodule Initialization

This submodule profides function for group related operations. The `__init__.py`
file imports key functions to expose them as part of the package's public API.

Exposed API:
- get_groups_for_user: Retrieve Groups for a specific user from AWS Identity Center.
- get_all_groups: Retrieve Groups and Users.EmailID.
- export_groups_to_csv: Export Groups and associated users to CSV file format.

Modules:
- groups: Handles retrieval of all Groups and associated Users 

Usage:
Import specific function or modules as needed:
    from src.groups import group_user
    from src.groups import all_group
    from src.groups import export_groups
"""

# src/groups/__init__.py
# Import specific function
from .group_user import get_groups_for_user
from .all_group import get_all_groups
from .export_groups import export_groups_to_csv

# Specifying explicity Public API that should be exposed
__all__ = ["get_groups_for_user", "get_all_groups", "export_groups_to_csv"]
print("Initializing groups package...")