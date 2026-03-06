# Codebase Documentation

This document provides a comprehensive overview of the codebase, adhering strictly to the provided files and their contents without inferring or inventing features.

## Overview

This codebase consists of two distinct applications: a command-line calculator written in Python and a browser-based Task Manager application implemented with HTML, CSS, and JavaScript. The Python application provides basic arithmetic operations and a calculation history. The Task Manager is a single-page web application that allows users to create, manage, filter, sort, and persist tasks locally in the browser.

## File Structure

-   `app.py`: Contains the Python code for a command-line calculator.
-   `sample-app.html`: Contains the HTML structure, CSS styling, and JavaScript logic for a web-based Task Manager.

## File: app.py

This Python script implements a simple command-line calculator. It defines several functions for basic arithmetic operations, a central `calculate` function to dispatch operations, and functions for managing and printing calculation history. The `main` function orchestrates the user interaction, allowing continuous calculations until the user decides to exit.

-   `add(a, b)`: Returns the sum of `a` and `b`.
-   `subtract(a, b)`: Returns the difference of `a` and `b`.
-   `multiply(a, b)`: Returns the product of `a` and `b`.
-   `divide(a, b)`: Returns the quotient of `a` divided by `b`. Raises a `ValueError` if `b` is zero.
-   `modulo(a, b)`: Returns the remainder of `a` divided by `b`. Raises a `ValueError` if `b` is zero.
-   `power(a, b)`: Returns `a` raised to the power of `b`.
-   `floor_divide(a, b)`: Returns the floor division of `a` by `b`. Raises a `ValueError` if `b` is zero.
-   `calculate(a, b, operator)`: A dispatcher function that takes two numbers (`a`, `b`) and an `operator` string. It calls the appropriate arithmetic function based on the operator. Supported operators are `+`, `-`, `*`, `/`, `%`, `^`, `//`. Raises a `ValueError` for unsupported operators.
-   `print_history(history)`: Prints the list of past calculations stored in the `history` list. If the history is empty, it prints "No calculations yet."
-   `main()`: The main entry point for the calculator application. It displays a welcome message, supported operators, and instructions. It enters a loop to prompt the user for numbers and operators, performs calculations using `calculate`, stores expressions in a `history` list, and prints results. It handles `ValueError` for invalid inputs or operations (like division by zero). Users can type 'history' to view past calculations or 'exit' to quit.
-   `if __name__ == "__main__":`: This block ensures that the `main()` function is called only when the script is executed directly (not when imported as a module).

## File: sample-app.html

This file defines a single-page web application for a Task Manager. It combines HTML for structure, CSS for styling, and JavaScript for dynamic functionality, all embedded within a single HTML file.

The HTML defines the layout of the task manager, including a header, input fields for new tasks (text, priority, due date), controls for filtering and sorting tasks, buttons for various actions (add, clear completed, mark all done/active, export/import), a list to display tasks, and an empty state message.

The CSS styles the application to provide a clean and responsive user interface. It uses CSS variables for theme colors and defines styles for layout, form elements, task items, and various status indicators (priority, overdue, done).

The JavaScript provides the interactive logic:
-   It manages a list of tasks, stored persistently using `localStorage`.
-   It includes functions for adding, toggling completion, editing, removing tasks, and bulk actions like marking all done or active, and clearing completed tasks.
-   It implements filtering tasks by status (all, active, done), sorting tasks by creation date, priority, or due date, and searching tasks by text content.
-   It includes functionality to export tasks to a JSON file and import tasks from a JSON file.
-   A real-time clock is displayed in the header.
-   The `render` function updates the UI based on the current state of tasks, filters, and sorts.

## HTML Structure

The HTML document starts with a standard `<!doctype html>` declaration and an `<html>` element with `lang="en"`.

The `<head>` section includes:
-   `meta` tags for character set (`UTF-8`) and viewport configuration.
-   A `<title>` tag setting the page title to "Task Manager".
-   An embedded `<style>` block containing all the CSS rules for the application.

