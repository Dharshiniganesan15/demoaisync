# Simple Python Output Script

## Overview
This repository contains a single Python script (`app.py`) designed to demonstrate basic text output operations to the console. The script executes a sequence of print statements, though one of the statements is syntactically malformed and will cause the script to terminate prematurely.

## File Structure

```
.
└── app.py
```

## `app.py` Details

This Python script performs a series of actions primarily involving printing text to standard output.

**Code:**
```python
print("hi")
print("hello")
print("test")
p r i n t ( ' t e s t   w e b h o o k ' ) 
```

**Functionality:**
1.  Prints the string "hi" to the console.
2.  Prints the string "hello" to the console.
3.  Prints the string "test" to the console.
4.  The line `p r i n t ( ' t e s t   w e b h o o k ' )` contains spaces between the letters of the word "print", making it syntactically invalid as a Python `print()` function call. When Python attempts to execute this line, it will raise a `SyntaxError`, halting the script's execution at this point.

## How to Run

1.  **Prerequisites:** Ensure you have Python installed on your system.
2.  **Execution:** Navigate to the directory containing `app.py` in your terminal or command prompt. Execute the script using the Python interpreter:

    ```bash
    python app.py
    ```

## Expected Output

Upon running the script, you will observe the output from the first three `print()` statements, followed by a `SyntaxError` that indicates the issue with the malformed line:

```
hi
hello
test
  File "app.py", line 4
    p r i n t ( ' t e s t   w e b h o o k ' ) 
    ^
SyntaxError: invalid syntax
```