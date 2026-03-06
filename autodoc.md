# Codebase Documentation

This document provides a comprehensive overview of the codebase, adhering strictly to the provided files and their contents without inferring or inventing features.

## Overview

This codebase consists of two distinct applications: a command-line calculator implemented in Python, and a web-based task manager implemented using HTML, CSS, and JavaScript. The Python application provides basic arithmetic operations and maintains a history of calculations. The web application allows users to create, manage, filter, sort, and persist tasks with various attributes.

## File Structure

The codebase is composed of the following files:

*   `app.py`: Contains the Python source code for the command-line calculator.
*   `sample-app.html`: Contains the HTML structure, embedded CSS styling, and embedded JavaScript functionality for the web-based task manager.

## File: app.py

This file contains a Python program that functions as a simple command-line calculator. It defines several functions for basic arithmetic operations, a core `calculate` function to dispatch operations, and a `main` function to handle user interaction and calculation history.

**Functions:**

*   `add(a, b)`:
    *   Takes two numerical arguments, `a` and `b`.
    *   Returns their sum.
*   `subtract(a, b)`:
    *   Takes two numerical arguments, `a` and `b`.
    *   Returns the result of `a` minus `b`.
*   `multiply(a, b)`:
    *   Takes two numerical arguments, `a` and `b`.
    *   Returns their product.
*   `divide(a, b)`:
    *   Takes two numerical arguments, `a` and `b`.
    *   Raises a `ValueError` if `b` is 0, preventing division by zero.
    *   Returns the result of `a` divided by `b`.
*   `modulo(a, b)`:
    *   Takes two numerical arguments, `a` and `b`.
    *   Raises a `ValueError` if `b` is 0, preventing modulo by zero.
    *   Returns the remainder of `a` divided by `b`.
*   `power(a, b)`:
    *   Takes two numerical arguments, `a` and `b`.
    *   Returns `a` raised to the power of `b`.
*   `floor_divide(a, b)`:
    *   Takes two numerical arguments, `a` and `b`.
    *   Raises a `ValueError` if `b` is 0, preventing floor division by zero.
    *   Returns the floor division result of `a` by `b`.
*   `calculate(a, b, operator)`:
    *   Takes two numerical arguments (`a`, `b`) and a string `operator`.
    *   Dispatches the calculation to the appropriate arithmetic function based on the `operator` string.
    *   Supported operators are `+`, `-`, `*`, `/`, `%`, `^`, `//`.
    *   Raises a `ValueError` for unsupported operators.
    *   Returns the result of the operation.
*   `print_history(history)`:
    *   Takes a list `history` (expected to contain strings representing calculations).
    *   Prints "No calculations yet." if the history list is empty.
    *   Otherwise, prints a numbered list of all items in the `history`.
*   `main()`:
    *   This is the entry point for the calculator application.
    *   Prints a welcome message, supported operators, and instructions for 'history' and 'exit' commands.
    *   Initializes an empty list `history` to store calculation expressions.
    *   Enters an infinite loop to continuously prompt the user for input.
    *   Allows the user to type 'exit' to quit the application or 'history' to view past calculations.
    *   Prompts for the first number, operator, and second number.
    *   Attempts to convert inputs to `float` and calls `calculate`.
    *   If successful, formats the expression and result, appends it to `history`, and prints the result.
    *   Catches `ValueError` exceptions (e.g., for invalid input, division by zero, or unsupported operators) and prints an error message.

## File: sample-app.html

This file contains a complete HTML document that structures a web-based Task Manager application. It includes embedded CSS for styling and embedded JavaScript for all interactive functionality, task management logic, and local storage persistence.

## HTML Structure

The document defines a standard HTML5 page:

*   **`<!doctype html>`**: Declares the document type.
*   **`<html lang="en">`**: The root element, set to English language.
*   **`<head>`**: Contains metadata for the page.
    *   **`<meta charset="UTF-8" />`**: Specifies character encoding.
    *   **`<meta name="viewport" content="width=device-width, initial-scale=1.0" />`**: Configures the viewport for responsive design.
    *   **`<title>Task Manager</title>`**: Sets the browser tab title.
    *   **`<style>`**: Contains all the embedded CSS rules for the application's appearance.