The `<body>` section contains the main content:
-   A `<main>` element with class `app` serves as the primary container for the entire application.
-   Inside `main`, a `<header>` element displays the application title "Demo AI Sync - Task Board" and includes a `<span>` with `id="clock"` for displaying the current time.
-   A `<section>` element with class `content` encapsulates the main interactive components:
    -   Multiple `<div>` elements with class `row` organize input fields and buttons into horizontal layouts.
    -   The first `row` contains:
        -   An `<input type="text" id="taskInput">` for entering new task descriptions.
        -   A `<select id="prioritySelect">` for choosing task priority (High, Medium, Low).
        -   An `<input type="date" id="dueDateInput">` for setting a task's due date.
        -   A `<button id="addBtn">` to add a new task.
    -   The second `row` contains:
        -   A `<select id="filterSelect">` for filtering tasks by status (All, Active, Done).
        -   A `<select id="sortSelect">` for sorting tasks (Newest, Oldest, Priority, Due Date).
        -   An `<input type="text" id="searchInput">` for searching tasks.
        -   A `<button id="clearCompletedBtn" class="button-clear">` to clear completed tasks.
    -   A third `row` contains a `div` with `id="summary"` to display task statistics.
    -   A fourth `row` contains buttons for bulk actions:
        -   `<button id="markAllDoneBtn" class="button-clear">` to mark all tasks as done.
        -   `<button id="markAllActiveBtn" class="button-clear">` to mark all tasks as active.
        -   `<button id="exportBtn" class="button-clear">` to export tasks.
        -   `<button id="importBtn" class="button-clear">` to import tasks.
    -   An unordered list (`<ul id="taskList">`) is where individual task items are rendered.
    -   A `<div>` with `id="emptyState"` and class `empty` is displayed when there are no tasks.
    -   An `<input type="file" id="importFileInput">` is hidden and used for selecting a JSON file for import.
-   Finally, a `<script>` block is embedded at the end of the `<body>` to contain all the JavaScript logic, ensuring that the DOM is fully loaded before scripts attempt to access elements.

## CSS Styling

The embedded `<style>` block defines the visual appearance of the Task Manager.

-   **CSS Variables**: A `:root` selector defines several custom properties (CSS variables) for colors, including background (`--bg`), card background (`--card`), text (`--text`), muted text (`--muted`), primary color (`--primary`), success color (`--success`), danger color (`--danger`), and border color (`--border`).
-   **Universal Box Sizing**: `* { box-sizing: border-box; }` ensures consistent box model behavior.
-   **Body Styling**: `body` sets `margin: 0`, a system font stack, a linear gradient background, default text color, minimum height, and centers the content using `display: grid` and `place-items: center`.
-   **App Container**: `.app` defines the main application card, setting its width, background, border, border-radius, and box-shadow. It also handles `overflow: hidden`.
-   **Header Styling**: `header` sets a dark background, white text, padding, and uses flexbox for alignment and spacing of its child elements. `h1` and `span` inside the header are also styled.
-   **Content Section**: `.content` provides padding and uses `display: grid` with `gap` for internal spacing.
-   **Row Layouts**: `.row` uses `display: grid` with `gap` for horizontal alignment of form elements. Specific `grid-template-columns` values are applied inline to some `.row` elements to control column widths.
-   **Form Elements**: `input`, `select`, and `button` elements share styles for font inheritance, border-radius, border, and padding. Focus states for `input` and `select` are defined with an outline and border color change.
-   **Buttons**: `button` elements have `cursor: pointer`, no border, default background `var(--primary)`, white text, and font-weight. A `.button-clear` class provides an alternative dark background.
-   **Task List**: `ul` removes default list styling and uses `display: grid` with `gap`. `li` elements are styled as individual cards with borders, padding, and a grid layout for content and controls.
-   **Metadata**: `.meta` is for secondary text, setting `color` and `font-size`.
-   **Badges**: `.badge` styles small labels, defining `display: inline-block`, border-radius, padding, font-size, and font-weight.
    -   `priority-high`, `priority-medium`, `priority-low` classes define specific background and text colors for priority badges.
