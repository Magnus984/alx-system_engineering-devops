#!/usr/bin/python3
"""Gathers data from an API"""
import requests
import sys


employee_id = int(sys.argv[1])
to_do_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos/'
        ).json()
completed = 0
total = 0
for i in range(len(to_do_list)):
    if to_do_list[i].get("userId") == employee_id:
        total += 1
        if to_do_list[i].get("completed"):
            completed += 1

users = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        ).json()

name = users.get('name')
print(
    f"Employee {name} is done with tasks({completed}/{total})"
)

for i in range(len(to_do_list)):
    if to_do_list[i].get("userId") == employee_id:
        if to_do_list[i].get("completed"):
            print("\t {}".format(
                to_do_list[i].get("title"))
                )
