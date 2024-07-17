#!/usr/bin/python3
"""api module to gather data from a given api."""
import requests
import sys


def get_employee_todo_info(employee_id):
    """ supposed to pull from an rest api and return the data in a certain format. """

    # Define Base URL/API endpoints
    base_url = 'https://jsonplaceholder.typicode.com/'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # gets data from api
    employee_data = requests.get(employee_url).json()
    employee_name = employee_data['name']
    todo_data = requests.get(todos_url).json()
    total_tasks = len(todo_data)
    completed_tasks = [task for task in  todo_data if task['completed']]
    done_tasks = len(completed_tasks)

    # prints data to std out
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    """ beginning of main to use to get employee info """
    
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>)")
        sys.exit(1)

get_employee_todo_info(sys.argv[1])
