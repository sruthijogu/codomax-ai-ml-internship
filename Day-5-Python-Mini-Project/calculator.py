# Step 1: Define the function first at the top
def calculator(num1, num2, choice):
    if choice == 1:
        result = num1 + num2
        print("Result:", result)
    elif choice == 2:
        result = num1 - num2
        print("Result:", result)
    elif choice == 3:
        result = num1 * num2
        print("Result:", result)
    elif choice == 4:
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print("Invalid choice")

# Step 2: Run the main application loop
while True:
    print("\n---- Calculator ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit") # Added a clean exit option
    
    choice = int(input("Choose an operation (1-5): "))
    
    # Check if the user wants to close the program
    if choice == 5:
        print("Exiting calculator. Goodbye!")
        break
    elif choice < 1 or choice > 5:
        print("Invalid option. Please try again.")
        continue

    # Take number inputs inside the loop for new calculations
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Step 3: Call the function with user inputs
    calculator(num1, num2, choice)