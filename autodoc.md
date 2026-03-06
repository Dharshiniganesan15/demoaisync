# Codebase Documentation

This document provides a comprehensive overview of the codebase, adhering strictly to the provided files and their contents without inferring or inventing features.

## Overview

The codebase consists of two distinct and independent applications: a simple command-line calculator implemented in Python, and a web-based Task Manager application implemented using HTML, CSS, and JavaScript. The Python script provides basic arithmetic operations, while the HTML file defines the structure, styling, and interactive functionality of a task management interface.

## File Structure

- `app.py`: Contains Python code for a command-line calculator.
- `sample-app.html`: Contains HTML structure, CSS styling, and JavaScript logic for a web-based Task Manager.

## File: app.py

This file contains Python code that implements a basic command-line calculator. It defines functions for arithmetic operations and a main function to handle user input and display results.

-   **`add(a, b)`**:
    -   Purpose: Adds two numbers.
    -   Parameters: `a` (number), `b` (number).
    -   Returns: The sum of `a` and `b`.
-   **`subtract(a, b)`**:
    -   Purpose: Subtracts the second number from the first.
    -   Parameters: `a` (number), `b` (number).
    -   Returns: The difference of `a` and `b`.
-   **`multiply(a, b)`**:
    -   Purpose: Multiplies two numbers.
    -   Parameters: `a` (number), `b` (number).
    -   Returns: The product of `a` and `b`.
-   **`divide(a, b)`**:
    -   Purpose: Divides the first number by the second.
    -   Parameters: `a` (number), `b` (number).
    -   Raises: `ValueError` if `b` is zero (division by zero is not allowed).
    -   Returns: The quotient of `a` and `b`.
-   **`calculate(a, b, operator)`**:
    -   Purpose: Performs an arithmetic operation based on the given operator.
    -   Parameters: `a` (number), `b` (number), `operator` (string representing "+", "-", "*", or "/").
    -   Raises: `ValueError` if the `operator` is not one of the supported types.
    -   Returns: The result of the specified operation.
-   **`main()`**:
    -   Purpose: Serves as the entry point for the calculator application.
    -   Prompts the user to enter two numbers and an operator.
    -   Calls `calculate()` to perform the operation.
    -   Prints the result or an error message if a `ValueError` occurs during input conversion or calculation.
-   **`if __name__ == "__main__":`**:
    -   This standard Python construct ensures that the `main()` function is called only when the script is executed directly, not when imported as a module.

## File: sample-app.html

This file contains the complete code for a web-based Task Manager application, encompassing its HTML structure, CSS styling, and JavaScript functionality.

## HTML Structure

The HTML structure defines the layout and content of the Task Manager interface.

-   **`<!doctype html>`**: Declares the document as an HTML5 document.
-   **`<html lang="en">`**: The root element, specifying the document language as English.
-   **`<head>`**:
    -   **`<meta charset="UTF-8" />`**: Specifies the character encoding for the document.
    -   **`<meta name="viewport" content="width=device-width, initial-scale=1.0" />`**: Configures the viewport for responsive design.
    -   **`<title>Task Manager</title>`**: Sets the title that appears in the browser tab.
    -   **`<style>`**: Contains inline CSS rules for styling the application (detailed in the CSS Styling section).
