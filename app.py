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
