# Codebase Documentation

This document provides a comprehensive overview of the codebase, adhering strictly to the provided files and their contents without inferring or inventing features.

## Overview

The codebase consists of two distinct applications: a command-line simple calculator written in Python, and a client-side web-based task manager application implemented using HTML, CSS, and JavaScript. The Python script provides basic arithmetic operations via a terminal interface, while the HTML file defines a web page with a user interface for managing tasks, including creation, editing, deletion, filtering, sorting, and data persistence in local storage, along with import/export capabilities.

## File Structure

- `app.py`: Contains the Python code for a simple command-line calculator.
- `sample-app.html`: Contains the HTML structure, CSS styling, and JavaScript functionality for a web-based task manager.

## File: app.py

This Python file implements a simple command-line calculator.

**Functions:**

- `add(a, b)`:
    - Takes two numerical arguments, `a` and `b`.
    - Returns their sum.
- `subtract(a, b)`:
    - Takes two numerical arguments, `a` and `b`.
    - Returns the difference of `a` minus `b`.
- `multiply(a, b)`:
    - Takes two numerical arguments, `a` and `b`.
    - Returns their product.
- `divide(a, b)`:
    - Takes two numerical arguments, `a` and `b`.
    - Returns the result of `a` divided by `b`.
    - Raises a `ValueError` if `b` is `0`.
- `calculate(a, b, operator)`:
    - Takes two numerical arguments `a`, `b`, and a string `operator`.
    - Calls the appropriate arithmetic function (`add`, `subtract`, `multiply`, `divide`) based on the `operator` string.
    - Supports `+`, `-`, `*`, `/` operators.
    - Raises a `ValueError` if an unsupported operator is provided.
- `main()`:
    - The main entry point for the calculator application.
    - Prints a welcome message and supported operators.
    - Prompts the user to enter two numbers and an operator via standard input.
    - Converts input numbers to `float`.
    - Calls `calculate` with the user inputs.
    - Prints the calculated `Result`.
    - Catches and prints `ValueError` exceptions that may occur during input conversion, division by zero, or unsupported operators.

**Execution:**

- The `if __name__ == "__main__":` block ensures that the `main()` function is called only when the script is executed directly (not when imported as a module).

## File: sample-app.html

This HTML file defines a web page for a task manager application. It includes embedded CSS for styling and embedded JavaScript for all interactive functionality.

## HTML Structure

The `sample-app.html` file defines the following structure:

- `<!doctype html>`: Declares an HTML5 document.
- `<html lang="en">`: The root element, specifying English language.
- `<head>`:
    - `<meta charset="UTF-8" />`: Specifies UTF-8 character encoding.
    - `<meta name="viewport" content="width=device-width, initial-scale=1.0" />`: Configures the viewport for responsive design.
    - `<title>Task Manager</title>`: Sets the title that appears in the browser tab.
    - `<style>`: Contains all the CSS styling for the page.
