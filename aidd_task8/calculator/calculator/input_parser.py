def get_numerical_input(prompt_message):
    while True:
        user_input = input(prompt_message)
        if user_input.lower() == 'q':
            return 'q'
        try:
            return float(user_input)
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

def get_operator_input(prompt_message):
    while True:
        operator = input(prompt_message)
        if operator.lower() == 'q':
            return 'q'
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Error: Invalid operator. Please use +, -, *, or /.")
