#!/usr/bin/python3
"""Script that fetches and imports an employee's TO-DO list progress
    to csv"""


import requests
import sys
import csv


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


def export_to_csv(employee_id, username, todo_list):
    """Exports data to CSV"""

    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            csv_writer.writerow([employee_id, username,
                                task.get('completed'), task.get('title')])
    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            username, todo_list = get_employee_todo_progress(employee_id)
            if username and todo_list:
                export_to_csv(employee_id, username, todo_list)
        except ValueError:
            print("Employee ID must be an integer.")
