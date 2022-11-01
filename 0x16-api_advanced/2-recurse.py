#!/usr/bin/python3
"""
Queries API and prints list containing all titles
"""
import requests


after = ""


def recurse(subreddit, hot_list=[]):
    """
    function that queries the Reddit API and returns list containing
    the titles of all hot articles for a subreddit
    """
    global after
    headers = {"User-Agent": "ALX"}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    if after:
        url = url + "?after=" + after
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']['children']

        for i in response.json()['data']['children']:
            hot_list.append(i['data']['title'])
        if after:
            return recurse(subreddit, hot_list)
        return hot_list


if __name__ == "__main__":
    pass
