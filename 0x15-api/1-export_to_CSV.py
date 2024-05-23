#!/usr/bin/python3
"""
Exports data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    list_to_csv = []

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
            sub_list = []
            sub_list.append(employee_id)
            sub_list.append(name)
            sub_list.append(to_do_list[i].get("completed"))
            sub_list.append(to_do_list[i].get("title"))
            list_to_csv.append(sub_list)

    with open(f'{employee_id}.csv', mode='w') as employee_file:
        employee_writer = csv.writer(
                employee_file, delimiter=',',
                quotechar='"', quoting=csv.QUOTE_ALL
                )
        for i in range(len(list_to_csv)):
            employee_writer.writerow(list_to_csv[i])
