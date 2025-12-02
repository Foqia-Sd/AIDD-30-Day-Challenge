# Implementation Plan: Python CLI Calculator

**Branch**: `1-cli-calculator` | **Date**: 2025-12-02 | **Spec**: [specs/1-cli-calculator/spec.md](specs/1-cli-calculator/spec.md)
**Input**: Feature specification from `/specs/1-cli-calculator/spec.md`

## Summary

This plan outlines the implementation of a simple Python CLI calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division). The technical approach focuses on a modular design, clear input/output handling, and robust error management for invalid inputs and division by zero scenarios, adhering to simplicity and readability principles.

## Technical Context

**Language/Version**: Python 3.x (latest stable version, e.g., 3.10+)
**Primary Dependencies**: None (using Python built-in functions)
**Storage**: N/A
**Testing**: `pytest` for unit and integration tests.
**Target Platform**: Any system with Python 3.x installed (CLI-based).
**Project Type**: Single CLI application.
**Performance Goals**: Instantaneous response for basic operations; minimal resource usage.
**Constraints**: No GUI, only CLI; basic arithmetic operations only; no external libraries for core logic.
**Scale/Scope**: Single-user CLI tool for fundamental calculations.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Simplicity and Readability**: The plan prioritizes a clean, modular structure with clear function responsibilities and explicit error handling, making it beginner-friendly and readable. **(PASS)**
- **II. Command-Line Interface (CLI) Focus**: The design is strictly CLI-based, with no plans for a GUI. **(PASS)**
- **III. Core Arithmetic Functionality**: The plan directly addresses the implementation of addition, subtraction, multiplication, and division, ensuring accurate numerical handling. **(PASS)**
- **IV. Clear Input and Output**: The plan includes dedicated components for input parsing, validation, and formatted output, including specific error messages. **(PASS)**
- **V. Beginner-Friendly Development**: The modular design, clear function definitions, and adherence to Python best practices (PEP 8) support easy understanding and extension for new developers. **(PASS)**

## Project Structure

### Documentation (this feature)

```text
specs/1-cli-calculator/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command) - N/A for this feature
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command) - N/A for this feature
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
calculator/
├── main.py              # Main entry point for CLI application
├── operations.py        # Contains arithmetic functions
├── input_parser.py      # Handles user input and validation
└── tests/
    ├── unit_tests.py    # Unit tests for operations and input parsing
    └── integration_tests.py # Integration tests for overall program flow
```

**Structure Decision**: A single project structure is selected, organized into `main.py` for program flow, `operations.py` for arithmetic logic, `input_parser.py` for input handling and validation, and a `tests/` directory for comprehensive testing. This aligns with the simplicity principle and modular design.

## Detailed Implementation Steps

### Phase 0: Research (N/A for this feature)

No specific research phase is required as the requirements are straightforward and align with Python's built-in capabilities and the project's simplicity constraints.

### Phase 1: Design & Contracts

#### 1. Data Model (`data-model.md`)

- **Input Numbers**: Two numerical values (floats) from user input.
- **Operator**: A string representing the arithmetic operation (+, -, *, /).
- **Result**: A numerical value (float) representing the outcome of the operation.
- **Error Message**: A string for user feedback on invalid inputs or operations.

#### 2. Function Structure and Program Flow

- **`main.py`**
    - **`main()` function**: The entry point of the application.
        - Orchestrates the program flow: display prompt, get input, perform calculation, display output.
        - Calls `get_numerical_input()` from `input_parser.py` twice.
        - Calls `get_operator_input()` from `input_parser.py` once.
        - Calls `perform_calculation()` from `operations.py`.
        - Prints the result or error message.

- **`operations.py`**
    - **`add(num1, num2)`**: Returns `num1 + num2`.
    - **`subtract(num1, num2)`**: Returns `num1 - num2`.
    - **`multiply(num1, num2)`**: Returns `num1 * num2`.
    - **`divide(num1, num2)`**: Returns `num1 / num2`. Includes `ZeroDivisionError` handling.
    - **`perform_calculation(num1, num2, operator)`**: Acts as a dispatcher.
        - Takes two numbers and an operator.
        - Uses conditional logic (if/elif/else) to call the appropriate arithmetic function.
        - Handles `ZeroDivisionError` specifically for division.
        - Returns the result or an error string.

- **`input_parser.py`**
    - **`get_numerical_input(prompt_message)`**: Prompts the user for a number.
        - Continuously prompts until valid float input is received.
        - Handles `ValueError` for non-numerical input.
        - Returns the validated float.
    - **`get_operator_input(prompt_message)`**: Prompts the user for an operator.
        - Continuously prompts until a valid operator (+, -, *, /) is received.
        - Returns the validated operator string.

#### 3. Data Flow

1.  `main.py` prompts for `num1` → `input_parser.py.get_numerical_input()` reads and validates.
2.  `main.py` prompts for `operator` → `input_parser.py.get_operator_input()` reads and validates.
3.  `main.py` prompts for `num2` → `input_parser.py.get_numerical_input()` reads and validates.
4.  `main.py` passes `num1`, `num2`, `operator` to `operations.py.perform_calculation()`.
5.  `perform_calculation()` dispatches to relevant arithmetic function.
6.  Arithmetic function returns result or raises error.
7.  `perform_calculation()` returns result or error string to `main.py`.
8.  `main.py` prints the final result or error message to the console.

#### 4. Error Handling Strategy

- **Invalid Numerical Input**: Handled in `input_parser.py`'s `get_numerical_input` using a `try-except ValueError` block. User is re-prompted until valid input.
- **Invalid Operator Input**: Handled in `input_parser.py`'s `get_operator_input` by checking if the input operator is one of the allowed characters. User is re-prompted.
- **Division by Zero**: Handled in `operations.py`'s `divide` function (by raising `ZeroDivisionError`) and caught in `perform_calculation`. An appropriate error string is returned.

#### 5. Quickstart Guide (`quickstart.md`)

Will provide instructions on how to run the calculator: clone repo, navigate to directory, and execute `python main.py`.

#### 6. Contracts (`contracts/`) - N/A for this feature

This is a standalone CLI application with no external APIs or contracts required.

## Complexity Tracking

No constitution violations, so this section is not applicable.
