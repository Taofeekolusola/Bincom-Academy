import psycopg2
from psycopg2 import sql

# Database connection parameters
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "adeshina123"

def show_menu():
    print("\nTodo List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")
# Establish a connection to the PostgreSQL database
def connect_to_database():
    try:
        connection = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        return connection
    except psycopg2.Error as e:
        print(f"Unable to connect to the database. Error: {e}")
        return None

# Create the tasks table if it doesn't exist
def create_tasks_table(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                task_name VARCHAR(255) NOT NULL
            );
        """)
        connection.commit()

# Add a task to the database
def add_task_to_database(connection, task):
    with connection.cursor() as cursor:
        cursor.execute(sql.SQL("INSERT INTO tasks (task_name) VALUES (%s);"), (task,))
        connection.commit()

# Remove a task from the database
def remove_task_from_database(connection, task_id):
    with connection.cursor() as cursor:
        cursor.execute(sql.SQL("DELETE FROM tasks WHERE id = %s;"), (task_id,))
        connection.commit()

# Retrieve tasks from the database
def retrieve_tasks_from_database(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, task_name FROM tasks;")
        tasks = cursor.fetchall()
        return tasks

# Update your add_task, remove_task, and show_tasks functions to interact with the database
def add_task():
    task = input("Enter the task: ")
    add_task_to_database(connection, task)
    print(f"Task '{task}' added successfully.")

def remove_task():
    tasks = retrieve_tasks_from_database(connection)
    if not tasks:
        print("No tasks to remove.")
        return

    print("\nCurrent Tasks:")
    for task_id, task_name in tasks:
        print(f"{task_id}. {task_name}")

    try:
        task_id = int(input("Enter the task number to remove: "))
        remove_task_from_database(connection, task_id)
        print(f"Task with ID {task_id} removed successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def show_tasks():
    tasks = retrieve_tasks_from_database(connection)
    if not tasks:
        print("No tasks.")
    else:
        print("\nCurrent Tasks:")
        for task_id, task_name in tasks:
            print(f"{task_id}. {task_name}")

# Main program loop
connection = connect_to_database()

if connection:
    create_tasks_table(connection)

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

    connection.close()
