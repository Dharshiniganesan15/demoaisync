# Codebase Documentation

This document provides a comprehensive overview of the codebase, adhering strictly to the provided files and their contents without inferring or inventing features.

## Overview

This codebase consists of two distinct parts: a simple Python script (`app.py`) providing basic arithmetic operations, and a client-side web application (`sample-app.html`) that functions as a "Task Manager." The Python script and the web application are independent and do not interact with each other within this codebase.

The web application, `sample-app.html`, is a standalone HTML file that includes embedded CSS for styling and JavaScript for all its dynamic functionality. It allows users to create, manage, filter, sort, and persist tasks directly within their web browser using local storage.

## File Structure

- `app.py`: Contains Python functions for arithmetic operations.
- `sample-app.html`: A self-contained HTML file that implements a task manager application, including embedded CSS styles and JavaScript logic.

## File: app.py

**Language:** Python

This file defines two basic mathematical functions:

-   `add(a, b)`: Takes two arguments, `a` and `b`, and returns their sum.
-   `subtract(a, b)`: Takes two arguments, `a` and `b`, and returns their difference.

These functions are designed for direct invocation within a Python environment and do not have any interaction or integration with the `sample-app.html` file.

## File: sample-app.html

**Language:** HTML, CSS, JavaScript

This file constitutes a complete client-side task management application.

It is structured as a standard HTML5 document, including:

-   **Metadata:** Defines character set, viewport settings, and the page title "Task Manager."
-   **Embedded CSS (`<style>` tag):** Contains all the styling rules for the application, defining colors, layout, and visual presentation of elements.
-   **HTML Structure (`<body>` tag):** Organizes the user interface elements such as a header, input fields for adding tasks, controls for filtering, sorting, and searching, a list to display tasks, and an empty state message.
-   **Embedded JavaScript (`<script>` tag):** Implements all the application logic, including DOM manipulation, event handling, task creation, modification, deletion, persistence using `localStorage`, filtering, sorting, and import/export functionality.

This single file contains the entire user interface and operational logic for the task manager.

## HTML Structure

The `sample-app.html` file defines the following key HTML elements and their organization:

-   `<!doctype html>`: Declares an HTML5 document.
-   `<html lang="en">`: Root element with language set to English.
-   `<head>`:
    -   `<meta charset="UTF-8" />`: Specifies UTF-8 character encoding.
    -   `<meta name="viewport" content="width=device-width, initial-scale=1.0" />`: Configures the viewport for responsive design.
    -   `<title>Task Manager</title>`: Sets the title displayed in the browser tab.
    -   `<style>`: Contains all the CSS styling for the application.
-   `<body>`:
    -   `<main class="app">`: The main container for the application, styled to appear as a card.
        -   `<header>`:
            -   `<h1>Demo AI Sync - Task Board</h1>`: The main title of the application.
            -   `<span id="clock"></span>`: An empty span where the current date and time are displayed by JavaScript.
        -   `<section class="content">`: The primary content area containing task input and controls.
            -   `<div class="row">` (for adding tasks):
                -   `<input id="taskInput" type="text" placeholder="Enter task..." />`: Input field for new task text.
                -   `<select id="prioritySelect">`: Dropdown to select task priority (High, Medium, Low).
                -   `<input id="dueDateInput" type="date" />`: Date input for task due date.
                -   `<button id="addBtn">Add Task</button>`: Button to add a new task.
            -   `<div class="row">` (for filtering and sorting):
                -   `<select id="filterSelect">`: Dropdown to filter tasks by status (All, Active, Done).
                -   `<select id="sortSelect">`: Dropdown to sort tasks (Newest, Oldest, Priority, Due Date).
                -   `<input id="searchInput" type="text" placeholder="Search tasks..." />`: Input for searching tasks by text.
                -   `<button id="clearCompletedBtn" class="button-clear">Clear Completed</button>`: Button to remove completed tasks.
            -   `<div class="row">` (for task summary):
                -   `<div class="meta" id="summary">0 tasks</div>`: Displays a summary of tasks.
            -   `<div class="row">` (for bulk actions and import/export):
                -   `<button id="markAllDoneBtn" class="button-clear">Mark All Done</button>`: Button to mark all tasks as done.
                -   `<button id="markAllActiveBtn" class="button-clear">Mark All Active</button>`: Button to mark all tasks as active.
                -   `<button id="exportBtn" class="button-clear">Export JSON</button>`: Button to export tasks as a JSON file.
                -   `<button id="importBtn" class="button-clear">Import JSON</button>`: Button to trigger the import of tasks from a JSON file.
            -   `<ul id="taskList"></ul>`: An unordered list where individual task items are dynamically rendered by JavaScript.
            -   `<div id="emptyState" class="empty">No tasks yet. Add your first task.</div>`: A message displayed when no tasks are present or visible after filtering.
            -   `<input id="importFileInput" type="file" accept="application/json" style="display:none;" />`: A hidden file input used for importing JSON task data.
    -   `<script>`: Contains all the JavaScript logic for the application.

