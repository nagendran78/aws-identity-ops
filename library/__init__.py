"""
Author: nagendran.s

Library Package Initialization

This package provides utility functions for managing and exporting user data,
as well as other common utilities. The `__init__.py` file imports key functions
to expose them as part of the package's public API.

Exposed API:
- list_users: Retrieve the list of users from AWS Identity Center.
- clear_screen: Clears the console screen.
- export_users_to_csv: Exports user data to a CSV output file.
- get_groups_for_user: Retrieve Groups based on users from AWS Identity Center. 

Modules:
- users: Contains user-related operations.
- common: Contains utility functions used across the project.
- export_users: Handles exporting user data to various formats.
- groups: Contains Groups related operations.
"""

# library/__init__.py
# Import specific function
from .users import list_users
from .common import clear_screen
from .export_users import export_users_to_csv
from .groups import get_groups_for_user

# Specifying explicity Public API that should be exposed
__all__ = ["list_users", "clear_screen", "export_users_to_csv",
            "get_groups_for_user"] 