# cli.py
from task_manager import add_task, get_tasks

def show_menu():
    print("\n📅 Task Calendar")
    print("1. Add a Task")
    print("2. View Tasks by Date")
    print("3. Exit")

def handle_add_task():
    task = input("Enter your task: ")
    date_str = input("Enter the due date (YYYY-MM-DD): ")
    success, message = add_task(task, date_str)
    print(message)

def handle_view_tasks():
    tasks = get_tasks()
    if not tasks:
        print("📭 No tasks scheduled.")
        return

    print("\n🗓️ Your Task Calendar:")
    for date in sorted(tasks):
        print(f"\n📆 {date}:")
        for i, task in enumerate(tasks[date], 1):
            print(f"  {i}. {task}")
