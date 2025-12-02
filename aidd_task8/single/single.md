# Simple Python CLI Calculator — Project Specification (single.md)

## 1️⃣ /constitution Output

The project constitution has been initialized to version 0.1.0, reflecting the initial principles and governance for the Simple Python CLI Calculator. No manual follow-up is required for other files. Suggested commit message: docs: initialize constitution to v0.1.0 (new project principles + governance)

Impact: Constitution file created and updated with project principles.

Reflection: The constitution was successfully created based on user input, defining the core principles and constraints for the CLI calculator project.

## 2. /specify output

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

## 3. /plan output

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

## 4. /tasks output

# Tasks: Python CLI Calculator

**Input**: Design documents from `/specs/1-cli-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create `calculator/` directory
- [ ] T002 Create `calculator/main.py`
- [ ] T003 Create `calculator/operations.py`
- [ ] T004 Create `calculator/input_parser.py`
- [ ] T005 Create `calculator/tests/` directory
- [ ] T006 Create `calculator/tests/unit_tests.py`
- [ ] T007 Create `calculator/tests/integration_tests.py`

---

## Phase 2: Foundational (Input Parsing and Validation)

**Purpose**: Implement and test core input handling components.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T008 Implement `get_numerical_input(prompt_message)` function in `calculator/input_parser.py`
- [ ] T009 [P] Implement `get_operator_input(prompt_message)` function in `calculator/input_parser.py`
- [ ] T010 [P] Write unit tests for `get_numerical_input` in `calculator/tests/unit_tests.py`
- [ ] T011 [P] Write unit tests for `get_operator_input` in `calculator/tests/unit_tests.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Perform Basic Addition (Priority: P1) 🎯 MVP

**Goal**: The user can successfully add two numbers and see the correct sum.

**Independent Test**: Provide two numbers and the '+ ' operator, then verify the output is the correct sum.

### Tests for User Story 1
- [ ] T012 [P] [US1] Write unit tests for `add` function in `calculator/tests/unit_tests.py`

### Implementation for User Story 1
- [ ] T013 [US1] Implement `add(num1, num2)` function in `calculator/operations.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Perform Basic Subtraction (Priority: P1)

**Goal**: The user can successfully subtract one number from another and see the correct difference.

**Independent Test**: Provide two numbers and the '-' operator, then verify the output is the correct difference.

### Tests for User Story 2
- [ ] T014 [P] [US2] Write unit tests for `subtract` function in `calculator/tests/unit_tests.py`

### Implementation for User Story 2
- [ ] T015 [US2] Implement `subtract(num1, num2)` function in `calculator/operations.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Perform Basic Multiplication (Priority: P1)

**Goal**: The user can successfully multiply two numbers and see the correct product.

**Independent Test**: Provide two numbers and the '*' operator, then verify the output is the correct product.

### Tests for User Story 3
- [ ] T016 [P] [US3] Write unit tests for `multiply` function in `calculator/tests/unit_tests.py`

### Implementation for User Story 3
- [ ] T017 [US3] Implement `multiply(num1, num2)` function in `calculator/operations.py`

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Perform Basic Division (Priority: P1)

**Goal**: The user can successfully divide one number by another and see the correct quotient.

**Independent Test**: Provide two numbers and the '/' operator, then verify the output is the correct quotient.

### Tests for User Story 4
- [ ] T018 [P] [US4] Write unit tests for `divide` function (excluding zero division) in `calculator/tests/unit_tests.py`

### Implementation for User Story 4
- [ ] T019 [US4] Implement `divide(num1, num2)` function (without zero division handling) in `calculator/operations.py`

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Handle Division by Zero (Priority: P1)

**Goal**: The user is informed with an error message when attempting to divide by zero.

**Independent Test**: Provide a number, the '/' operator, and zero, then verify the error message "Error: Division by zero is not allowed."

### Tests for User Story 5
- [ ] T020 [P] [US5] Write unit tests for division by zero handling in `calculator/tests/unit_tests.py`

