# Codebase Documentation

This document provides a comprehensive overview of the codebase, adhering strictly to the provided files and their contents without inferring or inventing features.

## Overview

The codebase consists of two independent applications:
1.  A command-line calculator written in Python (`app.py`).
2.  A web-based task manager implemented as a single HTML file (`sample-app.html`), incorporating HTML structure, CSS styling, and JavaScript functionality.

These two applications do not interact with each other.

## File Structure

-   `app.py`: Contains the Python code for a command-line calculator.
-   `sample-app.html`: Contains the HTML structure, CSS styling, and JavaScript logic for a web-based task manager.

## File: app.py

This file contains Python code implementing a simple command-line calculator application.

**Functions:**

*   `add(a, b)`: Returns the sum of `a` and `b`.
*   `subtract(a, b)`: Returns the difference of `a` and `b`.
*   `multiply(a, b)`: Returns the product of `a` and `b`.
*   `divide(a, b)`: Returns the quotient of `a` and `b`. Raises `ValueError` if `b` is zero.
*   `modulo(a, b)`: Returns the remainder of the division of `a` by `b`. Raises `ValueError` if `b` is zero.
*   `power(a, b)`: Returns `a` raised to the power of `b`.
*   `floor_divide(a, b)`: Returns the floor division of `a` by `b`. Raises `ValueError` if `b` is zero.
*   `calculate(a, b, operator)`: Takes two numbers `a`, `b` and an `operator` string. It dispatches to the appropriate arithmetic function based on the operator. Supported operators are `+`, `-`, `*`, `/`, `%`, `^`, `//`. Raises `ValueError` for unsupported operators.
*   `print_history(history)`: Prints the list of past calculations. If the history is empty, it prints "No calculations yet.".
*   `main()`: The main entry point of the calculator application.
    *   It prints a welcome message and lists supported operators.
    *   It maintains a `history` list to store calculation expressions.
    *   It enters a loop that prompts the user for the first number, operator, and second number.
    *   Users can type `'exit'` to quit the application or `'history'` to view past calculations.
    *   It attempts to convert user input to `float` and perform calculations using the `calculate` function.
    *   Successful calculations are added to the `history` list and the result is printed.
    *   It catches `ValueError` for invalid input or operations (like division by zero) and prints an error message.

**Execution:**

The `if __name__ == "__main__":` block ensures that the `main()` function is called only when the script is executed directly.

## File: sample-app.html

This file is a self-contained web application for managing tasks. It includes the HTML structure, CSS styling, and JavaScript functionality within a single file.

## HTML Structure

The HTML document defines the structure of a "Task Manager" application.

*   **Document Setup:** Standard HTML5 boilerplate with `lang="en"`, `meta` tags for charset and viewport, and a `<title>` of "Task Manager".
*   **Main Container:** A `<main>` element with class `app` serves as the primary container for the application interface.
*   **Header:**
    *   A `<header>` element inside `main` contains an `<h1>` with "Demo AI Sync - Task Board" and a `<span>` with `id="clock"` to display a live clock.
*   **Content Section:**
    *   A `<section>` with class `content` holds all interactive elements and the task list.
    *   **Task Input Row:** A `div` with class `row` contains:
        *   An `<input>` field (`id="taskInput"`) for entering task descriptions.
        *   A `<select>` element (`id="prioritySelect"`) for choosing task priority (High, Medium, Low).
        *   An `<input>` field (`id="dueDateInput"`, type="date") for selecting a due date.
        *   A `<button>` (`id="addBtn"`) to add tasks.
    *   **Filter/Sort/Search Row:** Another `div` with class `row` contains:
        *   A `<select>` (`id="filterSelect"`) for filtering tasks by status (All, Active, Done).
        *   A `<select>` (`id="sortSelect"`) for sorting tasks (Newest, Oldest, Priority, Due Date).
        *   An `<input>` field (`id="searchInput"`) for searching tasks by text.
        *   A `<button>` (`id="clearCompletedBtn"`) to clear completed tasks.
    *   **Summary Row:** A `div` with class `row` contains a `div` (`id="summary"`) to display task summary information (e.g., "0 tasks").
    *   **Bulk Actions Row:** A `div` with class `row` contains buttons for bulk actions:
        *   `Mark All Done` (`id="markAllDoneBtn"`)
        *   `Mark All Active` (`id="markAllActiveBtn"`)
        *   `Export JSON` (`id="exportBtn"`)
        *   `Import JSON` (`id="importBtn"`)
    *   **Task List:** An unordered list (`<ul id="taskList">`) where individual tasks will be dynamically rendered.
    *   **Empty State:** A `div` (`id="emptyState"`) with class `empty` to be displayed when no tasks are present.
    *   **Hidden File Input:** An `<input>` field (`id="importFileInput"`, type="file") for importing JSON, hidden by default.

