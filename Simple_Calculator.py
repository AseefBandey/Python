#Python Program to Make a Simple Calculator
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

operations = {
    "add": add,
    "sub": sub,
    "mul": multiply,
    "div": divide
}

print("Welcome! Choose an Operation: \n Add = Addition \n Sub = Subtraction \n Mul = Multiplication \n Div = Division")
input_cal = input("Enter Preferred Arithmetic Operator Abbreviation: ").lower()

if input_cal in operations:
    try:
        x = int(input("Enter First Number: "))
        y = int(input("Enter Second Number: "))

        result = operations[input_cal](x, y) #dynamic function calling using a dictionary
        print(f"Result: {result}")
    
    except ValueError:
        print("Error! Please enter valid numbers.")
else:
    print("Invalid input! Please enter 'add', 'sub', 'mul', or 'div'.")

