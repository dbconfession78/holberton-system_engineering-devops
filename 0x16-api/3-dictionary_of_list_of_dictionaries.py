#!/usr/bin/python3
"""
Module: 3-dictionary_of_list_of_dictionaries
"""
import json
import requests
import sys


def main():
    """ entry point  """
    base_url = 'https://jsonplaceholder.typicode.com'
    users = requests.get('{}/users'.format(base_url)).json()
    dict = {}
    for user in users:
        username = user.get('username')
        user_id = user.get('id')
        todos = requests.get('{}/todos?userId={}'.format(
            base_url, user_id)).json()

        list = [{"username": username, "task": td.get('title'),
                 "completed": td.get('completed')} for td in todos]
        dict[user_id] = list

    with open('todo_all_employees.json', encoding='utf-8',
              mode='w', newline="") as f:
        json.dump(dict, f)


if __name__ == '__main__':
    """ script entry point """
    main()
