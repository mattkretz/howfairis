import requests


def get_from_github_with_auth_raw(url, apikeys):

    headers = {}

    username = apikeys.get("github").get("username")
    key = apikeys.get("github").get("key")

    return requests.get(url, headers, auth=(username, key))
