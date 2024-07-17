#!/usr/bin/python3
"""api module to gather data from a given api."""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 1-export_to_CSV.py <employee_id>)")
        sys.exit(1)

    else:
        employee_id = sys.argv[1]

        # Define Base URL/API endpoints
        base_url = 'https://jsonplaceholder.typicode.com/'
        employee_url = f'{base_url}/users/{employee_id}'
        todos_url = f'{base_url}/todos?userId={employee_id}'

        # gets data from api and id from argv[1]
        employee_data = requests.get(employee_url).json()
        employee_name = employee_data['username']
        todo_data = requests.get(todos_url).json()

        # setup data to use in writing file
        tasks = []
        for task in todo_data:
            tasks.append({
                'task': task['title'],
                'completed': task['completed'],
                'username': employee_name
            })

        # json data
        json_data = {employee_id: tasks}

        # Setup JSON file
        with open(f'{employee_id}.JSON', 'w') as f:

            json.dump(json_data, f)
