# task_reminder.py

def main():
    print("=== Task Reminder ===")
    print("Choose your priority task for today:")
    print("1. Complete project")
    print("2. Collaborate with other developers")
    print("3. Call a friend")

    choice = input("Enter 1, 2, or 3: ")

    # Match case to decide task
    match choice:
        case "1":
            task = "Complete project"
            urgency = "high"
        case "2":
            task = "Collaborate with other developers"
            urgency = "medium"
        case "3":
            task = "Call a friend"
            urgency = "low"
        case _:
            print("Invalid choice. Exiting.")
            return

    print(f"\nYour task for today: {task} (Urgency: {urgency.upper()})\n")

    # Loop to remind user based on urgency
    reminders = 0
    while reminders < 3:
        if urgency == "high":
            print(f"⚠️ Reminder {reminders+1}: Don't forget to {task} ASAP!")
        elif urgency == "medium":
            print(f"🔔 Reminder {reminders+1}: Try to {task} today.")
        else:
            print(f"😊 Reminder {reminders+1}: Remember to {task} when you can.")
        
        reminders += 1

if __name__ == "__main__":
    main()
