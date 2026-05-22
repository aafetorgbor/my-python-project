# Calculator Usage Guide

## Overview

The calculator module provides a simple `Calculator` class with basic arithmetic operations.

## Features

- **Addition**: Add two numbers
- **Subtraction**: Subtract one number from another
- **Multiplication**: Multiply two numbers
- **Division**: Divide one number by another (with zero-division protection)
- **Power**: Raise a number to a power
- **Modulo**: Get the remainder of division (with zero-division protection)

## Usage

### Basic Usage

```python
from src.calculator import Calculator

# Create a calculator instance
calc = Calculator()

# Perform operations
result = calc.add(10, 5)        # 15
result = calc.subtract(10, 5)   # 5
result = calc.multiply(10, 5)   # 50
result = calc.divide(10, 5)     # 2.0
result = calc.power(2, 3)       # 8
result = calc.modulo(10, 3)     # 1
```

### Error Handling

The calculator includes error handling for invalid operations:

```python
from src.calculator import Calculator

calc = Calculator()

# Division by zero
try:
    result = calc.divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")  # Error: Cannot divide by zero

# Modulo by zero
try:
    result = calc.modulo(10, 0)
except ValueError as e:
    print(f"Error: {e}")  # Error: Cannot perform modulo with zero
```

## Running the Demo

To see the calculator in action, run:

```bash
python3 src/calculator.py
```

## Running Tests

To run the unit tests:

```bash
python3 -m unittest tests/test_calculator.py -v
```

## API Reference

### Calculator Class

#### `add(a, b)`
Returns the sum of `a` and `b`.

#### `subtract(a, b)`
Returns the difference of `a` and `b` (a - b).

#### `multiply(a, b)`
Returns the product of `a` and `b`.

#### `divide(a, b)`
Returns the quotient of `a` divided by `b`.
- **Raises**: `ValueError` if `b` is zero

#### `power(a, b)`
Returns `a` raised to the power of `b`.

#### `modulo(a, b)`
Returns the remainder of `a` divided by `b`.
- **Raises**: `ValueError` if `b` is zero