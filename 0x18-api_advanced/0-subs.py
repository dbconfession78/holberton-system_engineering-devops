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
    ua = {"User-Agent": "some user agent by(me)"}

    headers.update(ua)
    r = requests.get(url, headers=headers).json()
    retval = r.get('data', {}).get('subscribers')
    if retval is None:
        return 0
    return retval