*   **`<body>`**: Contains the visible content of the web page.
    *   **`<main class="app">`**: The main container for the task manager application.
        *   **`<header>`**: Displays the application title and a real-time clock.
            *   `<h1>Demo AI Sync - Task Board</h1>`
            *   `<span id="clock"></span>`: Element to display the current date and time.
        *   **`<section class="content">`**: The main content area containing task input, filters, actions, and the task list.
            *   **Input Row 1 (`div.row`):**
                *   `<input id="taskInput" type="text" placeholder="Enter task..." />`: Text input for new task description.
                *   `<select id="prioritySelect">` (options: High, Medium, Low): Dropdown to select priority for new tasks.
                *   `<input id="dueDateInput" type="date" />`: Date input for new task due date.
                *   `<button id="addBtn">Add Task</button>`: Button to add a new task.
            *   **Control Row 2 (`div.row`):**
                *   `<select id="filterSelect">` (options: All, Active, Done): Dropdown to filter tasks by completion status.
                *   `<select id="sortSelect">` (options: Newest, Oldest, Priority, Due Date): Dropdown to sort the task list.
                *   `<input id="searchInput" type="text" placeholder="Search tasks..." />`: Text input to search tasks.
                *   `<button id="clearCompletedBtn" class="button-clear">Clear Completed</button>`: Button to remove all completed tasks.
            *   **Summary Row (`div.row`):**
                *   `<div class="meta" id="summary">0 tasks</div>`: Displays a summary of tasks.
            *   **Bulk Actions Row (`div.row`):**
                *   `<button id="markAllDoneBtn" class="button-clear">Mark All Done</button>`: Button to mark all tasks as completed.
                *   `<button id="markAllActiveBtn" class="button-clear">Mark All Active</button>`: Button to mark all tasks as active.
                *   `<button id="exportBtn" class="button-clear">Export JSON</button>`: Button to export tasks as a JSON file.
                *   `<button id="importBtn" class="button-clear">Import JSON</button>`: Button to trigger task import.
            *   **Task List (`ul#taskList`)**: An unordered list where individual tasks are dynamically rendered.
            *   **Empty State (`div#emptyState`)**: A message displayed when no tasks are currently visible.
            *   **Import File Input (`input#importFileInput`)**: A hidden file input used for selecting JSON files for import.
    *   **`<script>`**: Contains all the embedded JavaScript code for application logic.

## CSS Styling

The embedded CSS defines the visual presentation of the task manager.

*   **Variables (`:root`)**: Defines custom CSS properties for colors, including background, card background, text colors, primary/success/danger colors, and border color.
*   **Global Reset (`*`)**: Sets `box-sizing` to `border-box`.
*   **`body`**: Styles the overall page with `margin: 0`, a system font stack, a linear gradient background, text color, minimum height, and centers the content using `grid` and `place-items`.
*   **`.app`**: Styles the main application container with a maximum width, background, border, border-radius, and box-shadow.
*   **`header`**: Styles the application header with a dark background, white text, padding, and uses flexbox for alignment and spacing. `h1` and `span` inside the header are also styled.
*   **`.content`**: Styles the main content area with padding and a grid layout for spacing.
*   **`.row`**: A utility class for creating grid layouts for grouping related elements, often used with `grid-template-columns`.
*   **`input, select, button`**: General styling for form elements including font inheritance, border-radius, border, and padding. Focus styles are also defined.
*   **`button`**: Base styles for buttons, including cursor, removing default border, background, text color, and font weight.
    *   `.button-clear`: A variant for secondary buttons.
*   **`ul`**: Resets list styles, margins, padding, and applies a grid layout.
*   **`li`**: Styles individual list items with borders, padding, and a grid layout to align task text and controls.
*   **`.meta`**: Styles for secondary text like task creation date or due date.
*   **`.badge`**: Styles for priority badges, with specific color variants.
    *   `.priority-high`, `.priority-medium`, `.priority-low`: Background and text colors for different priority levels.
*   **`.overdue`**: Styling for overdue task indicators, making the text red and bold.
*   **`.controls`**: Styles the container for task action buttons (Done, Edit, Delete) using flexbox.
*   **`.done`**: Styling for completed tasks, applying a line-through and changing text color.
*   **`.btn-success`, `.btn-danger`**: Specific background colors for success (Done/Undo) and danger (Delete) buttons.
*   **`.empty`**: Styling for the empty state message, with padding, centered text, muted color, and a dashed border.

## JavaScript Functionality

The embedded JavaScript provides all the interactive functionality for the Task Manager application.

