def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return num1 / num2

def perform_calculation(num1, num2, operator):
    try:
        if operator == '+':
            return add(num1, num2)
        elif operator == '-':
            return subtract(num1, num2)
        elif operator == '*':
            return multiply(num1, num2)
        elif operator == '/':
            return divide(num1, num2)
        else:
            return "Error: Invalid operator."
    except ZeroDivisionError as e:
        return f"Error: {e}"
