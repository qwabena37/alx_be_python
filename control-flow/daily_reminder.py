# priority_task_reminder.py
import time

def main():
    print("=== Priority Task Reminder ===")
    print("Choose your priority task for today:")
    print("1. Complete Weekly Milestone")
    print("2. Collaborate with other developers")
    print("3. Go fishing")

    task = input("Enter your task: ")

    # Match Case: pick task
    match priority:
        case "1":
            task = "Complete Weekly Milestone"
            priority = 'high'
        case "2":
            task = "Collaborate with other developers"
            priority = 'medium'
        case "3":
            task = "Go fishing"
            priority = 'low'
        case _:
            print("Invalid priority. Exiting.")
            return

    # Ask about priority (just for display)
    priority = input("Priority (high/medium/low): ")

    # Ask about time sensitivity (used in if loop)
    time_bound = input("Is it time-bound? (yes/no): ")

    print(f"\nYour task for today: {task}")
    print(f"Priority: {priority.upper()}")
    print(f"Time-bound: {time_bound.upper()}\n")

    reminders = 0
    while reminders < 3:
        if time_bound == "yes":
            print(f"⏰ Reminder {reminders+1}: {task} MUST be done soon!")
            time.sleep(2)  # frequent reminders
        else:
            print(f"😊 Reminder {reminders+1}: Don't forget to {task} today.")
            time.sleep(5)  # relaxed reminders
        reminders += 1

    print("\n✅ All reminders sent. Stay productive!")

if __name__ == "__main__":
    main()
