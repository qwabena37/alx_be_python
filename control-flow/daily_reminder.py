# task_reminder.py

def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    print("\n=== Task Reminder ===")

    # Process task based on priority
    match priority:
        case "high":
            reminder = f"⚠️ HIGH PRIORITY: {task}"
        case "medium":
            reminder = f"🔔 MEDIUM PRIORITY: {task}"
        case "low":
            reminder = f"😊 LOW PRIORITY: {task}"
        case _:
            reminder = f"❓ UNKNOWN PRIORITY: {task}"

    # Modify reminder if time-bound
    if time_bound == "yes":
        reminder += " — that requires immediate attention today!"

    # Provide customized reminder
    print('Reminder: ' + reminder) 


if __name__ == "__main__":
    main()