**DOM Element References:**
Variables are declared to hold references to various HTML elements by their IDs: `taskInput`, `prioritySelect`, `dueDateInput`, `addBtn`, `taskList`, `filterSelect`, `sortSelect`, `searchInput`, `clearCompletedBtn`, `markAllDoneBtn`, `markAllActiveBtn`, `exportBtn`, `importBtn`, `importFileInput`, `summary`, `emptyState`, and `clock`.

**Constants:**
*   `STORAGE_KEY`: A string used as the key for storing task data in `localStorage`.
*   `tasks`: An array that holds all the task objects.

**Functions:**

*   `formatDateTime(d = new Date())`:
    *   Takes an optional `Date` object (defaults to current date/time).
    *   Returns a locale-specific string representation of the date and time.
*   `renderClock()`:
    *   Updates the `textContent` of the `clock` DOM element with the current formatted date and time using `formatDateTime()`.
*   `createTask(text, priority, dueDate)`:
    *   Creates and returns a new task object with properties:
        *   `id`: A unique identifier generated using `crypto.randomUUID()`.
        *   `text`: The task description.
        *   `priority`: (defaults to "medium")
        *   `dueDate`: (defaults to empty string)
        *   `done`: (defaults to `false`)
        *   `createdAt`: Timestamp of creation in ISO string format.
*   `saveTasks()`:
    *   Serializes the `tasks` array to a JSON string.
    *   Stores the JSON string in `localStorage` using `STORAGE_KEY`.
*   `loadTasks()`:
    *   Retrieves task data from `localStorage` using `STORAGE_KEY`.
    *   Parses the JSON string.
    *   Filters and maps the parsed data to ensure tasks have valid structure and default values.
    *   Populates the global `tasks` array with the loaded, cleaned tasks.
    *   Includes error handling for parsing invalid JSON.
*   `addTask()`:
    *   Retrieves values from `taskInput`, `prioritySelect`, and `dueDateInput`.
    *   If `taskInput` is empty, the function returns early.
    *   Creates a new task using `createTask()`.
    *   Adds the new task to the beginning of the `tasks` array (`unshift`).
    *   Clears the input fields and resets `prioritySelect`.
    *   Calls `saveTasks()` and `render()`.
    *   Sets focus back to `taskInput`.
*   `toggleTask(id)`:
    *   Finds a task by its `id` within the `tasks` array.
    *   If found, toggles its `done` status.
    *   Calls `saveTasks()` and `render()`.
*   `editTask(id)`:
    *   Finds a task by its `id`.
    *   Prompts the user to edit the task's text.
    *   If the user provides valid, non-empty text, updates the task's `text` property.
    *   Calls `saveTasks()` and `render()`.
*   `removeTask(id)`:
    *   Finds the index of a task by its `id`.
    *   If found, removes the task from the `tasks` array using `splice`.
    *   Calls `saveTasks()` and `render()`.
*   `clearCompletedTasks()`:
    *   Iterates through the `tasks` array in reverse.
    *   Removes any task where `done` is `true`.
    *   Calls `saveTasks()` and `render()`.
*   `markAllDone()`:
    *   Sets the `done` property of all tasks in the `tasks` array to `true`.
    *   Calls `saveTasks()` and `render()`.
*   `markAllActive()`:
    *   Sets the `done` property of all tasks in the `tasks` array to `false`.
    *   Calls `saveTasks()` and `render()`.
*   `exportTasks()`:
    *   Creates a `payload` object containing the current `tasks` array and an `exportedAt` timestamp.
    *   Serializes the payload to a JSON string.
    *   Creates a `Blob` object from the JSON string.
    *   Creates a temporary anchor (`<a>`) element, sets its `href` to a URL created from the `Blob`, and sets a dynamic `download` filename.
    *   Simulates a click on the anchor to trigger the download.
    *   Cleans up the temporary URL and anchor element.
*   `importTasksFromFile(file)`:
    *   Takes a `File` object as an argument.
    *   Uses a `FileReader` to read the content of the file as text.
    *   On `onload` event:
        *   Parses the file content as JSON. It can handle either a direct array of tasks or an object with a `tasks` property.
        *   Filters and maps the incoming tasks to ensure valid structure and default values, similar to `loadTasks()`.
        *   Replaces the current `tasks` array with the imported, cleaned tasks.
        *   Calls `saveTasks()` and `render()`.
        *   Displays an alert if the JSON file is invalid.
