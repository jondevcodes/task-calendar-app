from datetime import datetime
import json
import os

task_calendar = {}
DATA_FILE = "tasks.json"

def load_tasks():
    global task_calendar
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            raw_data = json.load(f)
            # Convert date strings back into datetime.date objects
            task_calendar = {
                datetime.strptime(date, "%Y-%m-%d").date(): tasks
                for date, tasks in raw_data.items()
            }

def save_tasks():
    with open(DATA_FILE, "w") as f:
        json.dump({str(date): tasks for date, tasks in task_calendar.items()}, f)

def show_menu():
    print("\n📅 Task Calendar")
    print("1. Add a Task")
    print("2. View Tasks by Date")
    print("3. Exit")

def add_task():
    task = input("Enter your task: ")
    date_str = input("Enter the due date (YYYY-MM-DD): ")

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")
        return

    if date not in task_calendar:
        task_calendar[date] = []

    task_calendar[date].append(task)
    save_tasks()
    print(f"✅ Task added for {date}: {task}")

def view_tasks():
    if not task_calendar:
        print("📭 No tasks scheduled.")
        return

    print("\n🗓️ Your Task Calendar:")
    for date in sorted(task_calendar):
        print(f"\n📆 {date}:")
        for i, task in enumerate(task_calendar[date], 1):
            print(f"  {i}. {task}")

# Load existing tasks when the app starts
load_tasks()

# App loop
while True:
    show_menu()
    choice = input("Choose an option (1–3): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("❗ Invalid option. Please choose 1, 2, or 3.")
