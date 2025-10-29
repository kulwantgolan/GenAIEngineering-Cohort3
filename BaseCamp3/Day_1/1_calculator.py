# calculator.py
# A simple calculator with add and subtract functions
import sys
print("Simple Calculator")

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

print("Simple Calculator started")
# Main program
if __name__ == "__main__":  #  is a conditional check that determines if the script is being run directly (versus being imported as a module). The code inside this if block runs only in the direct execution case.
    choice = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if choice.upper() == 'ADD':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice.upper() == 'SUB':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    else:
        print("Invalid input")

print("Simple Calculator ended")