*   `getFilteredTasks()`:
    *   Applies filtering based on the `filterSelect` value ("all", "active", "done").
    *   Applies searching based on the `searchInput` value (case-insensitive substring match on task text).
    *   Applies sorting based on the `sortSelect` value ("newest", "oldest", "priority", "due").
        *   "priority" sorting uses a predefined rank (`high: 0, medium: 1, low: 2`).
        *   "due" sorting handles tasks without due dates.
        *   "newest" (default) and "oldest" sort by `createdAt` timestamp.
    *   Returns a new array of filtered and sorted task objects.
*   `render()`:
    *   Calls `getFilteredTasks()` to get the tasks to display.
    *   Clears the `taskList` HTML element.
    *   Iterates over the filtered tasks:
        *   Constructs HTML for each task, including text, priority badge, due date, creation date, and control buttons (Done/Undo, Edit, Delete).
        *   Dynamically applies `done` class if the task is completed and `overdue` class if the task has passed its due date and is not completed.
        *   Attaches event listeners to the dynamically created toggle, edit, and delete buttons.
        *   Appends the new `li` element to `taskList`.
    *   Updates the `summary` element with task counts (total, done, showing).
    *   Toggles the display of `emptyState` based on whether there are tasks to show.
    *   Dynamically enables/disables and styles `clearCompletedBtn`, `markAllDoneBtn`, and `markAllActiveBtn` based on the current state of tasks.

**Event Listeners:**
*   `addBtn` clicks call `addTask()`.
*   `taskInput` `keydown` for "Enter" key calls `addTask()`.
*   `filterSelect` `change` event calls `render()`.
*   `sortSelect` `change` event calls `render()`.
*   `searchInput` `input` event calls `render()`.
*   `clearCompletedBtn` clicks call `clearCompletedTasks()`.
*   `markAllDoneBtn` clicks call `markAllDone()`.
*   `markAllActiveBtn` clicks call `markAllActive()`.
*   `exportBtn` clicks call `exportTasks()`.
*   `importBtn` clicks triggers a click on the hidden `importFileInput`.
*   `importFileInput` `change` event reads the selected file and calls `importTasksFromFile()`, then resets the file input.

**Initialization:**
*   `loadTasks()` is called once when the script loads to retrieve previously saved tasks.
*   `setInterval(renderClock, 1000)` sets up a timer to update the clock every second.
*   `renderClock()` is called immediately to display the clock on load.
*   `render()` is called immediately to display the initial task list.

## Features

*   **Python Calculator:**
    *   Performs basic arithmetic operations: addition, subtraction, multiplication, division, modulo, power, and floor division.
    *   Handles division by zero errors for `/`, `%`, and `//` operators.
    *   Interactive command-line interface.
    *   Stores and displays a history of calculations.
    *   Supports `exit` command to terminate the program.
    *   Supports `history` command to view past calculations.
*   **HTML Task Manager:**
    *   Add tasks with a description, priority (High, Medium, Low), and an optional due date.
    *   Displays a list of tasks.
    *   Toggle task completion status (mark as done or active).
    *   Edit existing task descriptions.
    *   Delete individual tasks.
    *   Filter tasks by status: all, active, or done.
    *   Sort tasks by newest first, oldest first, priority (High > Medium > Low), or due date.
    *   Search tasks by text description.
    *   Clear all completed tasks.
    *   Mark all tasks as done.
    *   Mark all tasks as active.
    *   Export all tasks to a JSON file.
    *   Import tasks from a JSON file.
    *   Persists task data in the browser's local storage.
    *   Displays a real-time clock in the header.
    *   Provides a summary of tasks (total, done, showing count).
    *   Visual indicators for task priority, overdue status, and completion (strike-through).
    *   Displays an "empty state" message when no tasks match the current filters/search.

## How to Use/Run

**Python Calculator (`app.py`):**

1.  Save the provided Python code as `app.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved `app.py`.
4.  Run the application using the command: `python app.py`
5.  Follow the on-screen prompts to enter numbers and operators.
6.  Type `history` to view past calculations.
7.  Type `exit` to quit the application.

**HTML Task Manager (`sample-app.html`):**

1.  Save the provided HTML code as `sample-app.html`.
2.  Open a web browser (e.g., Chrome, Firefox, Edge).
3.  Navigate to the saved `sample-app.html` file by:
    *   Dragging the file into an open browser window or tab.
    *   Using the "File > Open File..." menu option in your browser.
    *   Typing the local file path into the browser's address bar.
4.  The task manager application will load in your browser. You can then interact with the input fields, buttons, and dropdowns to manage tasks.
5.  Task data will be automatically saved and loaded from your browser's local storage.