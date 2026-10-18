print("=" * 40)
print("       SIMPLE PYTHON CALCULATOR")
print("=" * 40)

def calculate(a, b, choice):

    if choice == "1":
        return add(a, b)

    elif choice == "2":
        return subtract(a, b)

    elif choice == "3":
        return multiply(a, b)

    elif choice == "4":

        if b == 0:
            return "Cannot divide by zero"

        return divide(a, b)

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice: ")

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

result = calculate(num1, num2, choice)
print(f"Result: {result}")

