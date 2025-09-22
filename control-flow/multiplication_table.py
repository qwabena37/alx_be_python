
def main():
    try:
        # Ask the user to enter a number
        number = int(input("Enter a number to display its multiplication table: "))

        print(f"\nMultiplication Table for {number}:\n")
        # Loop from 1 to 10
        for i in range(1, 11):
            result = number * i
            print(f"{number} x {i} = {result}")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
