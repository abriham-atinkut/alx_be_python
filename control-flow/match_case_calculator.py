num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if num2 == 0 and operation == "/":
    print("Cannot divide by zero.")
else:
    match operation:
        case "+":
            addition = num1 + num2
            print(f"The result is {addition}.")
        case "-":
            subtract = num1 - num2
            print(f"The result is {subtract}.")
        case "*":
            multiply  = num1 * num2
            print(f"The result is {multiply}.")
        case "/":
            divide  = num1 / num2
            print(f"The result is {divide}.")
        case _:
            print("Please Enter valid operation")

