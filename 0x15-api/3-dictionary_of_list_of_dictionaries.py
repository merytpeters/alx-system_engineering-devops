#!/usr/bin/python3
"""Exports to JSON"""


import json
import requests


# Get all employees todo list
base_url = "https://jsonplaceholder.typicode.com"

# Fetch all employees details
employees_url = f"{base_url}/users"
employees_response = requests.get(employees_url)

employees_data = employees_response.json()

# Fetch employee TODO List
todos_url = f"{base_url}/todos"
todos_response = requests.get(todos_url)
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
                "task": task['title'],
                "completed": task['completed']
            }
            employee_tasks.append(task_info)

    all_todos[employee_id] = employee_tasks


# Exports all data to JSON
json_filename = "todo_all_employees.json"
with open(json_filename, mode='w') as json_file:
    json.dump(all_todos, json_file, indent=4)
