"""
Author: nagendran.s
Description: Script to export Groups and Users data to CSV file
"""

import csv

# Exports Group and User details into a CSV file for reporting purposes.
def export_groups_to_csv(groups_with_users: dict, output_file: str) -> None:
    """
    Module: Exports the Group and associated User data to a CSV file

    Args:
        groups_with_users (dict): A dictionary where keys are Group names and values are lists of Usernames.
        output_file (str): Path to output the CSV file.

    Returns:
        None
    """
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write data in the desired format
            for group, users in groups_with_users.items():
                # Write the group name as a separate row
                writer.writerow(["Group", group])
                
                # Write the usernames in separate rows
                for username in users:
                    writer.writerow(["", username])

                # Write a blank row after each group block
                writer.writerow([])

        print(f"Group data exported to: {output_file}")

    except Exception as e:
        print(f"Error exporting group data to CSV file '{output_file}': {e}")
# endregion