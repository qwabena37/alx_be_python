
def main():
    try:
        # Ask the user for a positive integer
        size = int(input("Enter a positive integer for the square size: "))

        if size <= 0:
            print("Please enter a positive integer greater than zero.")
            return

        print(f"\nSquare pattern of size {size}:\n")
        
        # Nested loops to draw the square
        for i in range(size):
            for j in range(size):
                print("*", end=" ")
            print()  # Move to the next line after each row

    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