## CSS Styling

The embedded `<style>` block in `sample-app.html` provides the following styling:

-   **CSS Variables (`:root`):** Defines a set of custom properties for colors (`--bg`, `--card`, `--text`, `--muted`, `--primary`, `--success`, `--danger`, `--border`) for consistent theming.
-   **Universal Box-Sizing:** `* { box-sizing: border-box; }` ensures consistent box model behavior.
-   **Body Styling:** Sets margin, font family, a linear gradient background, text color, minimum height, centers content vertically and horizontally, and adds padding.
-   **`.app` (Main Container):** Styles the main application wrapper with a specific width, background, border, border-radius, and box-shadow, giving it a card-like appearance.
-   **`header`:** Styles the application header with a dark background, white text, padding, and uses flexbox for aligning its content (`h1` and `span`).
-   **`header h1`:** Resets margin and sets font size for the header title.
-   **`header span`:** Styles the clock display with a smaller font size and muted color.
-   **`.content`:** Styles the main content area with padding and a grid layout for its children.
-   **`.row`:** A general-purpose class for grid layouts, often with two columns, and a gap.
-   **`input`, `select`, `button`:** Base styles for form elements including font inheritance, border-radius, border, and padding. Focus styles are also applied.
-   **`button`:** General button styles with pointer cursor, no border, primary background color, white text, and bold font.
-   **`.button-clear`:** A specific style for buttons with a darker background, typically used for secondary actions.
-   **`ul`:** Resets list styling (no bullets, margin, padding) and applies a grid layout.
-   **`li`:** Styles individual task list items with a border, border-radius, padding, grid layout, and background.
-   **`.meta`:** Styles secondary information (e.g., due date, creation date) with muted color and smaller font size.
-   **`.badge`:** Styles small informational tags (e.g., priority) with rounded corners, padding, smaller font size, and bold text.
-   **`.priority-high`, `.priority-medium`, `.priority-low`:** Specific background and text colors for priority badges.
-   **`.overdue`:** Styles text for overdue tasks with a danger color and bold font.
-   **`.controls`:** Styles the container for action buttons within a task item, using flexbox for layout.
-   **`.done`:** Applies a line-through text decoration and muted color to completed task text.
-   **`.btn-success`, `.btn-danger`:** Utility classes for buttons with success (green) and danger (red) background colors.
-   **`.empty`:** Styles the message displayed when no tasks are present, with padding, centered text, muted color, and a dashed border.

## JavaScript Functionality

The embedded `<script>` block in `sample-app.html` implements the following JavaScript functionalities:

-   **DOM Element References:** All relevant HTML elements (task input, priority select, due date input, add button, task list, filter select, sort select, search input, clear completed button, mark all done/active buttons, export/import buttons, import file input, summary, empty state, clock) are referenced by their IDs.
-   **Constants:**
    -   `STORAGE_KEY`: A string used as the key for `localStorage` to store task data.
    -   `tasks`: An array that holds all the task objects in memory.
