"""
Calculator module.
"""


class Calculator:
    """
    Calculator class.
    """
    def __init__(self, num1, num2):
        """
        Create new Calculator object.
        """
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        """
        Sum opration.
        """
        result = self.num1 + self.num2
        print(f"The result of sum is ({result}).")

    def subtraction(self):
        """
        Subtraction opration.
        """
        result = self.num1 - self.num2
        print(f"The result of subtraction is ({result}).")

    def multiply(self):
        """
        Multiply opration.
        """
        result = self.num1 * self.num2
        print(f"The result of multiply is ({result}).")

    def division(self):
        """
        Division opration.
        """
        if self.num2 != 0:
            result = self.num1 / self.num2
            print(f"The result of division is ({result}).")
        else:
            print("Error: Division by zero is not allowed.")


while True:
    try:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
    except ValueError:
        print("Please use integer.")
        continue

    nums = Calculator(number1, number2)
    operator = input("""Enter the operation (+,-,*,/,
                     q(if you want to quit)): """).lower()

    if operator == "+":
        nums.sum()
    elif operator == "-":
        nums.subtraction()
    elif operator == "*":
        nums.multiply()
    elif operator == "/":
        nums.division()
    elif operator == "q":
        break
    else:
        print("Wrong operation.")
