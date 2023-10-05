# Calculator
from art import logo
# Add
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    num1 = float(input("Whats the first number?: "))
    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))

    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    finish_calculate = False
    while not finish_calculate:
        continue_calculate = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if continue_calculate == "n":
            finish_calculate = True
            calculator()
        elif continue_calculate == "y":
            operation_symbol = input("Pick an operation: ")
            next_num = float(input("What's the next number?: "))
            next_answer = operations[operation_symbol](answer, next_num)
            print(f"{answer} {operation_symbol} {next_num} = {next_answer}")

calculator()