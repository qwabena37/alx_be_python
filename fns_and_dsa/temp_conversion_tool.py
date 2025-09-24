# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit → Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius → Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program
if __name__ == "__main__":
    try:
        # Ask user for input
        temp_str = input("Enter the temperature to convert: ")
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Check if input is numeric
        if not temp_str.replace(".", "", 1).lstrip("-").isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temperature = float(temp_str)

        # Decide which conversion to apply
        if unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature:.2f}°C is {result:.2f}°F")
        elif unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature:.2f}°F is {result:.2f}°C")
        else:
            raise ValueError("Invalid temperature. Please enter a numeric value.")

    except ValueError as e:
        print(e)