-   **Overdue Indicator**: `.overdue` styles text to be red and bold for overdue tasks.
-   **Controls**: `.controls` uses flexbox to arrange action buttons within a task item.
-   **Done State**: `.done` applies `text-decoration: line-through` and changes text color for completed tasks.
-   **Action Buttons**: `.btn-success` and `.btn-danger` classes define green and red backgrounds respectively for specific action buttons.
-   **Empty State**: `.empty` styles the message displayed when no tasks are present, using padding, centered text, muted color, and a dashed border.

## JavaScript Functionality

The JavaScript code provides the dynamic behavior for the Task Manager application.

-   **DOM Element References**: Numerous `const` variables are defined to hold references to key HTML elements by their `id` (e.g., `taskInput`, `addBtn`, `taskList`, `filterSelect`, `summary`, `clock`).
-   **Storage Key and Task Array**:
    -   `STORAGE_KEY`: A constant string used as the key for `localStorage` to persist tasks.
    -   `tasks`: An array that holds all task objects in memory.
-   **`formatDateTime(d)`**: A utility function to format a `Date` object into a localized date and time string.
-   **`renderClock()`**: Updates the `clock` element in the header with the current formatted date and time. It is called every second using `setInterval`.
-   **`createTask(text, priority, dueDate)`**: Creates a new task object with a unique `id` (using `crypto.randomUUID()`), trimmed `text`, `priority`, `dueDate`, `done` status (initially `false`), and `createdAt` timestamp.
-   **`saveTasks()`**: Serializes the `tasks` array to a JSON string and saves it to `localStorage` using the `STORAGE_KEY`.
-   **`loadTasks()`**: Retrieves the task data from `localStorage`, parses it as JSON, and populates the `tasks` array. It includes error handling and ensures data consistency by filtering and mapping task objects to a defined structure.
-   **`addTask()`**: Adds a new task to the `tasks` array. It retrieves the task text, priority, and due date from the input fields, creates a task object, unshifts it to the `tasks` array, clears input fields, saves tasks, renders the UI, and sets focus back to the task input.
-   **`toggleTask(id)`**: Finds a task by its `id` and flips its `done` status. It then saves tasks and re-renders.
-   **`editTask(id)`**: Prompts the user to edit a task's text. If a valid new text is provided, it updates the task, saves, and re-renders.
-   **`removeTask(id)`**: Finds a task by its `id` and removes it from the `tasks` array. It then saves tasks and re-renders.
-   **`clearCompletedTasks()`**: Iterates through the `tasks` array and removes all tasks where `done` is `true`. Saves and re-renders.
-   **`markAllDone()`**: Sets the `done` status of all tasks to `true`. Saves and re-renders.
-   **`markAllActive()`**: Sets the `done` status of all tasks to `false`. Saves and re-renders.
-   **`exportTasks()`**: Creates a JSON blob containing the current `tasks` array and an `exportedAt` timestamp. It then creates a temporary anchor (`<a>`) element, sets its `href` to a URL created from the blob, sets a download filename, simulates a click, and then cleans up the temporary elements and URL.
-   **`importTasksFromFile(file)`**: Reads the content of a selected file (expected to be JSON). Upon successful load, it parses the JSON, validates its structure (expecting an array of tasks or an object with a `tasks` property), cleans the incoming task data, replaces the current `tasks` array, saves, and re-renders. It alerts the user on invalid JSON.
-   **`getFilteredTasks()`**: Applies filtering, searching, and sorting logic to the `tasks` array based on the current values of `filterSelect`, `searchInput`, and `sortSelect`.
    -   **Filtering**: Filters by `active` (not done) or `done` status.
    -   **Searching**: Filters by text content (case-insensitive).
    -   **Sorting**: Sorts tasks based on `newest` (default, `createdAt` descending), `oldest` (`createdAt` ascending), `priority` (High > Medium > Low), or `due` date (ascending, with unset due dates at the end).
