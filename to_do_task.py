from datetime import datetime

# Define a list to store tasks along with their due dates and times
tasks = []

# Function to add a task with a due date and time to the list
def add_task(task, due_date):
    tasks.append((task, due_date))
    print(f"Task '{task}' added to the To-Do List with due date and time: {due_date}")

# Function to remove a task from the list
def remove_task(task):
    removed = False
    for t in tasks:
        if t[0] == task:
            tasks.remove(t)
            removed = True
            print(f"Task '{task}' removed from the To-Do List.")
            break
    if not removed:
        print(f"Task '{task}' not found in the To-Do List.")

# Function to display the current tasks in the list
def show_tasks():
    if not tasks:
        print("\nYour To-Do List is empty.")
    else:
        print("\nYour To-Do List:")
        for index, (task, due_date) in enumerate(tasks, start=1):
            print(f"{index}. {task} (Due: {due_date})")

# Main loop to interact with the user
while True:
    print("\n----------OPTIONS:----------")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show tasks")
    print("4. Quit")
    print("----------------------------")

    choice = input("\nEnter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("\nEnter the task you want to add: ")
        due_date_str = input("Enter the due date (e.g., 'DD-MM-YYYY'): ")
        due_time_str = input("Enter the due time (e.g., 'HH:MM'): ")
        try:
            due_date = datetime.strptime(due_date_str, "%d-%m-%Y")
            due_time = datetime.strptime(due_time_str, "%H:%M").time()
            due_date_time = datetime.combine(due_date, due_time)
            add_task(task, due_date_time)
        except ValueError:
            print("Invalid date or time format. Please use 'DD-MM-YYYY' for date and 'HH:MM' for time.")
    elif choice == '2':
        task = input("\nEnter the task you want to remove: ")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
