#!/usr/bin/python3
"""
<<<<<<< HEAD
queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
=======
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

>>>>>>> 8c86fed25c18cd0bba8476e31884382815369c61
import requests


def number_of_subscribers(subreddit):
<<<<<<< HEAD
    """returns number of total subscribers"""
    url = ("https://www.reddit.com/dev/api/me/{}".format(subreddit))
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return (0)
    response = response.json()
    if 'data' in response:
        return (response.get('data').get('subscribers'))

    else:
        return (0)
=======
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
>>>>>>> 8c86fed25c18cd0bba8476e31884382815369c61
