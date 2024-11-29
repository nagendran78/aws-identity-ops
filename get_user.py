"""
Author: nagendran.s
Description: Retrieve Userd from "AWS-IAM Identity Center" and Export to CSV 
"""

import boto3
import uuid
from library import users
from library import common
from library import export_users

# AWS Payer CLI Profile name
aws_profile_name            = '' 

# IAM Identity Center - Store ID
identity_centre_store_id    = ''

#Output File Name
output_file_name            = "users-" + uuid.uuid4().hex + ".csv"

# Method Execution Section
if __name__ == "__main__":
    # Create a session using the specified AWS profile
    session = boto3.Session(profile_name = aws_profile_name)

    # Create an identitystore client from the session
    identitystore_client = session.client('identitystore')

    # Execute function to fetch result for individual AWS-Account
    users = users.list_users(identity_centre_store_id, identitystore_client)

    # Print user details on the screen
    #for user in users:
    #    print(user)

    # Execute users to CSV
    export_users.export_users_to_csv(users, output_file_name)


    #Notify the process has been completed.
    common.clear_screen() 
    print(f"Completed fetching Users", "\U0001F60E")
    print(f"Output File Name: {output_file_name}")