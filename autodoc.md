# Python Print Statements Example

## Overview

This repository contains a single Python script (`app.py`) that demonstrates the use of the `print()` function to output various string literals to the console.

## Files

### `app.py`

This Python script sequentially executes several `print()` statements. Each statement outputs a specific string to standard output, with each string appearing on a new line.

The script performs the following actions:

*   Prints the string `"hi"`.
*   Prints the string `"hello"`.
*   Prints the string `"test"`.
*   Prints the string `"t e s t   w e b h o o k"`. Note the explicit spaces between characters in this string literal.
*   Prints the string `"t e s t   f i x"`. Note the explicit spaces between characters in this string literal.
*   Prints the string `"t e s t   f i x"` again. Note the explicit spaces between characters in this string literal.

There are also visible spaces between the `p`, `r`, `i`, `n`, `t` characters in the function calls for the last three print statements, as well as before the opening parenthesis, which Python's lexer ignores as whitespace.

## Usage

To execute the `app.py` script, ensure you have a Python interpreter installed. Then, navigate to the directory containing the `app.py` file in your terminal and run the script using the Python command:

```bash
python app.py
```

### Expected Output

Upon execution, the script will produce the following output to the console:

```
hi
hello
test
t e s t   w e b h o o k
t e s t   f i x
t e s t   f i x
```