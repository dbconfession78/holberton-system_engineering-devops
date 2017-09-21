#!/usr/bin/python3
"""
module: 0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API (https://www.reddit.com/dev/api/) and
    returns the number of subscribers for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = requests.utils.default_headers()
    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
          'AppleWebKit/537.36 (KHTML, like Gecko) ' +
          'Chrome/55.0.2883.87 Safari/537.36'}

    headers.update(ua)
    r = requests.get(url, headers=headers).json()
    retval = r.get('data').get('subscribers')
    if retval is None:
        return 0
    return retval