### Implementation for User Story 5
- [ ] T021 [US5] Modify `divide` function in `calculator/operations.py` to raise `ZeroDivisionError`
- [ ] T022 [US5] Implement `perform_calculation(num1, num2, operator)` function in `calculator/operations.py` to handle `ZeroDivisionError` and dispatch operations

**Checkpoint**: Division by zero is now handled gracefully.

---

## Phase 8: Main Application Logic and Integration (P1/P2)

**Goal**: The full CLI calculator application can run, accept inputs, perform operations, and display results/errors.

**Independent Test**: Run the `main.py` script and interact with it to perform various valid and invalid operations, verifying correct behavior and error messages.

### Implementation for Main Application Logic
- [ ] T023 Implement `main()` function in `calculator/main.py` to orchestrate input, calculation, and output.
- [ ] T024 Add welcome message and exit condition (e.g., 'q' to quit) to `calculator/main.py`.

### Integration Tests
- [ ] T025 Write integration tests for basic addition in `calculator/tests/integration_tests.py`
- [ ] T026 [P] Write integration tests for basic subtraction in `calculator/tests/integration_tests.py`
- [ ] T027 [P] Write integration tests for basic multiplication in `calculator/tests/integration_tests.py`
- [ ] T028 [P] Write integration tests for basic division in `calculator/tests/integration_tests.py`
- [ ] T029 [P] Write integration tests for division by zero in `calculator/tests/integration_tests.py`
- [ ] T030 [P] Write integration tests for invalid numerical input in `calculator/tests/integration_tests.py`
- [ ] T031 [P] Write integration tests for invalid operator input in `calculator/tests/integration_tests.py`

**Checkpoint**: The full calculator application is functional and integrated.

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements and quality assurance.

- [ ] T032 Refine output messages and prompts for user-friendliness across `main.py` and `input_parser.py`
- [ ] T033 Ensure all Python code adheres to PEP 8 style guidelines across all `.py` files

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-8)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Stories 1-5 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories for their core logic.
- **User Stories 6-7 (P2)**: Handled within Foundational and Main Application phases, so no separate story dependencies.

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Logic implementation before integration (e.g., `divide` before `perform_calculation`)

### Parallel Opportunities

- All Setup tasks T002-T007 can run in parallel (creating files/directories).
- Tasks T009, T010, T011 can run in parallel within the Foundational phase.
- Unit test tasks (e.g., T012, T014, T016, T018, T020) can be run in parallel with each other.
- Integration test tasks (T026-T031) can run in parallel.
- Different user stories (Phases 3-7) can be worked on in parallel by different team members once Foundational phase is complete.

---

## Parallel Example: Foundational (Input Parsing)

```bash
# Launch input parser implementation in parallel:
Task: "Implement get_numerical_input(prompt_message) function in calculator/input_parser.py"
Task: "Implement get_operator_input(prompt_message) function in calculator/input_parser.py"

# Launch unit tests for input parser in parallel:
Task: "Write unit tests for get_numerical_input in calculator/tests/unit_tests.py"
Task: "Write unit tests for get_operator_input in calculator/tests/unit_tests.py"
```

---

## Parallel Example: User Stories (after Foundational)

```bash
# Developer A works on Addition:
Task: "Implement add(num1, num2) function in calculator/operations.py"
Task: "Write unit tests for add function in calculator/tests/unit_tests.py"

# Developer B works on Subtraction:
Task: "Implement subtract(num1, num2) function in calculator/operations.py"
Task: "Write unit tests for subtract function in calculator/tests/unit_tests.py"
```

---

## Implementation Strategy

### MVP First (Phases 1-3)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Addition)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (Addition) → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 (Subtraction) → Test independently → Deploy/Demo
4. Continue with other arithmetic operations and error handling in sequence, testing each incrementally.

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together.
2. Once Foundational is done:
   - Developer A: User Story 1 (Addition) and User Story 3 (Multiplication)
   - Developer B: User Story 2 (Subtraction) and User Story 4 (Division)
   - Developer C: User Story 5 (Division by Zero) and Main Application Logic/Integration
3. Stories complete and integrate independently.

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

## 5. /implement output






