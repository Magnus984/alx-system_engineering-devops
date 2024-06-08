#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """retuns title of posts or None if subreddit is invalid"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            "User-Agent": "My Custom User-Agent"
            }
    params = {
            "limit": 10,
            "t": "all"
            }
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            print(f'{post["data"]["title"]}')
    else:
        print("None")
