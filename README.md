✅ To-Do List Manager

A simple command-line To-Do List Manager built with Python.

This project allows users to create and manage their tasks directly from the terminal. Tasks are stored in a "tasks.json" file so they can be saved and loaded when the program is run again.

✨ Features

The To-Do List Manager provides the following options:

1. Add Task
   
   - Enter a task ID
   - Enter a task name
   - New tasks are saved automatically

2. View Tasks
   
   - Displays all saved tasks
   - Shows the task ID, task name, and completion status

3. Mark Task Complete
   
   - Enter a task ID
   - Changes the task's status to completed

4. Delete Task
   
   - Enter a task ID
   - Removes the selected task

5. Exit
   
   - Closes the To-Do List Manager

💾 Data Storage

The program uses a JSON file to store tasks.

tasks.json

Example of the stored data:

[
    {
        "ID": 1,
        "Task name": "Learn Python",
        "Completed": false
    },
    {
        "ID": 2,
        "Task name": "Practice SQL",
        "Completed": true
    }
]

Because tasks are stored in a JSON file, they can be loaded again when the program starts.

🛠️ Technologies Used

- Python 3
- "json" module
- "random" module
- File handling
- Lists and dictionaries

No external Python libraries are required.

▶️ How to Run

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

2. Open the project folder

cd YOUR-REPOSITORY

3. Run the program

python todo.py

On Linux, you can also use:

python3 todo.py

📋 Example

WELCOME TO
 ~~~~~~~~~~~~~~~ TO DO LIST MANAGER ~~~~~~~~~~~~~~~~~~

1. Add Task
2. View Tasks
3. Mark task Complete
4. Delete Task
5. Exit

enter which task you want to do: 1

enter task ID: 1
enter your task: Learn Python

task added succesfully
Your Task ID is: 1

Viewing tasks:

=========================YOUR TASKS========================
  ID                 TASK                     status

{'ID': 1, 'Task name': 'Learn Python', 'Completed': False}

After completing the task:

enter task id whose task you want to mark completed: 1

task marked as completed

🧠 Python Concepts Practiced

This project was created to practice fundamental Python concepts:

- Variables
- Functions
- Lists
- Dictionaries
- Loops
- Conditional statements
- User input
- Exception handling
- File handling
- JSON
- "try" and "except"
- Reading and writing files

📁 Project Structure

to-do-list-manager/
│
├── todo.py
├── tasks.json
└── README.md

«"tasks.json" is created automatically when a task is saved if it does not already exist.»

🎯 Project Goal

The main goal of this project is to build a simple task-management program while learning how Python programs can store and manage data using files.

🚀 Future Improvements

Possible improvements for future versions:

- Automatically generate unique task IDs
- Edit existing tasks
- Add task priorities
- Add due dates
- Show only completed or pending tasks
- Improve the terminal interface
- Add a graphical user interface (GUI)
- Add task search functionality

👨‍💻 Author

Akhlesh Prajapati

B.Sc. (Hons.) Information Science Student

---

⭐ If you find this project useful, feel free to star the repository!