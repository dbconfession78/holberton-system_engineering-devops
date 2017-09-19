#!/usr/bin/python3
"""
Module: 2-export_to_JSON
"""
import json
import requests
import sys


def print_completed(user_id):
    """ prints a list of given user's completed todo's  """
    base_url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users?id={}'.format(base_url, user_id)).json()
    todos = requests.get('{}/todos?userId={}'.format(base_url, user_id)).json()

    list = [
        {"task": td.get('title'),
         "completed": td.get('completed'),
         "username": user[0].get('username')} for td in todos]

    with open('{}.json'.format(user_id), encoding='utf-8',
              mode='w', newline="") as f:
        json.dump({user_id: list}, f)

if __name__ == '__main__':
    """ script entry point """
    if len(sys.argv) > 1:
        try:
            user_id = sys.argv[1]
            print_completed(user_id)
        except:
            pass
