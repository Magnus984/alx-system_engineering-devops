#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
            "User-Agent": "Mozilla/5.0"
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    return 0
