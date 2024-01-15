# Simple To-Do List in Python

# Initialize an empty list to store tasks
tasks = []

def show_menu():
    print("\nTodo List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return
    
    print("\nCurrent Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    try:
        task_index = int(input("Enter the task number to remove: "))
        if 1 <= task_index <= len(tasks):
            removed_task = tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def show_tasks():
    if not tasks:
        print("No tasks.")
    else:
        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Main program loop
while True:
    show_menu()

    try:
        choice = int(input("\nEnter your choice (1-4): "))
        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            show_tasks()
        elif choice == 4:
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
