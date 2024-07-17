#!/usr/bin/python3
"""api module to gather data from a given api."""
import json
import requests


if __name__ == "__main__":

    # Define Base URL/API endpoints
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users'
    todos_url = f'{base_url}/todos'

    # gets employee data from api
    employee_data = requests.get(employee_url).json()

    json_data = {}

    # get tasks for each employee
    for employee in employee_data:
        employee_id = employee['id']
        employee_name = employee['username']

        # gets tasks data
        todo_data = requests.get(f'{todos_url}?userId={employee_id}').json()

        # setup data to use in writing file
        tasks = []
        for task in todo_data:
            tasks.append({
                'task': task['title'],
                'completed': task['completed'],
                'username': employee_name
            })

        # json data
        json_data[employee_id] = tasks

    # Setup JSON file
    with open(f'todo_all_employees.JSON', 'w') as f:

        json.dump(json_data, f)