-   **`<body>`**:
    -   **`<main class="app">`**: The main container for the application.
        -   **`<header>`**: Displays the application title and a dynamic clock.
            -   **`<h1>Demo AI Sync - Task Board</h1>`**: The main title of the task board.
            -   **`<span id="clock"></span>`**: An element to display the current date and time.
        -   **`<section class="content">`**: The main content area where tasks are managed.
            -   **Task Input Row (`div.row`)**: Contains elements for adding new tasks.
                -   **`<input id="taskInput" type="text" placeholder="Enter task..." />`**: Text input for the task description.
                -   **`<select id="prioritySelect">`**: Dropdown for selecting task priority (High, Medium, Low).
                -   **`<input id="dueDateInput" type="date" />`**: Date input for the task's due date.
                -   **`<button id="addBtn">Add Task</button>`**: Button to add a new task.
            -   **Filter/Sort/Search Row (`div.row`)**: Contains elements for managing existing tasks.
                -   **`<select id="filterSelect">`**: Dropdown for filtering tasks by status (All, Active, Done).
                -   **`<select id="sortSelect">`**: Dropdown for sorting tasks (Newest, Oldest, Priority, Due Date).
                -   **`<input id="searchInput" type="text" placeholder="Search tasks..." />`**: Text input for searching tasks.
                -   **`<button id="clearCompletedBtn" class="button-clear">Clear Completed</button>`**: Button to remove all completed tasks.
            -   **Summary Row (`div.row`)**: Displays a summary of tasks.
                -   **`<div class="meta" id="summary">0 tasks</div>`**: Shows the total task count and done count.
            -   **Batch Actions Row (`div.row`)**: Contains buttons for bulk task actions.
                -   **`<button id="markAllDoneBtn" class="button-clear">Mark All Done</button>`**: Marks all tasks as complete.
                -   **`<button id="markAllActiveBtn" class="button-clear">Mark All Active</button>`**: Marks all tasks as active.
                -   **`<button id="exportBtn" class="button-clear">Export JSON</button>`**: Exports tasks to a JSON file.
                -   **`<button id="importBtn" class="button-clear">Import JSON</button>`**: Initiates task import from a JSON file.
            -   **`<ul id="taskList"></ul>`**: An unordered list where individual tasks will be rendered.
            -   **`<div id="emptyState" class="empty">No tasks yet. Add your first task.</div>`**: A message displayed when there are no tasks.
            -   **`<input id="importFileInput" type="file" accept="application/json" style="display:none;" />`**: A hidden file input for selecting JSON files for import.
-   **`<script>`**: Contains JavaScript code for the application's interactive functionality (detailed in the JavaScript Functionality section).

## CSS Styling

The embedded CSS uses custom properties (CSS variables) for a consistent theme and applies styles to various elements to create a modern and clean user interface.

-   **`:root`**: Defines custom properties for colors and borders:
    -   `--bg`: Background color.
    -   `--card`: Card background color.
    -   `--text`: Default text color.
    -   `--muted`: Muted text color.
    -   `--primary`: Primary action color.
    -   `--success`: Success action color.
    -   `--danger`: Danger action color.
    -   `--border`: Border color.
-   **`*`**: Sets `box-sizing: border-box` globally.
-   **`body`**:
    -   Resets `margin`, sets font family, applies a `linear-gradient` background, sets text color, and uses CSS Grid to center content vertically and horizontally.
-   **`.app`**:
    -   Styles the main application container: sets maximum width, background, border, border-radius, and box-shadow.
-   **`header`**:
    -   Styles the application header: dark background, white text, padding, and uses flexbox for alignment and spacing.
    -   `h1` and `span` within header are styled for font size and color.
-   **`.content`**:
    -   Styles the main content section: padding and grid layout with a gap.
-   **`.row`**:
    -   Styles container for grouping form elements: uses CSS Grid for horizontal arrangement.
-   **`input, select, button`**:
    -   Base styling for form controls: `font: inherit`, border-radius, border, and padding.
    -   `input:focus, select:focus`: Adds outline and changes border color on focus.
-   **`button`**:
    -   Default button styling: pointer cursor, no border, primary background, white text, and font weight.
-   **`.button-clear`**:
    -   Alternative button style with a dark gray background.
-   **`ul`**:
    -   Resets list-style, margin, padding, and uses grid layout for task items.
-   **`li`**:
    -   Styles individual task items: border, border-radius, padding, and uses grid layout for content and controls.
-   **`.meta`**:
    -   Styles metadata text (e.g., due date, created date): muted color and smaller font size.
-   **`.badge`**:
    -   Styles priority badges: inline-block, border-radius, padding, font size, and bold text.
-   **`.priority-high`, `.priority-medium`, `.priority-low`**:
    -   Specific background and text colors for high, medium, and low priority badges.
-   **`.overdue`**:
    -   Highlights overdue tasks with red color and bold text.
-   **`.controls`**:
    -   Styles the container for task action buttons: uses flexbox with a gap.
-   **`.done`**:
    -   Applies `text-decoration: line-through` and muted color to completed tasks.
