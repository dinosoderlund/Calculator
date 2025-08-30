#different calculation operations for calculator
def add(a,b):
    print(f"{a} + {b} = {a + b}")

def subtract(a,b):
    print(f"{a} - {b} = {a - b}")

def divide(a,b):
    print(f"{a} / {b} = {a / b}")

def multiply(a,b):
    print(f"{a} * {b} = {a * b}")

#menu 
num1 = float(input(("Enter the first number: ")))
num2 = float(input(("Enter the second number: ")))
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
choice = int(input("What do you want to choose(1,2,3,4): "))
if choice == 1:
    add(num1, num2)
elif choice == 2:
    subtract(num1, num2)
elif choice == 3:
    divide(num1, num2)
elif choice == 4:
    multiply(num1, num2)


