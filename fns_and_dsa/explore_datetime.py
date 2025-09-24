from datetime import datetime, timedelta

# Function to display current date and time
def display_current_datetime():
    current_date = datetime.now()  # Save current datetime
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

# Function to calculate future date
def calculate_future_date(current_date, days):
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

# Main Program
if __name__ == "__main__":
    # Show current datetime
    current_date = display_current_datetime()

    # Ask user for input
    days = int(input("Enter number of days to add: "))

    # Calculate and display future date
    calculate_future_date(current_date, days)
