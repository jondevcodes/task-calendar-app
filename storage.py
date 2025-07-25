# storage.py
import json
import os
from datetime import datetime
from task_manager import set_tasks, get_tasks

DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            raw_data = json.load(f)
            task_data = {
                datetime.strptime(date, "%Y-%m-%d").date(): tasks
                for date, tasks in raw_data.items()
            }
            set_tasks(task_data)

def save_tasks():
    with open(DATA_FILE, "w") as f:
        json.dump(
            {str(date): tasks for date, tasks in get_tasks().items()},
            f
        )
