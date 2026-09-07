tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\n--- TO-DO LIST ---")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{i}. {task['name']} - {status}")


def add_task():
    task = input("Enter task: ")
    tasks.append({"name": task, "completed": False})
    print("Task added successfully!")


def update_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to update: "))

        if 1 <= number <= len(tasks):
            new_task = input("Enter new task: ")
            tasks[number - 1]["name"] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted = tasks.pop(number - 1)
            print(f"'{deleted['name']}' deleted successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def mark_completed():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to mark as completed: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n======================")
    print("      TO-DO LIST")
    print("======================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Completed")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        mark_completed()

    elif choice == "6":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")