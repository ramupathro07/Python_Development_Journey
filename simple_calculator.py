
import math


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


print("Advanced Calculator")
print("===================")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power (a^b)")
print("6. Modulus (a % b)")
print("7. Square Root")
print("8. Percentage")
print("9. Exit")

while True:
    print("\nChoose an operation:")
    choice = input("Enter option (1-9): ").strip()

    if choice == '9':
        print("Exiting advanced calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4', '5', '6', '8'):
        a = get_float("Enter the first number: ")
        b = get_float("Enter the second number: ")

        if choice == '1':
            print("Result:", a + b)
        elif choice == '2':
            print("Result:", a - b)
        elif choice == '3':
            print("Result:", a * b)
        elif choice == '4':
            if b == 0:
                print("Error: Division by zero")
            else:
                print("Result:", a / b)
        elif choice == '5':
            print("Result:", a ** b)
        elif choice == '6':
            if b == 0:
                print("Error: Modulus by zero")
            else:
                print("Result:", a % b)
        elif choice == '8':
            print("Result:", (a * b) / 100)

    elif choice == '7':
        a = get_float("Enter a number: ")
        if a < 0:
            print("Error: Square root of a negative number is not real.")
        else:
            print("Result:", math.sqrt(a))

    else:
        print("Invalid choice. Please select a valid option.")
