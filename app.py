import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot do modulo by zero.")
    return a % b


def power(a, b):
    return a ** b


def floor_divide(a, b):
    if b == 0:
        raise ValueError("Cannot floor-divide by zero.")
    return a // b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)


def percent_of(a, b):
    return (a / 100.0) * b


def calculate(a, b, operator):
    if operator == "+":
        return add(a, b)
    if operator == "-":
        return subtract(a, b)
    if operator == "*":
        return multiply(a, b)
    if operator == "/":
        return divide(a, b)
    if operator == "%":
        return modulo(a, b)
    if operator == "^":
        return power(a, b)
    if operator == "//":
        return floor_divide(a, b)
    raise ValueError("Unsupported operator. Use one of: +, -, *, /, %, ^, //")


def evaluate_expression(expression):
    """Parse and evaluate expressions like '12 + 7'."""
    parts = expression.strip().split()
    if len(parts) != 3:
        raise ValueError("Expression format should be: <number> <operator> <number>")
    a = float(parts[0])
    operator = parts[1]
    b = float(parts[2])
    return calculate(a, b, operator)


def print_history(history):
    if not history:
        print("No calculations yet.")
        return
    print("\nCalculation History:")
    for i, item in enumerate(history, start=1):
        print(f"{i}. {item}")
    print("")


def main():
    print("Simple Calculator")
    print("Supported operators: +, -, *, /, %, ^, //")
    print("Extra commands: sqrt <number>, pct <percent> <number>, expr <a op b>")
    print("Type 'history' to view previous calculations.")
    print("Type 'exit' to quit.\n")

    history = []

    while True:
        first = input("Enter first number (or 'exit'/'history'): ").strip().lower()
        if first == "exit":
            print("Goodbye.")
            break
        if first == "history":
            print_history(history)
            continue
        if first.startswith("sqrt "):
            try:
                value = float(first.split(maxsplit=1)[1])
                result = square_root(value)
                history.append(f"sqrt {value} = {result}")
                print(f"Result: {result}\n")
            except ValueError as exc:
                print(f"Error: {exc}\n")
            continue
        if first.startswith("pct "):
            try:
                parts = first.split()
                if len(parts) != 3:
                    raise ValueError("Format: pct <percent> <number>")
                percent = float(parts[1])
                number = float(parts[2])
                result = percent_of(percent, number)
                history.append(f"{percent}% of {number} = {result}")
                print(f"Result: {result}\n")
            except ValueError as exc:
                print(f"Error: {exc}\n")
            continue
        if first.startswith("expr "):
            try:
                expression = first.split(maxsplit=1)[1]
                result = evaluate_expression(expression)
                history.append(f"{expression} = {result}")
                print(f"Result: {result}\n")
            except ValueError as exc:
                print(f"Error: {exc}\n")
            continue

        try:
            a = float(first)
            operator = input("Enter operator (+, -, *, /, %, ^, //): ").strip()
            b = float(input("Enter second number: ").strip())
            result = calculate(a, b, operator)
            expression = f"{a} {operator} {b} = {result}"
            history.append(expression)
            print(f"Result: {result}\n")
        except ValueError as exc:
            print(f"Error: {exc}\n")


if __name__ == "__main__":
    main()
