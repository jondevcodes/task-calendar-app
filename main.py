# main.py
from cli import show_menu, handle_add_task, handle_view_tasks
from storage import load_tasks, save_tasks

load_tasks()

while True:
    show_menu()
    choice = input("Choose an option (1–3): ")

    if choice == "1":
        handle_add_task()
        save_tasks()
    elif choice == "2":
        handle_view_tasks()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("❗ Invalid option. Please choose 1, 2, or 3.")

