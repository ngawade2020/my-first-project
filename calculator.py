import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def square_root(a):
    if a < 0:
        return "Cannot find square root of negative number"
    return math.sqrt(a)

def power(a, b):
    return a ** b


while True:

    print("\n===== PYTHON CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice in ['1', '2', '3', '4', '6']:

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))

            elif choice == '2':
                print("Result:", subtract(num1, num2))

            elif choice == '3':
                print("Result:", multiply(num1, num2))

            elif choice == '4':
                print("Result:", divide(num1, num2))

            elif choice == '6':
                print("Result:", power(num1, num2))

        elif choice == '5':

            num = float(input("Enter number: "))
            print("Result:", square_root(num))

        elif choice == '7':

            print("Thank you for using calculator!")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter valid numbers")