## CSS Styling

The CSS styling is embedded within a `<style>` block in the `<head>` of `sample-app.html`.

*   **CSS Variables:** Defines a set of custom properties (CSS variables) in `:root` for consistent colors (background, card, text, muted, primary, success, danger, border).
*   **Global Reset/Base Styles:**
    *   `*`: Sets `box-sizing: border-box`.
    *   `body`: Resets margin, sets font family, applies a linear gradient background, sets text color, centers content vertically and horizontally, and adds padding.
*   **App Container (`.app`):** Styles the main application container as a card with a maximum width, background, border, border-radius, and box-shadow.
*   **Header:** Styles the header with a dark background, white text, padding, and uses flexbox for alignment and spacing.
*   **Content Area (`.content`):** Sets padding and uses CSS grid for layout with a gap between grid items.
*   **Row Layouts (`.row`):** Uses CSS grid to arrange elements in rows, with specific column definitions for different sections (e.g., task input row, filter row).
*   **Form Elements (`input`, `select`, `button`):** Provides consistent styling for font, border-radius, border, padding, and focus states.
*   **Buttons:**
    *   Default `button` styles for cursor, border, background, color, and font weight.
    *   `.button-clear`: Specific styles for a "clear" button with a dark background.
    *   `.btn-success`, `.btn-danger`: Styles for success (green) and danger (red) themed buttons.
*   **Task List (`ul`, `li`):**
    *   `ul`: Removes default list styling, resets margin/padding, and uses CSS grid for item spacing.
    *   `li`: Styles individual task items with borders, rounded corners, padding, and uses CSS grid to arrange task details and controls.
*   **Meta Information (`.meta`):** Styles for secondary text, typically used for dates and priority badges.
*   **Badges (`.badge`):** General styling for small informational labels.
*   **Priority Badges (`.priority-high`, `.priority-medium`, `.priority-low`):** Specific background and text colors for different priority levels.
*   **Overdue Text (`.overdue`):** Highlights overdue text with a danger color and bold font.
*   **Controls (`.controls`):** Uses flexbox for layout of action buttons within a task item.
*   **Done Tasks (`.done`):** Applies line-through text decoration and a muted color to completed tasks.
*   **Empty State (`.empty`):** Styles the message displayed when no tasks are present, with centering, muted color, dashed border, and padding.

## JavaScript Functionality

The JavaScript code is embedded within a `<script>` block at the end of `sample-app.html`. It implements the interactive logic for the task manager.

*   **DOM Element References:** Stores references to various HTML elements by their IDs (e.g., `taskInput`, `addBtn`, `taskList`, `summary`, `clock`).
*   **Constants:**
    *   `STORAGE_KEY`: A string used as the key for storing tasks in `localStorage`.
    *   `tasks`: An array that holds all task objects.
*   **Utility Functions:**
    *   `formatDateTime(d)`: Formats a `Date` object into a localized date and time string.
    *   `renderClock()`: Updates the `clock` span with the current formatted date and time.
*   **Task Management Core Logic:**
    *   `createTask(text, priority, dueDate)`: Generates a new task object with a unique `id` (using `crypto.randomUUID()`), `text`, `priority`, `dueDate`, `done` status (initially `false`), and `createdAt` timestamp.
    *   `saveTasks()`: Serializes the `tasks` array to a JSON string and saves it to `localStorage` using `STORAGE_KEY`.
    *   `loadTasks()`: Retrieves tasks from `localStorage`, parses the JSON, and populates the `tasks` array. It includes error handling and a data cleaning/migration step to ensure task objects have expected properties and structure.