-   **`.btn-success`, `.btn-danger`**:
    -   Specific background colors for success and danger buttons.
-   **`.empty`**:
    -   Styles the empty state message: padding, centered text, muted color, dashed border, and border-radius.

## JavaScript Functionality

The JavaScript code provides the dynamic behavior and interactivity for the Task Manager application.

-   **DOM Element References**:
    -   Numerous constants are defined to store references to key HTML elements (e.g., `taskInput`, `addBtn`, `taskList`, `filterSelect`, `summary`, `clock`, etc.) using `document.getElementById()`.
-   **`STORAGE_KEY`**: A constant string `"demoaisync_task_manager_v2"` used as the key for `localStorage`.
-   **`tasks`**: An array initialized as `[]` to store all task objects.
-   **`formatDateTime(d)`**:
    -   Formats a given `Date` object into a localized date and time string. Defaults to the current date if no date is provided.
-   **`renderClock()`**:
    -   Updates the `clock` span element with the current formatted date and time.
-   **`createTask(text, priority, dueDate)`**:
    -   Creates and returns a new task object with a unique `id` (using `crypto.randomUUID()`), `text`, `priority`, `dueDate`, `done` status (initially `false`), and `createdAt` timestamp.
-   **`saveTasks()`**:
    -   Saves the current `tasks` array to `localStorage` after converting it to a JSON string.
-   **`loadTasks()`**:
    -   Loads tasks from `localStorage`.
    -   Parses the JSON string, filters out invalid tasks, and populates the `tasks` array. Handles potential errors during parsing.
-   **`addTask()`**:
    -   Retrieves task details from input fields.
    -   If task text is not empty, a new task is created and added to the beginning of the `tasks` array.
    -   Input fields are cleared, tasks are saved, and the UI is re-rendered.
-   **`toggleTask(id)`**:
    -   Finds a task by its `id` and toggles its `done` status.
    -   Saves tasks and re-renders.
-   **`editTask(id)`**:
    -   Finds a task by its `id`.
    -   Prompts the user to edit the task's text. If input is valid, updates the task, saves, and re-renders.
-   **`removeTask(id)`**:
    -   Finds a task by its `id` and removes it from the `tasks` array.
    -   Saves tasks and re-renders.
-   **`clearCompletedTasks()`**:
    -   Iterates through the `tasks` array and removes all tasks where `done` is `true`.
    -   Saves tasks and re-renders.
-   **`markAllDone()`**:
    -   Sets the `done` status of all tasks to `true`.
    -   Saves tasks and re-renders.
-   **`markAllActive()`**:
    -   Sets the `done` status of all tasks to `false`.
    -   Saves tasks and re-renders.
-   **`exportTasks()`**:
    -   Creates a JSON payload containing `exportedAt` timestamp and the current `tasks` array.
    -   Creates a Blob from the JSON, generates a URL, and programmatically triggers a download of the JSON file with a dynamic filename.
-   **`importTasksFromFile(file)`**:
    -   Reads the content of a provided file using `FileReader`.
    -   On load, it attempts to parse the file content as JSON.
    -   It supports importing both a direct array of tasks or an object with a `tasks` property.
    -   Filters and maps incoming tasks to ensure data integrity and populates the `tasks` array.
    -   Saves tasks, re-renders, and alerts on invalid JSON format.
-   **`getFilteredTasks()`**:
    -   Filters tasks based on the `filterSelect` (all, active, done) and `searchInput` query.
    -   Sorts the filtered tasks based on `sortSelect` (newest, oldest, priority, due date). Priority sorting uses a defined `priorityRank`. Due date sorting handles unset dates.
    -   Returns the sorted and filtered list of tasks.
-   **`render()`**:
    -   This is the core rendering function that updates the UI based on the current `tasks` array and filter/sort settings.
    -   Clears existing tasks in `taskList`.
    -   Iterates through the `getFilteredTasks()` result to create `<li>` elements for each task.
    -   Each `<li>` displays task text, priority badge, due date (with "overdue" styling if applicable), and creation date.
    -   Dynamically creates "Done"/"Undo", "Edit", and "Delete" buttons for each task and attaches event listeners to them.
    -   Updates the `summary` text with task counts.
    -   Shows/hides the `emptyState` div based on whether there are tasks to display.
    -   Disables/enables `clearCompletedBtn`, `markAllDoneBtn`, and `markAllActiveBtn` based on task states.
