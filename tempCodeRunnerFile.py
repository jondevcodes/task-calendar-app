import json
from datetime import datetime, date

class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def __repr__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} {self.name}"

class TaskTracker:
    def __init__(self, data_file="tasks.json"):
        self.data_file = data_file
        self.task_calendar = {}

    def add_task(self, task_name, date_str):
        try:
            due_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.")
            return

        task = Task(task_name)
        if due_date not in self.task_calendar:
            self.task_calendar[due_date] = []
        self.task_calendar[due_date].append(task)
        self.save_tasks()
        print(f"✅ Task added for {due_date}: {task.name}")

    def view_tasks(self):
        if not self.task_calendar:
            print("📭 No tasks scheduled.")
            return

        print("\n🗓️ Your Task Calendar:")
        for d in sorted(self.task_calendar):
            print(f"\n📆 {d}:")
            for i, task in enumerate(self.task_calendar[d], 1):
                print(f"  {i}. {task}")

    def save_tasks(self):
        raw_data = {
            str(d): [task.__dict__ for task in tasks]
            for d, tasks in self.task_calendar.items()
        }
        with open(self.data_file, "w") as f:
            json.dump(raw_data, f)

    def load_tasks(self):
        try:
            with open(self.data_file, "r") as f:
                raw_data = json.load(f)
            for d, tasks in raw_data.items():
                date_obj = datetime.strptime(d, "%Y-%m-%d").date()
                self.task_calendar[date_obj] = [Task(**t) for t in tasks]
        except FileNotFoundError:
            pass

def show_menu():
    print("\n📅 Task Calendar")
    print("1. Add a Task")
    print("2. View Tasks by Date")
    print("3. Exit")

if __name__ == "__main__":
    tracker = TaskTracker()
    tracker.load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1–3): ")

        if choice == "1":
            task = input("Enter your task: ")
            date_str = input("Enter the due date (YYYY-MM-DD): ")
            tracker.add_task(task, date_str)
        elif choice == "2":
            tracker.view_tasks()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid option. Please choose 1, 2, or 3.")
