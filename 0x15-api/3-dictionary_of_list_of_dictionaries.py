#!/usr/bin/python3
"""Exports to JSON"""


import json
import requests


def get_employees_todo_progress():
    """Get all employees todo list """

    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all employees details
    employees_url = f"{base_url}/users"
    employees_response = requests.get(employees_url)

    # Check if the employees were fetched successfully
    if employees_response.status_code != 200:
        print("Employees not found.")
        return None

    employees_data = employees_response.json()

    # Initialize a dictionary to hold all todo lists
    all_todos = {}

    for employee in employees_data:
        employee_id = employee['id']
        employee_name = employee['username']

    # Fetch employee TODO List
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)

    # Check if TODO list was fetched successfully
    while todos_response.status_code != 200:
        print(f"Failed to fetch TODO list for employee {employee_id}.")
        continue

    todos_data = todos_response.json()

    # Add the employee's todo list to the dictionary
    all_todos[employee_id] = []
    for task in todos_data:
        all_todos[employee_id].append({
            "username": employee_name,
            "task": task.get('title'),
            "completed": task.get('completed')
        })

    return all_todos


def export_all_to_json(all_todos):
    """Exports all data to JSON"""

    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(all_todos, json_file, indent=4)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    all_todos = get_employees_todo_progress()
    if all_todos:
        export_all_to_json(all_todos)
