def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            print("Result:", add(num1, num2))
        elif operator == '-':
            print("Result:", subtract(num1, num2))
        elif operator == '*':
            print("Result:", multiply(num1, num2))
        elif operator == '/':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid operator! Please enter one of +, -, *, /")
    except ValueError:
        print("Invalid input! Please enter numeric values only.")

if __name__ == "__main__":
    calculator()