*   **Task Actions:**
    *   `addTask()`: Retrieves values from `taskInput`, `prioritySelect`, and `dueDateInput`. If `taskInput` is not empty, it creates a new task using `createTask`, adds it to the beginning of the `tasks` array, clears the input fields, saves tasks, and triggers a `render`.
    *   `toggleTask(id)`: Finds a task by `id` and flips its `done` status. Saves tasks and triggers a `render`.
    *   `editTask(id)`: Prompts the user to edit a task's text. If input is valid, updates the task, saves, and re-renders.
    *   `removeTask(id)`: Finds a task by `id` and removes it from the `tasks` array. Saves tasks and triggers a `render`.
    *   `clearCompletedTasks()`: Iterates through the `tasks` array and removes all tasks where `done` is `true`. Saves tasks and triggers a `render`.
    *   `markAllDone()`: Sets the `done` status of all tasks to `true`. Saves tasks and triggers a `render`.
    *   `markAllActive()`: Sets the `done` status of all tasks to `false`. Saves tasks and triggers a `render`.
    *   `exportTasks()`: Creates a JSON blob containing the current `tasks` and `exportedAt` timestamp. It then creates a temporary anchor element (`<a>`), sets its `href` to a URL created from the blob, and programmatically clicks it to trigger a file download.
    *   `importTasksFromFile(file)`: Reads a provided file as text. Upon loading, it attempts to parse the content as JSON. It expects either an array of tasks or an object with a `tasks` property that is an array. It cleans/maps the incoming tasks, replaces the current `tasks` array, saves, and triggers a `render`. It alerts the user if the file is not valid JSON.
*   **Filtering and Sorting:**
    *   `getFilteredTasks()`: Applies filtering and sorting logic to the `tasks` array.
        *   **Filtering:** Filters by task status (`all`, `active`, `done`) and by a search query (case-insensitive substring match against task text).
        *   **Sorting:** Sorts tasks based on the `sortSelect` value: `newest` (by `createdAt` descending), `oldest` (by `createdAt` ascending), `priority` (High > Medium > Low), or `due` (earliest `dueDate` first, tasks without due dates appear last).
*   **Rendering (`render()`):**
    *   Retrieves the currently filtered and sorted tasks using `getFilteredTasks()`.
    *   Clears the `taskList` HTML content.
    *   Iterates through each task:
        *   Dynamically creates an `<li>` element.
        *   Determines if a task is `overdue` based on its `dueDate` and `done` status.
        *   Populates the `<li>`'s `innerHTML` with task text, priority badge, due date, creation date, and action buttons ("Done"/"Undo", "Edit", "Delete").
        *   Attaches event listeners to the dynamically created buttons (`toggleTask`, `editTask`, `removeTask`).
        *   Appends the `<li>` to the `taskList`.
    *   Updates the `summary` text with task counts (total, done, showing).
    *   Controls the visibility of the `emptyState` message.
    *   Disables/enables `clearCompletedBtn`, `markAllDoneBtn`, and `markAllActiveBtn` based on the current state of tasks (e.g., `clearCompletedBtn` is disabled if no tasks are done).
*   **Event Listeners:**
    *   `addBtn` click: calls `addTask`.
    *   `taskInput` keydown (Enter key): calls `addTask`.
    *   `filterSelect` change: calls `render`.
    *   `sortSelect` change: calls `render`.
    *   `searchInput` input: calls `render`.
    *   `clearCompletedBtn` click: calls `clearCompletedTasks`.
    *   `markAllDoneBtn` click: calls `markAllDone`.
    *   `markAllActiveBtn` click: calls `markAllActive`.
    *   `exportBtn` click: calls `exportTasks`.
    *   `importBtn` click: programmatically clicks the hidden `importFileInput`.
    *   `importFileInput` change: calls `importTasksFromFile` with the selected file.
