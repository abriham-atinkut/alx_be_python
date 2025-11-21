def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Zero can't divide!"
            elif num2 != 0:
                return num1 / num2
        case _:
            return "Sorry something goes wrong!"