-   **Event Listeners**:
    -   `addBtn` click and `taskInput` keydown (Enter): Trigger `addTask`.
    -   `filterSelect` change, `sortSelect` change, `searchInput` input: Trigger `render` to update task list based on new criteria.
    -   `clearCompletedBtn` click: Triggers `clearCompletedTasks`.
    -   `markAllDoneBtn` click: Triggers `markAllDone`.
    -   `markAllActiveBtn` click: Triggers `markAllActive`.
    -   `exportBtn` click: Triggers `exportTasks`.
    -   `importBtn` click: Simulates a click on the hidden `importFileInput`.
    -   `importFileInput` change: Triggers `importTasksFromFile` with the selected file.
-   **Initialization**:
    -   `loadTasks()`: Loads any previously saved tasks when the page loads.
    -   `setInterval(renderClock, 1000)`: Updates the clock every second.
    -   `renderClock()`: Initial call to display the clock immediately.
    -   `render()`: Initial call to display the task list.

## Features

-   **Command-line Calculator (from `app.py`)**:
    -   Performs addition, subtraction, multiplication, and division of two numbers.
    -   Handles division by zero error.
    -   Prompts for numerical inputs and operator.
    -   Displays calculation results or error messages.
-   **Web-based Task Manager (from `sample-app.html`)**:
    -   **Task Creation**: Add new tasks with a description, priority (High, Medium, Low), and an optional due date.
    -   **Task Management**:
        -   Mark tasks as completed or revert them to active.
        -   Edit the text of existing tasks.
        -   Delete individual tasks.
    -   **Task Viewing and Organization**:
        -   Filter tasks by status: all, active (incomplete), or done (completed).
        -   Sort tasks by creation date (newest/oldest), priority, or due date.
        -   Search tasks by keywords in their description.
    -   **Batch Actions**:
        -   Clear all completed tasks with a single click.
        -   Mark all existing tasks as done.
        -   Mark all existing tasks as active.
    -   **Persistence**: Tasks are automatically saved to and loaded from the browser's `localStorage` for data persistence across sessions.
    -   **Data Import/Export**:
        -   Export all tasks to a JSON file.
        -   Import tasks from a JSON file.
    -   **UI Indicators**:
        -   Displays a real-time clock in the header.
        -   Shows a summary of total tasks and completed tasks, and the number of currently displayed tasks.
        -   Indicates "overdue" tasks with distinct styling.
        -   Displays a message when no tasks are present or match current filters.
        -   Disables/enables certain buttons based on task state (e.g., "Clear Completed" is disabled if no tasks are done).

## How to Use/Run

**To run the Python Calculator (`app.py`):**

1.  Save the provided Python code into a file named `app.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved `app.py`.
4.  Run the script using the command: `python app.py`
5.  Follow the prompts to enter the first number, operator (`+`, `-`, `*`, or `/`), and the second number. The result will be printed to the console.

**To run the Web-based Task Manager (`sample-app.html`):**

1.  Save the provided HTML code into a file named `sample-app.html`.
2.  Open any modern web browser (e.g., Chrome, Firefox, Edge, Safari).
3.  Drag and drop the `sample-app.html` file into an open browser window or tab, or use the "Open File" option in your browser to select the file.
4.  The Task Manager application will load in your browser.
    -   **Add a Task**: Enter task text in the "Enter task..." input, select priority and due date, then click "Add Task".
    -   **Manage Tasks**: Use the "Done", "Edit", and "Delete" buttons next to each task.
    -   **Filter/Sort/Search**: Use the dropdowns and search input at the top to organize your task list.
    -   **Batch Actions**: Use the "Clear Completed", "Mark All Done", and "Mark All Active" buttons for bulk operations.
    -   **Import/Export**: Use "Export JSON" to save your tasks, and "Import JSON" to load tasks from a file (which will open a file selection dialog).