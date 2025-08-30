import tkinter as tk


# calculator operations
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


ops = {"+": add, "-": subtract, "/": divide, "*": multiply}


class Calculator:
    def _init_(self, root):
        self.first_num = None
        self.operator = None

        self.entry = tk.Entry(root, width=20, font=("Arial", 18), bd=5, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
            ("C", 5, 0),
        ]

        for text, r, c in buttons:
            if text.isdigit() or text == ".":
                cmd = lambda t=text: self.press_number(t)
            elif text in ops:
                cmd = lambda t=text: self.press_operator(t)
            elif text == "=":
                cmd = self.press_equals
            elif text == "CE":
                cmd = self.clear

            tk.Button(
                root, text=text, width=5, height=2, font=("Arial", 14), command=cmd
            ).grid(row=r, column=c)

#need to add function for pres snumber, operator, equals, clear


# menu
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
