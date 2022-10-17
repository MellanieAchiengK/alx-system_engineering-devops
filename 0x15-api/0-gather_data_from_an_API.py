#!/usr/bin/python3
""" use REST API to return TODO list informatio """

import requests
import sys

if __name__ == "__main__":

    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1]))

    name = employee.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_response = todos.json()
    
    totalTasks = len(todos_response)
    completed = len([todos for todos in todos_response
                         if todos.get("completed")])

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))
    for task in todos.json():
        if (task.get("completed")):
            print("\t {}".format(task.get("title")))
