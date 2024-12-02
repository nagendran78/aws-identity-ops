"""
Author: Nagendran Sandraprakasam 
Description: Contains all the common functions" 
"""

import os

# Function to clear screen
def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
