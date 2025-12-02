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
