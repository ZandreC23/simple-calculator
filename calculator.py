#!/usr/bin/env python3
"""
Simple Calculator Program
A calculator that evaluates mathematical expressions
"""

def main():
    print("=" * 50)
    print("           SIMPLE CALCULATOR")
    print("=" * 50)
    print("Enter expressions like: 5 + 3, 10 * 4, 15 / 3, etc.")
    print("Type 'exit' or 'quit' to close the calculator")
    print("=" * 50)
    
    while True:
        try:
            # Get expression from user
            expression = input("\nEnter calculation: ").strip()
            
            # Check if user wants to exit
            if expression.lower() in ['exit', 'quit', 'q']:
                print("\nGoodbye!")
                break
            
            # Skip empty input
            if not expression:
                continue
            
            # Evaluate the expression
            result = eval(expression)
            print(f"Result: {result}")
            
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        except Exception as e:
            print(f"Error: Invalid expression. Please use format: number operator number")

if __name__ == "__main__":
    main()