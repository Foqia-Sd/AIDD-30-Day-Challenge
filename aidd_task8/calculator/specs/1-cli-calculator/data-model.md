# Data Model: Python CLI Calculator

## Entities

### Number
- **Description**: A numerical value entered by the user.
- **Type**: Float (to support both integers and decimals).
- **Validation**: Must be a valid numerical string convertible to float.

### Operator
- **Description**: A character representing the arithmetic operation.
- **Type**: String.
- **Validation**: Must be one of: "+", "-", "*", "/".

### Result
- **Description**: The numerical outcome of a successful arithmetic operation.
- **Type**: Float.

### Error Message
- **Description**: A string providing feedback to the user in case of invalid input or an impossible operation (e.g., division by zero).
- **Type**: String.
