#!/usr/bin/python3
"""100-count"""
from collections import (defaultdict, namedtuple)
import json
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}


_dict = defaultdict(int)
after = None
done = False


def count_words(subreddit, word_list):
    """  queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces. Javascript should count as javascript,
    but java should not)."""
    global after, _dict, done, headers

    subreddit = subreddit.lower()
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
        subreddit, after if after else '')
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return
    content = str(r.content, encoding='utf8')
    obj = get_content_object_form(content)
    data = obj.data
    articles = data.children
    after = data.after

    for article in articles:
        title = article.data.title
        _dict = get_word_count(title, word_list, _dict)

    if after is None:
        return

    count_words(subreddit, word_list)
    if done:
        return
    print_results(_dict)
    done = True


# def helper(subreddit, after, word_list, dict):
#     """ """
#     url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
#         subreddit, after if after else '')
#     r = requests.get(url, headers=headers, allow_redirects=False)
#     if r.status_code != 200:
#         return dict
#     content = str(r.content, encoding='utf8')
#     obj = get_content_object_form(content)
#     data = obj.data
#     articles = data.children
#     after = data.after
#
#     for article in articles:
#         title = article.data.title
#         dict = get_word_count(title, word_list, dict)
#
#     if after is None:
#         return dict
#     return helper(subreddit, after, word_list, dict)


def get_word_count(title, word_list, _dict):
    """ ? """
    for word in word_list:
        wc = title.count(word)
        if wc > 0:
            _dict[word] += wc
    return _dict


def print_results(results):
    """ ? """

    results_info = []
    keys = results.keys()
    for (i, elem) in enumerate(keys):
        results_info.append({'key': elem, 'count': results[elem]})
    results_info = sorted(results_info, key=lambda k: k['count'])[::-1]
    for elem in results_info:
        print("{}: {}".format(elem['key'], elem['count']))


def get_content_object_form(content):
    """ ?? """
    return json.loads(content, object_hook=lambda d: namedtuple(
        'X', d.keys())(*d.values()))
