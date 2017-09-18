#!/usr/bin/python3
"""
Module: 0-gather_data_from_an_API
"""
import requests
import sys


def print_completed(user_id):
    """ prints a list of given user's completed todo's  """
    base_url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users?id={}'.format(base_url, user_id)).json()
    posts = requests.get('{}/posts'.format(base_url)).json()
    todos = requests.get('{}/todos?userId={}'.format(base_url, user_id)).json()
    completed = [td for td in todos if td.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'.format(
        user[0].get('name'), len(completed), len(todos)))

    for todo in completed:
        print('\t{}'.format(todo.get('title')))


if __name__ == '__main__':
    """ script entry point """
    if len(sys.argv) > 1:
        try:
            user_id = sys.argv[1]
            print_completed(user_id)
        except:
            pass
