"""
Author: nagendran.s
Description: Script to Retrieve Groups info for a specific User from "AWS-IAM Identity Center"
             using IdentityStore.Client class from Boto3
"""

import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Function to retrieve specific User-Group info from IAM-Identity-Centre
def get_groups_for_user(identity_store_id: str, identitystore_client: boto3.client, user_id: str) -> None:
    """
    Module: Fetches the group IDs and group names associated with a user from the IAM Identity Center.

    Args:
        identity_store_id (str): The ID of the Identity Store.
        identitystore_client (boto3.client): The initialized Identity Store client.
        user_id (str): The ID of the user.

    Returns:
        list[dict]: A dictionaries containing the list of group IDs and group names.
    """

    # region Variable Declaration
    user_info: list[dict]   = []
    username                = ""
    group_id                = ""
    group_info: list[dict]  = []
    group_details           = []
    # endregion

    try:
        # Fetch user details to retrieve the username
        user_info = identitystore_client.describe_user(
            IdentityStoreId = identity_store_id,
            UserId = user_id
        )
        username = user_info.get("UserName", "Unknown")

        # Fetch Group memberships based on UserID
        response = identitystore_client.list_group_memberships_for_member(
            IdentityStoreId = identity_store_id,
            MemberId = {"UserId": user_id}
        )
        memberships = response.get('GroupMemberships', [])

        # Extract group details
        for membership in memberships:
            group_id = membership["GroupId"]
            group_info = identitystore_client.describe_group(
                IdentityStoreId = identity_store_id,
                GroupId = group_id
            )
            group_details.append({
                "GroupId": group_id,
                "GroupName": group_info.get("DisplayName", "Unknown")
            })            
        return {
            "UserName": username,
            "Groups": group_details
        }

    except ClientError as e:
        print(f"An error occurred: {e.response['Error']['Message']}")
        return None
    except BotoCoreError as e:
        print(f"A boto3 error occurred: {str(e)}")
        return None