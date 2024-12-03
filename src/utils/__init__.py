"""
Author: nagendran.s

Utility Submodule Initialization

This submodule profides function for Common or Utility related operations. The `__init__.py`
file imports key functions to expose them as part of the package's public API.

Exposed API:
- clear_screen: Clear Screen at CLI.

Modules:
- common: Handles common utility functions.

Usage:
Import specific function or modules as needed:
    from src.utils import common
"""

# src/utils/__init__.py
# Import specific function
from .common import clear_screen

# Specifying explicity Public API that should be exposed
__all__ = ["clear_screen"]
print("Initializing utils package...")