# Simple Python Greeter

This repository contains a very basic Python script that prints two greeting messages to the console.

## Table of Contents

*   [Description](#description)
*   [Getting Started](#getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation](#installation)
*   [Usage](#usage)
*   [File Analysis](#file-analysis)

## Description

The `app.py` script is a minimalistic demonstration of Python's `print()` function. When executed, it outputs two distinct strings, "hi" and "hello", sequentially to the standard output.

## Getting Started

### Prerequisites

To run this script, you will need:

*   Python (version 3.x recommended)

### Installation

No special installation steps are required beyond having a Python interpreter installed on your system.
You can download Python from the [official Python website](https://www.python.org/downloads/).

## Usage

To run the script, navigate to the directory containing `app.py` in your terminal or command prompt and execute the following command:

```bash
python app.py
```

Upon execution, the script will produce the following output:

```
hi
hello
```

## File Analysis

### `app.py`

This file contains the core logic of the application, which is a simple sequence of two print statements.

```python
print("hi")
print("hello")
```

*   `print("hi")`: This line uses the built-in `print()` function in Python to output the string "hi" to the console.
*   `print("hello")`: This line, immediately following the first, outputs the string "hello" to the console. Each `print()` call results in a new line by default.