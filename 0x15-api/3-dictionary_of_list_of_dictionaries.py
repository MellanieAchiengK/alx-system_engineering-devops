#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    employees = requests.get("https://jsonplaceholder.typicode.com/users")
    employees = employees.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todoAll = {}

    for employee in employees:
        taskList = []
        for task in todos:
            if task.get('userId') == employee.get('id'):
                taskDict = {"username": employee.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[employee.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
