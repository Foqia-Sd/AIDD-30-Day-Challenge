# Feature Specification: Python CLI Calculator

**Feature Branch**: `1-cli-calculator`
**Created**: 2025-12-02
**Status**: Draft
**Input**: User description: "Specify the full requirements for a Python CLI calculator. It must support:
- addition
- subtraction
- multiplication
- division
Inputs: two numbers, and an operator.
Outputs: numerical result.
If division by zero happens, show an error message.
The calculator should run in the terminal and handle invalid input gracefully.
Make the specification detailed, including features, constraints, edge cases, and test cases."

## User Scenarios & Testing

### User Story 1 - Perform Basic Addition (Priority: P1)

The user wants to add two numbers and see the correct sum.

**Why this priority**: Addition is a fundamental arithmetic operation and a primary function of a calculator.

**Independent Test**: Can be fully tested by providing two numbers and the '+ ' operator, then verifying the output.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** the user inputs "5", then "+", then "3", **Then** the calculator outputs "8".
2. **Given** the calculator is running, **When** the user inputs "10.5", then "+", then "2.5", **Then** the calculator outputs "13.0".

---

### User Story 2 - Perform Basic Subtraction (Priority: P1)

The user wants to subtract one number from another and see the correct difference.

**Why this priority**: Subtraction is a fundamental arithmetic operation.

**Independent Test**: Can be fully tested by providing two numbers and the '-' operator, then verifying the output.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** the user inputs "10", then "-", then "4", **Then** the calculator outputs "6".
2. **Given** the calculator is running, **When** the user inputs "7.0", then "-", then "9.5", **Then** the calculator outputs "-2.5".

---

### User Story 3 - Perform Basic Multiplication (Priority: P1)

The user wants to multiply two numbers and see the correct product.

**Why this priority**: Multiplication is a fundamental arithmetic operation.

**Independent Test**: Can be fully tested by providing two numbers and the '*' operator, then verifying the output.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** the user inputs "6", then "*", then "7", **Then** the calculator outputs "42".
2. **Given** the calculator is running, **When** the user inputs "2.5", then "*", then "4", **Then** the calculator outputs "10.0".

---

### User Story 4 - Perform Basic Division (Priority: P1)

The user wants to divide one number by another and see the correct quotient.

**Why this priority**: Division is a fundamental arithmetic operation.

**Independent Test**: Can be fully tested by providing two numbers and the '/' operator, then verifying the output.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** the user inputs "10", then "/", then "2", **Then** the calculator outputs "5.0".
2. **Given** the calculator is running, **When** the user inputs "7", then "/", then "2", **Then** the calculator outputs "3.5".

---

### User Story 5 - Handle Division by Zero (Priority: P1)

The user wants to be informed with an error message when attempting to divide by zero.

**Why this priority**: Prevents application crash and provides clear feedback for an invalid operation.

**Independent Test**: Can be fully tested by providing a number, the '/' operator, and zero, then verifying the error message.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** the user inputs "10", then "/", then "0", **Then** the calculator outputs "Error: Division by zero is not allowed."

---

### User Story 6 - Handle Invalid Numerical Input (Priority: P2)

The user wants clear feedback if they enter non-numeric input when numbers are expected.

**Why this priority**: Improves user experience by gracefully handling incorrect input.

**Independent Test**: Can be fully tested by entering non-numeric characters for numbers and verifying the error message.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** the user inputs "abc" for a number, **Then** the calculator outputs "Error: Invalid input. Please enter a number."

---

### User Story 7 - Handle Invalid Operator Input (Priority: P2)

The user wants clear feedback if they enter an unsupported operator.

**Why this priority**: Improves user experience by gracefully handling incorrect input.

**Independent Test**: Can be fully tested by entering an unsupported operator and verifying the error message.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** the user inputs "5", then "&", then "3", **Then** the calculator outputs "Error: Invalid operator. Please use +, -, *, or /."

---

### Edge Cases

- Large numbers: The calculator should handle numbers within Python's standard float/integer limits correctly.
- Negative numbers: Arithmetic operations should be performed correctly with negative numbers.
- Decimal numbers: Arithmetic operations should be performed correctly with decimal numbers, and results should maintain appropriate precision.

## Requirements

### Functional Requirements

- **FR-001**: System MUST accept two numerical inputs from the user.
- **FR-002**: System MUST accept one of four operators: '+', '-', '* ', '/'.
- **FR-003**: System MUST perform addition of the two numbers when '+' is selected.
- **FR-004**: System MUST perform subtraction of the second number from the first when '-' is selected.
- **FR-005**: System MUST perform multiplication of the two numbers when '*' is selected.
- **FR-006**: System MUST perform division of the first number by the second when '/' is selected.
- **FR-007**: System MUST display an error message if division by zero is attempted.
- **FR-008**: System MUST display an error message for invalid non-numerical input.
- **FR-009**: System MUST display an error message for invalid operators.
- **FR-010**: System MUST output the numerical result of the operation.
- **FR-011**: System MUST run as a command-line application.

### Key Entities

- **Number**: A numerical value provided by the user (integer or float).
- **Operator**: A character representing an arithmetic operation (+, -, *, /).
- **Result**: The numerical outcome of an arithmetic operation.

## Success Criteria

### Measurable Outcomes

- **SC-001**: The calculator successfully performs all four basic arithmetic operations (addition, subtraction, multiplication, division) for valid inputs 100% of the time.
- **SC-002**: The calculator correctly identifies and provides an error message for division by zero scenarios 100% of the time.
- **SC-003**: The calculator gracefully handles and provides appropriate error messages for invalid numerical and operator inputs 100% of the time.
- **SC-004**: Users can successfully perform a calculation and view the result in the terminal without encountering unhandled errors.
