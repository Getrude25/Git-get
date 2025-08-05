num1 = 10
num2 = 5
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    result = "Invalid operation"
print(f"The result of {num1} {operation} {num2} is: {result}")
# Output: The result of 10 + 5 is: 15