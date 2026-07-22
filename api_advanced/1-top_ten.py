#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit. Prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "top-ten-checker/1.0"}
    params = {"limit": 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        results = response.json().get("data").get("children")
        if not results:
            print(None)
            return
        for post in results:
            print(post.get("data").get("title"))
    except (AttributeError, TypeError, ValueError):
        print(None)
