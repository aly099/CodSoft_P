# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Main calculator loop
while True:
    print("\n----------OPTIONS:----------")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Quit")
    print("----------------------------")
    
    choice = input("Enter your choice: ")

    if choice == "5":
        print("Have a great day!")
        break
    
    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter the First number: "))
        num2 = float(input("Enter the Second number: "))
        
        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        
        print(f"Result: {result}")
    else:
        print("Invalid input. Please choose a valid option.")
