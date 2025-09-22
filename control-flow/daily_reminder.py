# task_reminder.py

def main():
    print("=== Task Reminder ===")
    print("Choose your priority task for today:")
    print("1. Complete project")
    print("2. Collaborate with other developers")
    print("3. Call a friend")

    task = input("Enter your task: ")
    priority = input("Priority(high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")
   

    # Match case to decide task
    match priority:
        case "1":
            task = "Complete project"
            priority = "high"
            time_bound = "yes"
        case "2":
            task = "Collaborate with other developers"
            priority = "medium"
            time_bound = "no"
        case "3":
            task = "Call a friend"
            priority = "low"
            time_bound = "no"
        case _:
            print("Invalid choice. Exiting.")
            return

    # Loop to remind user based on urgency
    reminders = 0
    while reminders < 3:
        if time_bound == "yes":
            print(f"⚠️ Reminder {reminders+1}: Finish {task} it's a high priority task that requires immediate attention today!")
        else:
            print(f"🔔 Reminder {reminders+1}: Try to {task} at your free time.")
        
if __name__ == "__main__":
    main()
