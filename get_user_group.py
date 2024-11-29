"""
Author: nagendran.s
Description: Retrieve Group info based on UserID from "AWS-IAM Identity Center"
"""

import boto3
from library.groups import group_user

# AWS Payer CLI Profile name
aws_profile_name            = '' 

# IAM Identity Center - Store ID
identity_centre_store_id    = ''


# Method Execution Section
if __name__ == "__main__":
    # Create a session using the specified AWS profile
    session = boto3.Session(profile_name = aws_profile_name)

    # Create an identitystore client from the session
    identitystore_client = session.client('identitystore')

    # Fetch group details for the given user
    user_id = '32f441fe-6045-41b4-a3a9-f76d47cf7d95' #kristian.cabrera@cheetahdigital.com
    user_data = group_user.get_groups_for_user(identity_centre_store_id, identitystore_client, user_id)

    if user_data:
        print(f"User Name: {user_data['UserName']}")
        print("Groups associated with the user:")
        for group in user_data['Groups']:
            print(f"Group Name: {group['GroupName']}")
    else:
        print("No groups found or an error occurred.")