-   **`render()`**: This is the core function for updating the UI.
    -   It calls `getFilteredTasks()` to get the list of tasks to display.
    -   It clears the `taskList` HTML.
    -   For each task, it dynamically creates an `<li>` element with task details (text, priority badge, due date, created date) and control buttons (Done/Undo, Edit, Delete). It applies `done` class for completed tasks and `overdue` class for overdue tasks.
    -   Event listeners are attached to the `Done/Undo`, `Edit`, and `Delete` buttons for each task, calling `toggleTask`, `editTask`, and `removeTask` respectively.
    -   It updates the `summary` text to show total tasks, done tasks, and currently showing tasks.
    -   It manages the visibility of the `emptyState` message.
    -   It enables/disables and adjusts opacity/cursor for `clearCompletedBtn`, `markAllDoneBtn`, and `markAllActiveBtn` based on the current task states.
-   **Event Listeners**:
    -   `addBtn` `click`: Calls `addTask`.
    -   `taskInput` `keydown` (Enter key): Calls `addTask`.
    -   `filterSelect` `change`: Calls `render`.
    -   `sortSelect` `change`: Calls `render`.
    -   `searchInput` `input`: Calls `render`.
    -   `clearCompletedBtn` `click`: Calls `clearCompletedTasks`.
    -   `markAllDoneBtn` `click`: Calls `markAllDone`.
    -   `markAllActiveBtn` `click`: Calls `markAllActive`.
    -   `exportBtn` `click`: Calls `exportTasks`.
    -   `importBtn` `click`: Triggers a click on the hidden `importFileInput`.
    -   `importFileInput` `change`: Calls `importTasksFromFile` with the selected file and resets the input value.
-   **Initial Setup**:
    -   `loadTasks()`: Loads tasks from `localStorage` on page load.
    -   `setInterval(renderClock, 1000)`: Sets up the clock to update every second.
    -   `renderClock()`: Calls `renderClock` once immediately to display the time without delay.
    -   `render()`: Renders the initial state of the task list on page load.

## Features

-   **Python Calculator (`app.py`)**:
    -   Performs basic arithmetic operations: addition, subtraction, multiplication, division, modulo, exponentiation (power), and floor division.
    -   Includes error handling for division/modulo by zero and unsupported operators.
    -   Maintains a history of all successful calculations.
    -   Allows users to view calculation history.
    -   Provides a command-line interface for user interaction.
-   **Web Task Manager (`sample-app.html`)**:
    -   Create new tasks with a description, priority (High, Medium, Low), and an optional due date.
    -   Display tasks in a list.
    -   Toggle task completion status (mark as done/undo).
    -   Edit existing task descriptions.
    -   Delete individual tasks.
    -   Filter tasks by status: all, active (not done), or done.
    -   Sort tasks by creation date (newest/oldest), priority, or due date.
    -   Search tasks by text content.
    -   Clear all completed tasks.
    -   Mark all tasks as done.
    -   Mark all tasks as active (not done).
    -   Export all tasks to a JSON file.
    -   Import tasks from a JSON file.
    -   Persist tasks locally using `localStorage` in the browser.
    -   Display a real-time clock in the header.
    -   Indicate overdue tasks visually.
    -   Provide visual feedback for empty task lists.
    -   Dynamically enable/disable action buttons based on task state (e.g., "Clear Completed" is disabled if no tasks are done).

## How to Use/Run

**To use the Python Calculator (`app.py`):**

1.  Save the provided Python code into a file named `app.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where `app.py` is saved.
4.  Run the script using the Python interpreter:
    ```bash
    python app.py
    ```
5.  Follow the prompts to enter numbers and operators.
6.  Type `history` to view past calculations or `exit` to quit the program.

**To use the Web Task Manager (`sample-app.html`):**

1.  Save the provided HTML code into a file named `sample-app.html`.
2.  Open this `sample-app.html` file in any modern web browser (e.g., Chrome, Firefox, Edge, Safari).
3.  The Task Manager interface will load. You can then:
    -   Enter a task description, select priority and due date, then click "Add Task" or press Enter in the task input field.
    -   Use the dropdowns to filter or sort tasks.
    -   Use the search bar to find tasks.
    -   Click the "Done", "Edit", or "Delete" buttons next to each task.
    -   Use the bulk action buttons like "Clear Completed", "Mark All Done", "Mark All Active", "Export JSON", or "Import JSON".
    -   Tasks will be automatically saved and loaded from your browser's local storage.