*   **Initialization:**
    *   `loadTasks()` is called to load any previously saved tasks when the script starts.
    *   `setInterval(renderClock, 1000)` sets up the clock to update every second.
    *   `renderClock()` is called once immediately to display the clock.
    *   `render()` is called once immediately to display the initial task list.

## Features

This codebase provides the following features:

**From `app.py` (Command-Line Calculator):**
-   Performs basic arithmetic operations: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
-   Supports advanced arithmetic operations: modulo (`%`), exponentiation (`^`), and floor division (`//`).
-   Includes error handling for division by zero scenarios for `/`, `%`, and `//` operators.
-   Stores a history of all successful calculations.
-   Allows users to view the calculation history at any point by typing 'history'.
-   Provides an option to exit the application by typing 'exit'.
-   Handles non-numeric input gracefully with error messages.

**From `sample-app.html` (Web-Based Task Manager):**
-   **Task Creation:** Add new tasks with a text description, priority (High, Medium, Low), and an optional due date.
-   **Task Management:**
    -   Toggle the completion status of individual tasks (mark as "Done" or "Undo").
    -   Edit the text content of existing tasks.
    -   Delete individual tasks.
-   **Bulk Actions:**
    -   Clear all completed tasks.
    -   Mark all tasks as done.
    -   Mark all tasks as active (not done).
-   **Filtering:** Filter tasks by status: all tasks, active tasks, or completed tasks.
-   **Sorting:** Sort tasks by:
    -   Newest (creation date, descending)
    -   Oldest (creation date, ascending)
    -   Priority (High, Medium, Low)
    -   Due Date (earliest first)
-   **Search:** Search tasks by keywords in their text description.
-   **Persistence:** Tasks are automatically saved to and loaded from the browser's local storage, ensuring data persists across sessions.
-   **User Interface:**
    -   Displays tasks with their text, priority (indicated by a badge), due date, and creation timestamp.
    -   Visually indicates completed tasks by striking through their text.
    -   Visually highlights overdue tasks.
    -   Displays a live clock in the application header.
    -   Provides a dynamic summary of tasks (total, done, and currently displayed tasks).
    -   Shows an "empty state" message when no tasks match the current filters or if the list is empty.
    -   Disables relevant control buttons (e.g., "Clear Completed," "Mark All Done") when their action is not applicable.
-   **Import/Export:**
    -   Export all current tasks to a JSON file.
    -   Import tasks from a JSON file, replacing the current task list.

## How to Use/Run

**To use the Python Calculator (`app.py`):**

1.  **Save the file:** Save the provided Python code as `app.py` on your computer.
2.  **Open a terminal/command prompt:** Navigate to the directory where you saved `app.py`.
3.  **Run the script:** Execute the script using a Python interpreter:
    ```bash
    python app.py
    ```
4.  **Interact:** Follow the prompts in the terminal:
    *   Enter the first number.
    *   Enter the operator (`+`, `-`, `*`, `/`, `%`, `^`, `//`).
    *   Enter the second number.
    *   To view calculation history, type `history` when prompted for the first number.
    *   To exit the application, type `exit` when prompted for the first number.

**To use the Web-Based Task Manager (`sample-app.html`):**

1.  **Save the file:** Save the provided HTML code as `sample-app.html` on your computer.
2.  **Open in a web browser:** Locate the saved `sample-app.html` file and open it with any modern web browser (e.g., Chrome, Firefox, Edge, Safari). You can usually do this by double-clicking the file.
3.  **Interact:**
    *   **Add Tasks:** Type a task description into the "Enter task..." input field, select a priority and an optional due date, then click "Add Task".
    *   **Manage Tasks:** For each task in the list, click "Done"/"Undo" to toggle its completion status, "Edit" to modify its text, or "Delete" to remove it.
    *   **Filter & Sort:** Use the "Filter" and "Sort" dropdowns to change how tasks are displayed.
    *   **Search:** Use the "Search tasks..." input to find specific tasks.
    *   **Bulk Actions:** Use the "Clear Completed", "Mark All Done", "Mark All Active", "Export JSON", and "Import JSON" buttons for group operations.
    *   Tasks are automatically saved to your browser's local storage and will be present when you reopen the page.