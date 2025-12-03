"""This module is a simple to do app written in python, with the user interface being the terminal
"""
task_list = []

def add_task(task_title) :
    """This function takes a task and appends it to the task list

    Args:
        task (string): The title of the task. The title provided 
        by the user is appended to the task list
    """
    task_list.append(task_title)
    print("Task successfully added")

def show_tasks():
    """iterates through the list
    """
    if len(task_list) == 0 :
        print("No tasks yet")
    else:
        for i, task in enumerate(task_list):
            print(i, task)

def remove_task(task_number):
    """Removes a task given by the task # provided by the user

    Args:
        tasknumber (int): Denotes the index of the particular task in the task list
    """
    task_list.pop(task_number)
    print("Task successfully removed")

def edit_task(task_number):
    """Edits a task given by the task # provided by the user

    Args:
        task_number (int): Denotes the index of the particular task in the task list
    """
    remove_task(task_number)
    task_list.insert(task_number,
                     input("Enter task: "))
def main():
    """The driver function. This is also where the main loop of the program is located.
    """
    while True:
        print("1. Add a task")
        print("2. Show all tasks")
        print("3. Remove a task")
        print("4. Edit task")
        print("5. Exit application")
        ch = input("Enter action: ")
        if ch == "1" :
            t = input("Enter task: ")
            add_task(t)
            print("--------------------")
        elif ch == "2":
            show_tasks()
            print("--------------------")
        elif ch == "3":
            n = int(input("Enter the task # of the task to  be removed: "))
            remove_task(n)
            print("--------------------")
        elif ch == "4":
            n= int(input("Enter the task # of the task to be edited: "))
            edit_task(n)
        elif ch == "5":
            break
        else:
            print("Invalid action")
            print("--------------------")
main()
