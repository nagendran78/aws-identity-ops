"""
Author: nagendran.s
Description: Script to Retrieve Users from "AWS-IAM Identity Center"
             using IdentityStore.Client class from Boto3
"""

import boto3

# Function to retrieve Users info from IAM-Identity-Centre
def list_users(identity_store_id: str, identitystore_client: boto3.client) -> list[dict]:
    """
    Module: Lists all users from the IAM Identity Center.  

    Args:    
        identity_store_id (str): The ID of the Identity Store.
        identitystore_client (boto3.client): The initialized Identity Store client.

    Returns:
        list[dict]: A dictionary containing the list of Users.
    """

    # region Variable Declaration
    users: list[dict] = []
    next_token = None
    # endregion

    try:
        while True:
            if next_token:
                response = identitystore_client.list_users(
                    IdentityStoreId = identity_store_id,
                    NextToken = next_token
                )
            else:
                response = identitystore_client.list_users(
                    IdentityStoreId = identity_store_id
                )

            # Append user data to the list
            users.extend(response.get('Users', []))

            # Check if there's more data to fetch
            next_token = response.get('NextToken')
            if not next_token:
                break

    except identitystore_client.exceptions.AccessDeniedException as e:
        print("Access Denied: Check the IAM permissions.")
        print(e)
    except Exception as e:
        print(f"Error listing users: {e}")

    return users
