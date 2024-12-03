"""
Author: nagendran.s
Description: Script to export users data to CSV file
"""

import csv

# Exports user details into a CSV file for reporting purposes.
def export_users_to_csv(users: list[dict], output_file: str) -> None:
    """
    Module: Exports the list of users to CSV file.

    Args:
        users (list[Dict]): List of User dictionaries.
        output_file (str): Path to output the CSV file.

    Returns:
        None
    """

    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write header row
            headers = ['UserId', 'UserName', 'Email', 'DisplayName']
            writer.writerow(headers)

            # Write user rows
            for user in users:
                writer.writerow([
                    user.get('UserId', ''),
                    user.get('UserName', ''),
                    user.get('Emails', [{}])[0].get('Value', '') if user.get('Emails') else '',
                    user.get('DisplayName', '')
                ])

        print(f"User data exported to: {output_file}")

    except Exception as e:
        print(f"Error exporting user data to CSV file '{output_file}': {e}")