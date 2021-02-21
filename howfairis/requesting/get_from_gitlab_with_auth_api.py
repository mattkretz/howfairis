import requests
from backoff import expo
from backoff import on_exception
from ratelimit import RateLimitException
from ratelimit import limits


# https://docs.gitlab.com/ee/user/gitlab_com/index.html#gitlabcom-specific-rate-limits
@on_exception(expo, RateLimitException, max_tries=8)
@limits(calls=2000, period=60)
def get_from_gitlab_with_auth_api(url, apikeys):

    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    username = apikeys.get("gitlab").get("username")
    key = apikeys.get("gitlab").get("key")

    return requests.get(url, headers, auth=(username, key))
