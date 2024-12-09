"""
Author: nagendran.s
Description: Retrieve All the Groups and Users associated to it
             from "AWS-IAM Identity Center"
"""

import boto3
import uuid

# Add the project root to sys.path
from bootstrap import setup_project_path
setup_project_path()

from src.groups import all_group
from src.groups import export_groups

# AWS Payer CLI Profile name
aws_profile_name            = '' 

# IAM Identity Center - Store ID
identity_centre_store_id    = ''

#Output File Name
output_file_name            = "group-" + uuid.uuid4().hex + ".csv"

# Method Execution Section
if __name__ == "__main__":
    # Create a session using the specified AWS profile
    session = boto3.Session(profile_name = aws_profile_name)

    # Create an identitystore client from the session
    identitystore_client = session.client('identitystore')

    # Fetch all the Groups
    groups_data = dict()
    groups_data = all_group.get_all_groups(identity_centre_store_id, identitystore_client)

    # region Print Group-Name and UserName details on the screen
    """
    for group_name, username in groups_data.items():
        print(f"Group: {group_name}")
        print(f"Username: {', '.join(username)}")
        print("-" * 40)  # Separator for better readability
    """
    # endregion
        
    # Export Groups data to CSV 
    export_groups.export_groups_to_csv(groups_data, output_file_name)

    #Notify the process has been completed.
    print(f"Completed fetching Groups", "\U0001F60E")
    print(f"Output File Name: {output_file_name}")