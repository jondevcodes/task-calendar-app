# task_manager.py
from datetime import datetime

task_calendar = {}

def add_task(task, date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return False, "❌ Invalid date format. Use YYYY-MM-DD."

    if date not in task_calendar:
        task_calendar[date] = []

    task_calendar[date].append(task)
    return True, f"✅ Task added for {date}: {task}"

def get_tasks():
    return task_calendar

def set_tasks(data):
    global task_calendar
    task_calendar = data
