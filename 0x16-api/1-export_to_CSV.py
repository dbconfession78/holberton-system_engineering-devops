#!/usr/bin/python3
"""
Module: 1-export_to_CSV
"""
import csv
import requests
import sys


def write_csv(user_id):
    """ prints a list of given user's completed todo's  """
    base_url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users?id={}'.format(base_url, user_id)).json()
    todos = requests.get('{}/todos?userId={}'.format(base_url, user_id)).json()

    with open('{}.csv'.format(user_id),
              encoding='utf-8', mode='w', newline="") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        for td in todos:
            writer.writerow([
                user_id,
                user[0].get('username'),
                td.get('completed'),
                td.get('title')
            ])


if __name__ == '__main__':
    """ script entry point """
    if len(sys.argv) > 1:
        try:
            user_id = sys.argv[1]
            write_csv(user_id)
        except:
            pass
