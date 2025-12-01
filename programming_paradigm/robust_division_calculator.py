def safe_divide(numerator, denominator):
    try:
        num1 = int(numerator)
        num2 = int(denominator)
        # print(num1)
        # print(num2)
        return num1 / num2
    except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    except ValueError:
            return "Error: Please enter numeric values only."
