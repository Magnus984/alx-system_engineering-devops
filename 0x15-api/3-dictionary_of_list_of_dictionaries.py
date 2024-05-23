#!/usr/bin/python3
"""
export data in the JSON format.
"""
import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(url)
    Users = res.json()

    users_dict = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        url = url + '/todos/'
        res = requests.get(url)

        tasks = res.json()
        users_dict[USER_ID] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })

    with open(
            'todo_all_employees.json',
            mode='w', encoding='utf-8'
            ) as file:
        json.dump(users_dict, file)
