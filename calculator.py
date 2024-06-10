# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation."

# Main function to run the calculator
def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()
            
            result = calculate(num1, num2, operation)
            print(f"The result is: {result}")

            cont = input("Do you want to perform another calculation? (yes/no): ").lower()
            if cont != 'yes':
                print("Thanks for using the calculator!")
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Start the calculator
calculator()
