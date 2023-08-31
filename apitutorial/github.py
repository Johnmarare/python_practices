#!/usr/bin/python3
# github.py
"""
OAUTH practice using githup API
"""

import requests

# create variables with Client ID and Client SECRET
CLIENT_ID = "15bcdf6d458008cb38a3"
CLIENT_SECRET = "acec5530314573a84cdb2c20d538ea24f9e0c302"

# create variable with the "Authorization callback URL" field.
REDIRECT_URI = "https://httpbin.org/anything"


def create_oauth_link():
    """
    Function that creates a link to redirect the user to their GitHub account.
    First define required parameters that the API expects, call the API using
    the requests package and .get()method.
    """
    params = {
            "client_id": CLIENT_ID,
            "redirect_uri": REDIRECT_URI,
            "scope": "user",
            "response_type": "code",
    }

    endpoint = "https://github.com/login/oauth/authorize"
    response = requests.get(endpoint, params=params)
    return response.url


def exchange_code_for_access_token(code=None):
    """
    Function that exchanges the code gotten for an access token.
    A POST request is made in exchange for access token.
    If successful, a valid access token is returned.
    """
    params = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_uri": REDIRECT_URI,
            "code": code,
    }

    headers = {"Accept": "application/json"}
    endpoint = "https://github.com/login/oauth/access_token"
    response = requests.post(endpoint, params=params, headers=headers).json()
    return response["access_token"]


def print_user_info(access_token=None):
    """
    Time to test our access token. Function that returns user info.
    Based on GitHub info.
    """
    headers = {"Authorization": f"token {access_token}"}
    endpoint = "https://api.github.com/user"
    response = requests.get(endpoint, headers=headers).json()
    name = response["name"]
    username = response["login"]
    public_repos_count = response["total_private_repos"]
    print(f"{name} ({username}) | private repositories: {private_repos_count}")


link = create_oauth_link()
print(f"Follow the link to start the authentication with GitHub: {link}")
code = input("GitHub code: ")
access_token = exchange_code_for_access_token(code)
print(f"Exchanged code {code} with access token: {access_token}")
print_user_info(access_token=access_token)
