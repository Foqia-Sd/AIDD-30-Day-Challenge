from calculator.input_parser import get_numerical_input, get_operator_input
from calculator.operations import perform_calculation

def main():
    print("Welcome to the Simple CLI Calculator!")
    print("Enter 'q' at any time to quit.")

    while True:
        num1_input = get_numerical_input("Enter the first number: ")
        if num1_input == 'q':
            break

        operator = get_operator_input("Enter the operator (+, -, *, /): ")
        if operator == 'q':
            break

        num2_input = get_numerical_input("Enter the second number: ")
        if num2_input == 'q':
            break

        result = perform_calculation(num1_input, num2_input, operator)
        print(f"Result: {result}")
        print("\n")

if __name__ == "__main__":
    main()
