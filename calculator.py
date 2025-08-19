# Step 1: Define operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

# Step 2: Map operations to functions
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

# Step 3 & 4: Get input and perform calculation
try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation in operations:
        result = operations[operation](first_number, second_number)
        print(f"The result of {first_number} {operation} {second_number} is {result}")
    else:
        print("Invalid operation. Please select from +, -, *, /.")

except ValueError as e:
    print("Error:", e)
from +, -, *, /.")
