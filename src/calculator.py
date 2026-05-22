"""
Simple Calculator Module

This module provides basic arithmetic operations.
"""


class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    def add(self, a, b):
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
        """
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        return a * b
    
    def divide(self, a, b):
        """Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            Quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        """Raise a to the power of b.
        
        Args:
            a: Base number
            b: Exponent
            
        Returns:
            a raised to the power of b
        """
        return a ** b
    
    def modulo(self, a, b):
        """Calculate the remainder of a divided by b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Remainder of a divided by b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot perform modulo with zero")
        return a % b


def main():
    """Main function to demonstrate calculator usage."""
    calc = Calculator()
    
    print("Simple Calculator Demo")
    print("=" * 40)
    
    # Addition
    result = calc.add(10, 5)
    print(f"10 + 5 = {result}")
    
    # Subtraction
    result = calc.subtract(10, 5)
    print(f"10 - 5 = {result}")
    
    # Multiplication
    result = calc.multiply(10, 5)
    print(f"10 * 5 = {result}")
    
    # Division
    result = calc.divide(10, 5)
    print(f"10 / 5 = {result}")
    
    # Power
    result = calc.power(2, 3)
    print(f"2 ^ 3 = {result}")
    
    # Modulo
    result = calc.modulo(10, 3)
    print(f"10 % 3 = {result}")
    
    # Error handling example
    print("\nError Handling Demo:")
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

# Made with Bob
