#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to JSON"""

import json
import requests
import sys


if __name__ == "__main__":
    todo_url = "https://jsonplaceholder.typicode.com/user/{}/todos".format(
        sys.argv[1])
    employees_url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    employees_result = get(todo_url).json()
    employees_result = get(employees_url).json()

    todo_list = []
    for todo in todo_result:
        todo_dict = {}
        todo_dict.update({"task": todo.get("title"), "completed": todo.get(
            "completed"), "username": employees_result.get("username")})
        todo_list.append(todo_dict)

    with open("{}.json".format(sys.argv[1]), 'w') as f:
        dump({sys.argv[1]: todo_list}, f)
