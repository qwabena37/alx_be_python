num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input('Choose the operation (+, -, *, /): ' )
match operation:
    case "+":
        result = num1+num2
        print(f"The result is {result}") 
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1*num2
        print(f"The result is {result}")
    case "/":
        result = num1/num2
        print(f"The result is {result}")
    case "dividing(/) by 0":
        if num2 == 0 and operation == '/':
            print("Cannot divide by zero.")
    case _:
        print("input numbers.")