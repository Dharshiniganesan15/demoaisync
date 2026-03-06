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


def calculate(a, b, operator):
    if operator == "+":
        return add(a, b)
    if operator == "-":
        return subtract(a, b)
    if operator == "*":
        return multiply(a, b)
    if operator == "/":
        return divide(a, b)
    raise ValueError("Unsupported operator. Use one of: +, -, *, /")


def main():
    print("Simple Calculator")
    print("Supported operators: +, -, *, /")

    try:
        a = float(input("Enter first number: ").strip())
        operator = input("Enter operator (+, -, *, /): ").strip()
        b = float(input("Enter second number: ").strip())
        result = calculate(a, b, operator)
        print(f"Result: {result}")
    except ValueError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
