# SIMPLE TO-DO LIST MANAGER
# Modules used: Lists, Functions, File Handling
# File to store tasks
FILENAME = "tasks.txt"

# Function to load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                task = line.strip()
                tasks.append(task)
    except FileNotFoundError:
        pass  # If file not found, start with empty list
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Function to show all tasks
def view_tasks(tasks):
    print("\nYour To-Do List:")
    if len(tasks) == 0:
        print("No tasks found!\n")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

# Function to add a new task
def add_task(tasks):
    new_task = input("Enter new task: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added!\n")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"🗑 Task '{removed}' deleted!\n")
    else:
        print("Invalid task number!\n")

# ---------- Main Program ----------
def main():
    tasks = load_tasks()

    while True:
        print("====== TO-DO LIST MENU ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Exiting... Tasks saved in file.")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run the program
if __name__ == "__main__":
    main()