#!/usr/bin/python3
"""
Queries API and prints first 10
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
    """
    headers = {"User-Agent": "ALX"}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']['children']
        for posts in data[:10]:
            print(posts['data']['title'])
    else:
        print(None)


if __name__ == "__main__":
    pass
