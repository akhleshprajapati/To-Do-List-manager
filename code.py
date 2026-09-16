#***************************************************************************
# LIBRARIES
import random
import json


#***************************************************************************
# VARIABLES
FILE_NAME="tasks.json"


#***************************************************************************
# FUNCTIONS
def add_task():
    while True:
        task_id_input=input("enter task ID: ").strip()
        if not task_id_input:
            print("task ID cannot be empty")
            continue
        try:
            task_id=int(task_id_input)
        except ValueError:
            print("task ID must be a number")
            continue
        break

    while True:
        task_name=input("enter your task: ").strip()
        if task_name:
            break
        print("task name cannot be empty")

    task={
        "ID": task_id,
        "Task name": task_name,
        "Completed": False,
    }
    tasks.append(task)
    save_tasks(tasks)
    print("task added succesfully")
    print(f"Your Task ID is: {task_id}")
    
def view_task():
    print("=========================YOUR TASKS========================")
    print("  ID                 TASK                     status")
    for i in tasks:
        print(i)

def mark_task_completed():
    while True:
        task_id_input=input("enter task id whose task you want to mark completed: ").strip()
        if not task_id_input:
            print("task ID cannot be empty")
            continue
        try:
            task_id=int(task_id_input)
        except ValueError:
            print("task ID must be a number")
            continue
        break

    for task in tasks:
        if task["ID"]==task_id:
            task["Completed"] = True
            save_tasks(tasks)
            print("task marked as completed")
            return
    print("task ID not found")

def delete_task():
    while True:
        task_id_input=input("enter task id whose task you want to delete: ").strip()
        if not task_id_input:
            print("task ID cannot be empty")
            continue
        try:
            task_id=int(task_id_input)
        except ValueError:
            print("task ID must be a number")
            continue
        break

    for task in tasks:
        if task["ID"]==task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("task deleted succesfully")
            return
    print("task ID not found")

def exit():
    print("~~ THANK YOU FOR USING TO DO LIST MANAGER ~~")

def load_tasks():
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)

    except FileNotFoundError:
        return[]

def save_tasks(tasks):
    with open(FILE_NAME,"w") as file:
        json.dump(tasks,file,indent=4)  

# Load saved tasks after the file-handling functions are defined.
tasks=load_tasks()

#***************************************************************************
# MAIN MENU
choice="yes"
while choice=="yes":
    print("WELCOME TO \n ~~~~~~~~~~~~~~~ TO DO LIST MANAGER ~~~~~~~~~~~~~~~~~~")
    print("1. Add Task\n2. View Tasks\n3. Mark task Complete\n4. Delete Task\n5. Exit")
    user_choice=input("enter which task you want to do: ")

    if user_choice=="1":
        add_task()

    elif user_choice=="2":
        view_task()

    elif user_choice=="3":
        mark_task_completed()

    elif user_choice=="4":
        delete_task()

    elif user_choice=="5":
        exit()
        break

    else:
        print("invalid choice, please select 1-5")
    

#***************************************************************************
# For use again
    choice=input("want to use again (yes/no) : ")

    while choice not in ("yes","no"):
        print("you input invalid ,type yes/no")
        choice=input("want to use again (yes/no) : ")

if choice==("no"):
     print("~~ THANK YOU FOR USING TO DO LIST MANAGER ~~")

