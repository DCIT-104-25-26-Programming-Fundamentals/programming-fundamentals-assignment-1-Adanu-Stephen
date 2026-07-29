# ===============================================
# PROGRAMMING FUNDAMENTALS - Assignment 9
# Console-Based Simple Calculator
# ===============================================

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def exponentiation(a, b):
    return a ** b


def menu():
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


while True:
    menu()

    choice = input("Select an operation (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice. Please select a number from 1 to 7.")
        continue

    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    if choice == "1":
        result = addition(first, second)
        print(f"Result: {first} + {second} = {result}")

    elif choice == "2":
        result = subtraction(first, second)
        print(f"Result: {first} - {second} = {result}")

    elif choice == "3":
        result = multiplication(first, second)
        print(f"Result: {first} * {second} = {result}")

    elif choice == "4":
        result = division(first, second)

        if result is None:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Result: {first} / {second} = {result:.2f}")

    elif choice == "5":
        result = modulus(first, second)

        if result is None:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Result: {first} % {second} = {result}")

    elif choice == "6":
        result = exponentiation(first, second)
        print(f"Result: {first} ** {second} = {result}")