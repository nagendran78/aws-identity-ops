"""
Author: nagendran.s
Description: Script to Retrieve all the Groups and Users associated to it from "AWS-IAM Identity Center"
             using IdentityStore.Client class from Boto3
"""

import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Function to retrieve all Groups info from IAM-Identity-Centre
def get_all_groups(identity_store_id: str, identitystore_client: boto3.client) -> None:
    """
    Module: Fetches all the Group Info and Users EmailID in IAM Identity Center.

    Args:
        identity_store_id (str): The ID of the Identity Store.
        identitystore_client (boto3.client): The initialized Identity Store client.

    Returns:
        list[dict]: A dictionaries containing the list of Groups info and EmailID.
    """
    
    # region Variable Declarations
    groups_with_users       = dict()
    groups_response         = dict()
    group                   = dict()
    membership_response     = dict()
    memberships             = dict()
    membership              = dict()
    group_id                = ""
    group_name              = ""
    user_id                 = ""
    username                = ""
    next_token              = None
    membership_next_token   = None
    # endregion

    try:
        # Step 1: Fetch all groups
        while True:
            if next_token:
                groups_response = identitystore_client.list_groups(
                    IdentityStoreId = identity_store_id,
                    NextToken = next_token
                )
            else:
                groups_response = identitystore_client.list_groups(
                    IdentityStoreId = identity_store_id
                )

            groups = groups_response.get('Groups', [])
            for group in groups:
                group_id = group.get('GroupId')
                group_name = group.get('DisplayName', group_id)  # Default to GroupId if DisplayName is missing
                groups_with_users[group_name] = []
                
                # Step 2: Fetch UserIDs for each Group
                membership_next_token = None
                while True:
                    if membership_next_token:
                        membership_response = identitystore_client.list_group_memberships(
                            IdentityStoreId = identity_store_id,
                            GroupId = group_id,
                            NextToken = membership_next_token
                        )
                    else:
                        membership_response = identitystore_client.list_group_memberships(
                            IdentityStoreId = identity_store_id,
                            GroupId = group_id
                        )

                    memberships = membership_response.get('GroupMemberships', [])
                    for membership in memberships:
                        user_id = membership.get('MemberId', {}).get('UserId')

                        # Fetch user details to retrieve the username
                        user_info = identitystore_client.describe_user(
                            IdentityStoreId = identity_store_id,
                            UserId = user_id
                        )
                        username = user_info.get("UserName", "Unknown")
                        
                        if user_id:
                            groups_with_users[group_name].append(username)
                            #groups_with_users[group_name].append(user_id) #To return user_id

                    membership_next_token = membership_response.get('NextToken')
                    if not membership_next_token:
                        break

            next_token = groups_response.get('NextToken')
            if not next_token:
                break

    except identitystore_client.exceptions.AccessDeniedException as e:
        print(f"Access Denied: Check the IAM permissions.")
        print(e)
    except Exception as e:
        print(f"Error fetching groups or memberships: {str(e)}")

    return groups_with_users