- `<body>`:
    - `<main class="app">`: The main container for the task manager application.
        - `<header>`:
            - `<h1>Demo AI Sync - Task Board</h1>`: The main heading of the application.
            - `<span id="clock"></span>`: An element to display the current time.
        - `<section class="content">`: Contains the main interactive elements and task list.
            - **Task Input Row:** (`<div class="row" style="grid-template-columns: 1fr 130px 130px auto;">`)
                - `<input id="taskInput" type="text" placeholder="Enter task..." />`: Input field for new task text.
                - `<select id="prioritySelect">`: Dropdown for selecting task priority (High, Medium, Low).
                - `<input id="dueDateInput" type="date" />`: Date input for task due date.
                - `<button id="addBtn">Add Task</button>`: Button to add a new task.
            - **Filter/Sort/Search Row:** (`<div class="row" style="grid-template-columns: 160px 160px 1fr auto;">`)
                - `<select id="filterSelect">`: Dropdown for filtering tasks (All, Active, Done).
                - `<select id="sortSelect">`: Dropdown for sorting tasks (Newest, Oldest, Priority, Due Date).
                - `<input id="searchInput" type="text" placeholder="Search tasks..." />`: Input field for searching tasks.
                - `<button id="clearCompletedBtn" class="button-clear">Clear Completed</button>`: Button to remove all completed tasks.
            - **Summary Row:** (`<div class="row" style="grid-template-columns: 1fr;">`)
                - `<div class="meta" id="summary">0 tasks</div>`: Displays a summary of tasks.
            - **Bulk Actions/Import/Export Row:** (`<div class="row" style="grid-template-columns: repeat(4, auto); justify-content: start;">`)
                - `<button id="markAllDoneBtn" class="button-clear">Mark All Done</button>`: Button to mark all tasks as done.
                - `<button id="markAllActiveBtn" class="button-clear">Mark All Active</button>`: Button to mark all tasks as active.
                - `<button id="exportBtn" class="button-clear">Export JSON</button>`: Button to export tasks as JSON.
                - `<button id="importBtn" class="button-clear">Import JSON</button>`: Button to trigger JSON import.
            - `<ul id="taskList"></ul>`: An unordered list where individual tasks are rendered.
            - `<div id="emptyState" class="empty">No tasks yet. Add your first task.</div>`: A message displayed when no tasks are present.
            - `<input id="importFileInput" type="file" accept="application/json" style="display:none;" />`: A hidden file input for importing JSON.
    - `<script>`: Contains all the JavaScript code for the task manager functionality.

## CSS Styling

The embedded `<style>` block in `sample-app.html` defines the visual appearance of the task manager.

**CSS Variables:**

- Defines several custom properties (CSS variables) in the `:root` pseudo-class for consistent theming: `--bg`, `--card`, `--text`, `--muted`, `--primary`, `--success`, `--danger`, `--border`.

**General Styling:**

- `*`: Global `box-sizing: border-box`.
- `body`: Sets `margin`, `font-family`, a `linear-gradient` background, text color, min-height, and uses CSS Grid for centering the app.
- `.app`: Styles the main application container with `width` constraints, background, border, `border-radius`, and `box-shadow`.
- `header`: Styles the application header with background, text color, padding, and uses flexbox for alignment.
- `header h1`: Resets margin and sets font size for the main title.
- `header span`: Styles the clock display.
- `.content`: Styles the main content area with padding and CSS Grid layout for its children.
- `.row`: Styles grid-based rows for layout, with varying `grid-template-columns` applied inline to specific `div.row` elements.

**Form Elements Styling:**

- `input`, `select`, `button`: Inherits font, sets `border-radius`, `border`, and `padding`.
- `input:focus`, `select:focus`: Adds outline and border color on focus.
- `button`: Sets `cursor`, removes `border`, applies `primary` background and white text, with `font-weight`.
- `.button-clear`: Styles a secondary button with a darker background.

**Task List Styling:**

- `ul`: Resets `list-style`, `margin`, `padding`, and uses CSS Grid for task items.
- `li`: Styles individual task items with border, `border-radius`, padding, CSS Grid, and `align-items`.
- `.meta`: Styles metadata text (color, font size, margin).
- `.badge`: Styles priority badges (inline-block, `border-radius`, padding, font size/weight).
- `.priority-high`, `.priority-medium`, `.priority-low`: Specific background and text colors for different priority levels.
- `.overdue`: Applies red text and bold font to overdue dates.
- `.controls`: Uses flexbox for layout of task action buttons.
- `.done`: Applies `text-decoration: line-through` and muted color for completed tasks.
- `.btn-success`, `.btn-danger`: Styles success and danger buttons with specific background colors.
- `.empty`: Styles the empty state message with padding, centered text, muted color, dashed border, and `border-radius`.

## JavaScript Functionality

The embedded `<script>` block in `sample-app.html` provides all the interactive functionality for the task manager.

**DOM Element References:**

- A collection of `const` variables are defined to hold references to various HTML elements by their `id`, facilitating DOM manipulation.

**Global State:**