-   **`formatDateTime(d)`:** A helper function that takes a `Date` object (defaults to current date/time) and returns a locale-specific string representation of the date and time.
-   **`renderClock()`:** Updates the `clock` span element with the current formatted date and time.
-   **`createTask(text, priority, dueDate)`:** Creates and returns a new task object with a unique `id` (using `crypto.randomUUID()`), `text`, `priority`, `dueDate`, `done` status (initializes to `false`), and `createdAt` timestamp.
-   **`saveTasks()`:** Serializes the `tasks` array to a JSON string and saves it to `localStorage` under the `STORAGE_KEY`.
-   **`loadTasks()`:** Retrieves task data from `localStorage`, parses the JSON string, performs basic validation (ensuring it's an array and task objects have `text`), maps the data to a clean format, and populates the `tasks` array. Includes error handling for invalid JSON.
-   **`addTask()`:**
    -   Retrieves values from `taskInput`, `prioritySelect`, and `dueDateInput`.
    -   If `taskInput` is not empty, creates a new task using `createTask()`, adds it to the beginning of the `tasks` array (`unshift`).
    -   Clears input fields and resets priority to "medium."
    -   Calls `saveTasks()` and `render()`.
    -   Sets focus back to `taskInput`.
-   **`toggleTask(id)`:** Finds a task by `id` in the `tasks` array and flips its `done` status. Calls `saveTasks()` and `render()`.
-   **`editTask(id)`:** Finds a task by `id`. Prompts the user to edit the task's text. If valid input is provided, updates the task's `text`, calls `saveTasks()` and `render()`.
-   **`removeTask(id)`:** Finds a task by `id` and removes it from the `tasks` array. Calls `saveTasks()` and `render()`.
-   **`clearCompletedTasks()`:** Iterates through the `tasks` array from end to beginning and removes all tasks where `done` is `true`. Calls `saveTasks()` and `render()`.
-   **`markAllDone()`:** Sets the `done` status of all tasks in the `tasks` array to `true`. Calls `saveTasks()` and `render()`.
-   **`markAllActive()`:** Sets the `done` status of all tasks in the `tasks` array to `false`. Calls `saveTasks()` and `render()`.
-   **`exportTasks()`:**
    -   Creates a payload object containing `exportedAt` timestamp and the current `tasks` array.
    -   Converts the payload to a JSON string.
    -   Creates a `Blob` with the JSON data.
    -   Creates a temporary anchor (`<a>`) element, sets its `href` to a URL created from the blob, and sets `download` attribute for the filename (e.g., `tasks-YYYY-MM-DDTHH-MM-SS.json`).
    -   Programmatically clicks the anchor to trigger the download, then removes the anchor and revokes the object URL.
-   **`importTasksFromFile(file)`:**
    -   Takes a `File` object.
    -   Uses `FileReader` to read the file content as text.
    -   On successful load, parses the content as JSON.
    -   Extracts the incoming tasks (handles both array and object with `tasks` property).
    -   Filters and maps the incoming tasks to ensure basic validity and consistency (e.g., adds `id` if missing, trims text, sets default priority/due date, ensures `done` is boolean).
    -   Replaces the current `tasks` array with the imported clean tasks.
    -   Calls `saveTasks()` and `render()`.
    -   Includes error handling for invalid JSON format.
-   **`getFilteredTasks()`:**
    -   Filters tasks based on `filterSelect` value ("all", "active", "done") and `searchInput` value (case-insensitive text search).
    -   Sorts the filtered tasks based on `sortSelect` value ("newest", "oldest", "priority", "due"). Priority sorting uses a predefined rank. Due date sorting handles unset due dates.
    -   Returns the processed array of tasks.
-   **`render()`:** The main function to update the UI.
    -   Retrieves the filtered and sorted tasks using `getFilteredTasks()`.
    -   Clears the existing content of `taskList`.
    -   Iterates through each task:
        -   Constructs an `<li>` element dynamically.
        -   Applies `done` class if task is completed.
        -   Formats due date and applies `overdue` class if applicable.
        -   Applies `priority` badge classes.
        -   Attaches event listeners to the "Done"/"Undo", "Edit", and "Delete" buttons within each `li` to call `toggleTask`, `editTask`, and `removeTask` respectively.
        -   Appends the `li` to `taskList`.
    -   Updates the `summary` text with task counts (total, done, showing).
    -   Manages the `emptyState` display (visible if no tasks are shown, hidden otherwise).
    -   Disables/enables `clearCompletedBtn`, `markAllDoneBtn`, and `markAllActiveBtn` based on task states and counts.
-   **Event Listeners:**
    -   `addBtn` click and `taskInput` `keydown` (for "Enter" key): trigger `addTask()`.
    -   `filterSelect` `change`, `sortSelect` `change`, `searchInput` `input`: trigger `render()` to update the displayed task list.
    -   `clearCompletedBtn` `click`: triggers `clearCompletedTasks()`.
    -   `markAllDoneBtn` `click`: triggers `markAllDone()`.
    -   `markAllActiveBtn` `click`: triggers `markAllActive()`.
    -   `exportBtn` `click`: triggers `exportTasks()`.
    -   `importBtn` `click`: programmatically clicks the hidden `importFileInput` to open the file selection dialog.
    -   `importFileInput` `change`: when a file is selected, triggers `importTasksFromFile()` with the selected file and clears the input value.
-   **Initialization:**
    -   `loadTasks()`: Loads tasks from `localStorage` on page load.
    -   `setInterval(renderClock, 1000)`: Sets up an interval to update the clock every second.
    -   `renderClock()`: Calls `renderClock` immediately to display the clock on load.
    -   `render()`: Calls `render` immediately to display the initial task list.

## Features

-   **Python Arithmetic Functions:**
    -   Addition of two numbers.
    -   Subtraction of two numbers.
-   **Task Management (Web Application):**
    -   **Task Creation:** Add new tasks with text, priority (High, Medium, Low), and an optional due date.
    -   **Task Persistence:** Tasks are saved and loaded from the browser's `localStorage` between sessions.
    -   **Task Status Toggle:** Mark tasks as done or undo their completion status.
    -   **Task Editing:** Edit the text of an existing task.
    -   **Task Deletion:** Remove individual tasks.
    -   **Filtering:** Filter tasks by completion status (all, active, done).
    -   **Searching:** Search tasks by keywords in their text description.
    -   **Sorting:** Sort tasks by creation date (newest/oldest), priority, or due date.
    -   **Bulk Actions:**
        -   Clear all completed tasks.
        -   Mark all tasks as done.
        -   Mark all tasks as active.
    -   **Data Import/Export:**
        -   Export all current tasks to a JSON file.
        -   Import tasks from a user-selected JSON file.
    -   **Real-time Clock:** Displays the current date and time in the application header.
    -   **Visual Cues:**
        -   Tasks marked as "done" have strikethrough text.
        -   Priority is indicated by colored badges.
        -   Overdue tasks are highlighted.
    -   **Task Summary:** Displays a count of total tasks, completed tasks, and currently visible tasks.
    -   **Empty State:** Displays a message when no tasks are present or match current filters/search.
    -   **Dynamic Button States:** Buttons for bulk actions and clearing completed tasks are enabled/disabled based on the current state of the task list.

## How to Use/Run

**For `app.py` (Python Script):**

1.  **Save the file:** Save the provided Python code as `app.py` on your computer.
2.  **Run in a Python interpreter:**
    -   Open a terminal or command prompt.
    -   Navigate to the directory where you saved `app.py`.
    -   Start a Python interpreter by typing `python` (or `python3`).
    -   You can then import the functions and call them:
        ```python
        from app import add, subtract
        result_add = add(5, 3)
        print(f"5 + 3 = {result_add}") # Output: 5 + 3 = 8
        result_subtract = subtract(10, 4)
        print(f"10 - 4 = {result_subtract}") # Output: 10 - 4 = 6
        ```
    -   Alternatively, you can add print statements and function calls directly into `app.py` and run it:
        ```python
        # In app.py
        def add(a,b):
            return a + b
        def subtract(a,b):
            return a - b

        if __name__ == "__main__":
            print(f"2 + 2 = {add(2, 2)}")
            print(f"5 - 1 = {subtract(5, 1)}")
        ```
        Then, run from the terminal: `python app.py`

**For `sample-app.html` (Web Application):**

1.  **Save the file:** Save the provided HTML code as `sample-app.html` (or any `.html` extension) on your computer.
2.  **Open in a Web Browser:**
    -   Locate the saved `sample-app.html` file in your file explorer.
    -   Double-click the file. It will open automatically in your default web browser (e.g., Chrome, Firefox, Edge).
    -   Alternatively, open your web browser, go to `File > Open File` (or equivalent menu option), and select the `sample-app.html` file.

The application will load in your browser, and you can immediately start adding, managing, and interacting with tasks. All data is saved automatically in your browser's local storage.