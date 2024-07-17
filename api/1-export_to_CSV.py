#!/usr/bin/python3
"""api module to gather data from a given api."""
import requests
import sys
import csv


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
        employee_name = employee_data['name']
        todo_data = requests.get(todos_url).json()
        completed_tasks = [task for task in todo_data if task['completed']]

        # Setup CSV file
        with open(f'{employee_id}.csv', 'w') as f:

            for task in completed_tasks:
                csv.writer(f, quoting=csv.QUOTE_ALL).writerow([
                    employee_id,
                    employee_name,
                    task['completed'],
                    task['title']
                    ])
