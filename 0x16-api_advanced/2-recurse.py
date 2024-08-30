#!/usr/bin/python3
"""Module for task 2"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""
    import requests

    sb = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit)
                            ,params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sb.status_code >= 400:
        return None

    h_l = hot_list + [child.get("data").get("title")
                        for child in sb.json()
                        .get("data")
                        .get("children")]

    information = sb.json()
    if not information.get("data").get("after"):
        return h_l

    return recurse(subreddit, h_l, information.get("data").get("count"),
                   information.get("data").get("after"))
