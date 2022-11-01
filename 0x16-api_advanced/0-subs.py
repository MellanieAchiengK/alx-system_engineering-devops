#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ function that queries subreddit
    and returns no. of subscribers """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {"User-Agent": "ALX"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        subscribers = response.json()['data']['subscribers']
        return subscribers
    else:
        return 0


if __name__ == "__main__":
    pass