- `STORAGE_KEY`: A string constant used as the key for `localStorage` to store task data.
- `tasks`: An array that holds all task objects in memory.

**Utility Functions:**

- `formatDateTime(d = new Date())`: Formats a `Date` object into a locale-specific string.
- `renderClock()`: Updates the `clock` span with the current formatted date and time.
- `createTask(text, priority, dueDate)`: Creates a new task object with a unique ID, text, priority, due date, `done` status, and `createdAt` timestamp.

**Data Persistence (Local Storage):**

- `saveTasks()`: Serializes the `tasks` array to a JSON string and saves it to `localStorage` using `STORAGE_KEY`.
- `loadTasks()`: Retrieves task data from `localStorage`, parses it, and populates the `tasks` array. It includes error handling and data cleaning to ensure valid task objects.

**Task Management Functions:**

- `addTask()`:
    - Gets task text, priority, and due date from input fields.
    - Creates a new task using `createTask`.
    - Adds the new task to the beginning of the `tasks` array.
    - Clears input fields.
    - Saves tasks and re-renders the UI.
    - Sets focus back to the task input.
- `toggleTask(id)`: Finds a task by ID and toggles its `done` status. Saves tasks and re-renders.
- `editTask(id)`: Prompts the user to edit a task's text, updates the task, saves, and re-renders.
- `removeTask(id)`: Finds a task by ID and removes it from the `tasks` array. Saves tasks and re-renders.
- `clearCompletedTasks()`: Iterates through the `tasks` array and removes all tasks where `done` is `true`. Saves tasks and re-renders.
- `markAllDone()`: Sets `done: true` for all tasks. Saves tasks and re-renders.
- `markAllActive()`: Sets `done: false` for all tasks. Saves tasks and re-renders.

**Import/Export Functions:**

- `exportTasks()`:
    - Creates a JSON `payload` containing `exportedAt` timestamp and the current `tasks` array.
    - Creates a `Blob` from the JSON string.
    - Creates a temporary anchor (`<a>`) element, sets its `href` to a URL for the blob, and `download` attribute for the filename.
    - Programmatically clicks the link to trigger the download.
    - Cleans up the temporary URL and anchor element.
- `importTasksFromFile(file)`:
    - Takes a `File` object as input.
    - Uses `FileReader` to read the file content as text.
    - On load, attempts to parse the JSON content.
    - Extracts `tasks` data, cleans it, and replaces the current `tasks` array with the imported ones.
    - Saves tasks and re-renders.
    - Displays an alert for invalid JSON format.

**Filtering, Sorting, and Searching:**

- `getFilteredTasks()`:
    - Applies filtering based on `filterSelect` (all, active, done).
    - Applies searching based on `searchInput` (case-insensitive text match).
    - Sorts the filtered tasks based on `sortSelect` (newest, oldest, priority, due date). Priority sorting uses a defined `priorityRank` object.

**Rendering Function:**

- `render()`:
    - Gets the list of filtered and sorted tasks using `getFilteredTasks()`.
    - Clears the current content of `taskList`.
    - Iterates through the `rows` (tasks):
        - Constructs HTML for each task item, including task text, priority badge, due date, created date, and control buttons (Done/Undo, Edit, Delete).
        - Determines if a task is `overdue` based on `dueDate` and `done` status.
        - Attaches event listeners to the "Done/Undo", "Edit", and "Delete" buttons for each task, calling `toggleTask`, `editTask`, and `removeTask` respectively.
        - Appends the generated `li` element to `taskList`.
    - Updates the `summary` text with task counts.
    - Toggles the visibility of the `emptyState` message based on the number of displayed tasks.
    - Disables/enables `clearCompletedBtn`, `markAllDoneBtn`, and `markAllActiveBtn` based on task counts and status.

**Event Listeners:**

