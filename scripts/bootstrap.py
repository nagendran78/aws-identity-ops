"""
Author: nagendran.s
Description: Helper script to bootstrap project directory 
"""

import sys
import os

def setup_project_path():
    # Retrieve the directory of the current script (bootstrap.py)
    script_dir = os.path.dirname(__file__)

    # Retrieve the project root directory by going one level up
    project_root = os.path.abspath(os.path.join(script_dir, ".."))  

    if project_root not in sys.path:  # Ensure project_root is not already in sys.path to avoid duplicates
        sys.path.append(project_root) # Add the project root directory to sys.path
