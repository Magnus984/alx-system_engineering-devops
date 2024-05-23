#!/usr/bin/python3
"""
export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    tasks_list = []

    employee_id = int(sys.argv[1])
    to_do_list = requests.get(
            'https://jsonplaceholder.typicode.com/todos/'
            ).json()
    users = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}'
            ).json()
    name = users.get('username')
    for i in range(len(to_do_list)):
        if to_do_list[i].get("userId") == employee_id:
            myDict = {}
            myDict["task"] = to_do_list[i].get('title')
            myDict["completed"] = to_do_list[i].get('completed')
            myDict["username"] = name
            tasks_list.append(myDict)
    full_dict = {f'{employee_id}': tasks_list}

    with open(
            f'{employee_id}.json', mode='w', encoding='utf-8'
            ) as myFile:
        myFile.write(json.dumps(full_dict))
