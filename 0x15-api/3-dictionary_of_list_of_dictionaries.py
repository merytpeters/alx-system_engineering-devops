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

    employees_data = employees_response.json()

    # Fetch employee TODO List
    todos_url = f"{base_url}/todos"
    todos_response = requests.get(todos_url)

    # Check if TODO list was fetched successfully
    if todos_response.status_code != 200:
        print(f"Failed to fetch TODO list for employee {employee_id}.")
        return None

    todos_data = todos_response.json()

    # initialize a dictionary to hold the tasks for each user
    all_todos = {}

    # Add the employee's todo list to the dictionary
    for employee in employees_data:
        employee_id = employee["id"]
        employee_name = employee["username"]
        employee_tasks = []
        for task in todos_data:
            if task["userId"] == employee_id:
                task_info = {
                    "username": employee_name,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                employee_tasks.append(task_info)

        all_todos[employee_id] = employee_tasks
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
