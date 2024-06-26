#!/usr/bin/python3
"""
A recursive function
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "My Custom User-Agent"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for value in results.get("children"):
        hot_list.append(value.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
