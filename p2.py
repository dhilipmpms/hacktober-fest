def add(x, y):
    return x + y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("The sum is", add(num1, num2))
def subtract(x, y):
    return x - y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("The difference is", subtract(num1, num2))
def multiply(x, y):
    return x * y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("The product is", multiply(num1, num2))
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("The quotient is", divide(num1, num2))