- `addBtn` (click): Calls `addTask`.
- `taskInput` (keydown - Enter key): Calls `addTask`.
- `filterSelect` (change): Calls `render`.
- `sortSelect` (change): Calls `render`.
- `searchInput` (input): Calls `render`.
- `clearCompletedBtn` (click): Calls `clearCompletedTasks`.
- `markAllDoneBtn` (click): Calls `markAllDone`.
- `markAllActiveBtn` (click): Calls `markAllActive`.
- `exportBtn` (click): Calls `exportTasks`.
- `importBtn` (click): Triggers a click on the hidden `importFileInput`.
- `importFileInput` (change): Calls `importTasksFromFile` with the selected file.

**Initial Setup:**

- `loadTasks()`: Loads existing tasks from local storage on page load.
- `setInterval(renderClock, 1000)`: Updates the clock every second.
- `renderClock()`: Initial call to display the clock immediately.
- `render()`: Initial call to render the task list on page load.

## Features
- **Python Calculator:**
    - Addition of two numbers.
    - Subtraction of two numbers.
    - Multiplication of two numbers.
    - Division of two numbers (with zero-division error handling).
    - Command-line interface for inputting numbers and operator.
    - Error handling for invalid input or operations.
- **Web Task Manager:**
    - **Task Management:**
        - Add new tasks with text, priority (high, medium, low), and an optional due date.
        - Display a list of tasks.
        - Mark tasks as done or undo their completion status.
        - Edit existing task text.
        - Delete individual tasks.
        - Clear all completed tasks.
        - Mark all tasks as done.
        - Mark all tasks as active.
    - **Data Persistence:**
        - Tasks are saved to and loaded from the browser's local storage.
    - **Filtering and Sorting:**
        - Filter tasks by status (all, active, done).
        - Sort tasks by newest first, oldest first, priority (high > medium > low), or due date.
    - **Search:**
        - Search tasks by text (case-insensitive).
    - **Import/Export:**
        - Export all tasks to a JSON file.
        - Import tasks from a JSON file.
    - **User Interface:**
        - Displays a real-time clock.
        - Shows a summary of total tasks and completed tasks.
        - Displays a message when no tasks are present.
        - Buttons for bulk actions (Mark All Done, Mark All Active, Clear Completed) are dynamically enabled/disabled.
        - Visual indication for task priority (badges).
        - Visual indication for overdue tasks.
        - Visual indication for completed tasks (strike-through text).
        - Basic responsive styling.

## How to Use/Run

**For the Python Calculator (`app.py`):**

1.  Save the provided Python code as `app.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved `app.py`.
4.  Run the script using the Python interpreter:
    ```bash
    python app.py
    ```
5.  Follow the prompts to enter the first number, operator, and second number. The result or an error message will be printed to the console.

**For the Web Task Manager (`sample-app.html`):**

1.  Save the provided HTML code as `sample-app.html`.
2.  Open the `sample-app.html` file directly in a web browser (e.g., by double-clicking it in your file explorer).
3.  The task manager application will load in your browser.
4.  **Add a Task:**
    - Type a task description into the "Enter task..." input field.
    - Select a priority from the dropdown.
    - Select a due date using the date input.
    - Click the "Add Task" button or press `Enter` in the task input field.
5.  **Manage Tasks:**
    - Click "Done" to mark a task as completed, or "Undo" to revert.
    - Click "Edit" to modify a task's text.
    - Click "Delete" to remove a task.
6.  **Filter, Sort, and Search:**
    - Use the "Filter" dropdown to show "All", "Active", or "Done" tasks.
    - Use the "Sort" dropdown to change the order of tasks.
    - Type into the "Search tasks..." field to filter tasks by text.
7.  **Bulk Actions:**
    - Click "Clear Completed" to remove all tasks marked as done.
    - Click "Mark All Done" to mark every task as completed.
    - Click "Mark All Active" to mark every task as not completed.
8.  **Import/Export:**
    - Click "Export JSON" to download your current tasks as a `.json` file.
    - Click "Import JSON" to open a file dialog and select a `.json` file to load tasks from.
    - Tasks are automatically saved and loaded from your browser's local storage, so they will persist across browser sessions.