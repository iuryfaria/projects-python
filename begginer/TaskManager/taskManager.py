import json
import os

ARCHIVES_FILE = {'task.json', 'task.txt'} 


# Load tasks from a JSON or TXT file
def load_tasks():
    # Prioritize JSON file if both exist
    if "task.json" in ARCHIVES_FILE and os.path.exists("task.json"):
        with open("task.json", "r", encoding="utf-8") as f:
            return json.load(f)
        
    #fallback: txt
    if "task.txt" in ARCHIVES_FILE and os.path.exists("task.txt"):
        with open("task.txt", "r", encoding="utf-8") as f:
            for line in f:
                id_, description, line.strip().split(',', 1)
                task.append({'id': int(id_), 'description': description})
            
        return task
    
    return []

# Save tasks to a JSON or TXT file
def save_tasks(tasks):
    for archieve in ARCHIVES_FILE:
        
        #Save to JSON
        if archieve.endswith('.json'):
            with open(archieve, "w", encoding="utf-8") as f:
                json.dump(tasks, f, indent=4, ensure_ascii=False)

        #Save to TXT
        elif archieve.endswith('.txt'):
            with open(archieve, "w", encoding="utf-8") as f:
                for task in tasks:
                    f.write(f"{task['id']},{task['description']}\n")


# Add task
def add_task(tasks):
    description = input("Enter task description: ")

    task = {
        "id": len(tasks) + 1,
        "description": description
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


# List tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("Tasks:")
    for task in tasks:
        print(f"{task['id']}: {task['description']}")

# Delete task
def delete_task(tasks):
    list_tasks(tasks)
    
    try:
        task_id = int(input("Enter a task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)

                # Reorganize IDs
                for i, t in enumerate(tasks):
                    t["id"] = i + 1

                save_tasks(tasks)
                print("Task deleted successfully!")
                return
            
        print("Task ID not found.")
    
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")


# MENU

def menu():
    tasks = load_tasks()
    
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("0. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '0':
            print("Exiting Task Manager. Goodbye!")
            break

menu()