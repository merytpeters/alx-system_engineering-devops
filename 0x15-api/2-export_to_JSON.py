#!/usr/bin/python3
"""Exports to JSON"""


import csv
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Gets employee todo list """

    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)

    # Check if the employee exists
    if employee_response.status_code != 200:
        print("Employee not found.")
        return

    employee_data = employee_response.json()
    employee_name = employee_data['username']

    # Fetch employee TODO List
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)

    # Check if TODO list was fetched successfully
    if todos_response.status_code != 200:
        print("Failed to fetch TODO list.")
        return

    todos_data = todos_response.json()
    return employee_name, todos_data


def export_to_json(employee_id, username, todo_list):
    """Exports data to JSON"""

    json_data = {employee_id: []}
    for task in todo_list:
        json_data[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            username, todo_list = get_employee_todo_progress(employee_id)
            if username and todo_list:
                export_to_json(employee_id, username, todo_list)
        except ValueError:
            print("Employee ID must be an integer.")
