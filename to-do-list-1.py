import os

# Function to add a new task
def add_task(task_list, title, description):
    task_list.append({"title": title, "description": description, "completed": False})

# Function to list all tasks
def list_tasks(task_list):
    if not task_list:
        print("No tasks found!")
    else:
        for index, task in enumerate(task_list):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index + 1}. {task['title']} - {task['description']} - {status}")

# Function to mark a task as completed
def mark_completed(task_list, task_index):
    if 0 < task_index <= len(task_list):
        task_list[task_index - 1]["completed"] = True
    else:
        print("Invalid task index!")

# Function to remove a task
def remove_task(task_list, task_index):
    if 0 < task_index <= len(task_list):
        del task_list[task_index - 1]
    else:
        print("Invalid task index!")

# Function to save tasks to a file
def save_tasks(task_list, file_path):
    with open(file_path, "w") as file:
        for task in task_list:
            file.write(f"{task['title']},{task['description']},{task['completed']}\n")

# Function to load tasks from a file
def load_tasks(file_path):
    task_list = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                title, description, completed = line.strip().split(",")
                task_list.append({"title": title, "description": description, "completed": completed == "True"})
    return task_list

# Main function
def main():
    file_path = "tasks.txt"
    tasks = load_tasks(file_path)

    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Mark Task as Completed\n4. Remove Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(tasks, title, description)
            save_tasks(tasks, file_path)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            task_index = int(input("Enter task index to mark as completed: "))
            mark_completed(tasks, task_index)
            save_tasks(tasks, file_path)
        elif choice == "4":
            task_index = int(input("Enter task index to remove: "))
            remove_task(tasks, task_index)
            save_tasks(tasks, file_path)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
