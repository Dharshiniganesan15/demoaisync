# Python Console Output Example

## Overview

This repository contains a single Python script, `app.py`, designed to demonstrate basic console output operations. The script features a mix of standard Python `print()` function calls and several lines that resemble `print` statements but contain unusual spacing, which affects their execution as valid Python code.

## Project Structure

```
.
└── app.py
```

## `app.py`

The `app.py` script is written in Python and consists of a sequence of statements intended to display textual messages.

### Valid Console Output

The initial part of the script uses standard Python `print()` function calls. These lines are syntactically correct and, when executed by a Python interpreter, will output the specified strings to the console:

```python
print("hi")
print("hello")
print("test")
```

Upon execution, these lines will produce the following output:

```
hi
hello
test
```

### Malformed Console Output Attempts

Following the valid `print` statements, the script includes several lines that visually resemble `print` statements but contain spaces within the `print` keyword (e.g., `p r i n t` instead of `print`). This spacing makes them syntactically incorrect as function calls in standard Python.

```python
p r i n t ( ' t e s t   w e b h o o k ' )
 
 p r i n t ( ' t e s t   f i x ' )
 
 p r i n t ( ' t e s t   f i x ' )
 
 p r i n t ( ' t e s d d e ' )
 
 p r i n t ( ' n e w   f e a t u r e ' )
 
 p r i n t ( ' p r   f i x   t e s t ' )
 
 p r i n t ( ' f i n a l   t e s t ' )
```

Due to the non-standard spacing within the `p r i n t` identifier, these lines are not recognized as calls to the built-in `print()` function by a typical Python interpreter. Attempting to execute these lines directly would likely result in a `SyntaxError` or `NameError`, and they would not produce any console output as intended by a standard `print` function. These lines are present in the code exactly as shown, representing the literal text content of the file.