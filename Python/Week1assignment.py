#This is a simple calculator program that performs basic arithmetic operations.
# It prompts the user for two numbers and then calculates their sum, difference, product, and quotient.
# 🎉 lets go 🎉
num1 = float(input("Enter the first number: "))  # Input first number 
num2 = float(input("Enter the second number: "))  # Input second number
operation = input("Choose an operation (+, -, *, /): ")  # Input operation
# Perform calculations
sum_result = num1 + num2  # Addition arirhmetic
difference_result = num1 - num2  # Subtraction arithmetic
product_result = num1 * num2  # Multiplication arithmetic
quotient_result = num1 / num2  # Division arithmetic
# Display results
if operation == '+':
    print(f"Sum: {sum_result}")  # ➕
elif operation == '-':
    print(f"Difference: {difference_result}")
elif operation == '*':
    print(f"Product: {product_result}")
elif operation == '/':
    if num2 != 0:
        print(f"Quotient: {quotient_result}")
    else:
        print("Error: Division by zero.")
else:
    print("Invalid operation selected. Please choose +, -, *, or /.")
print(4+4)  
# wow, this is amazing!