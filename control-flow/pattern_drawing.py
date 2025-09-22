# pattern_drawing.py

def main():
    try:
        # Ask the user for a positive integer
        size = int(input("Enter the size of the pattern: "))

        if size <= 0:
            print("Please enter a positive integer greater than zero.")
            return

        print(f"\nSquare pattern of size {size}:\n")

        # Outer loop for rows
        i = 0
        while i < size:
            j = 0
            # Inner loop for columns
            while j < size:
                print("*", end=" ")
                j += 1
            print()  # Move to the next line after each row
            i += 1

    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
