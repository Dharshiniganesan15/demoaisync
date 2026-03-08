# Codebase Documentation

This document provides a comprehensive overview of the codebase, adhering strictly to the provided files and their contents without inferring or inventing features.

## Overview

The codebase consists of two distinct parts: a simple Python script defining a basic arithmetic function and a self-contained HTML file that implements a client-side task manager web application. The task manager features extensive HTML structure, embedded CSS for styling, and JavaScript for interactive functionality, including local storage persistence, task filtering, sorting, and import/export capabilities.

## File Structure

- `app.py`
- `sample-app.html`

## File: app.py

This Python file defines a single function.

```python
def add(a,b):
    return a + b
```

**Function:** `add(a, b)`
*   **Description:** Takes two arguments, `a` and `b`, and returns their sum.
*   **Parameters:**
    *   `a`: The first operand.
    *   `b`: The second operand.
*   **Returns:** The result of `a + b`.

## File: sample-app.html

This HTML file defines a complete web page for a task manager application, incorporating embedded CSS for styling and embedded JavaScript for all dynamic functionality.

## HTML Structure

The `sample-app.html` file establishes a single-page application structure.

*   **`<!doctype html>`**: Declares the document as an HTML5 file.
*   **`<html lang="en">`**: The root element, specifying the document language as English.
*   **`<head>`**: Contains metadata and styling information.
    *   **`<meta charset="UTF-8" />`**: Specifies the character encoding for the document.
    *   **`<meta name="viewport" ... />`**: Configures the viewport for responsive behavior across devices.
    *   **`<title>Task Manager</title>`**: Sets the title that appears in the browser tab or window.
    *   **`<style>`**: Contains all the CSS rules embedded directly into the document.
*   **`<body>`**: Contains the visible content of the web page.
    *   **`<main class="app">`**: The main container for the task manager application, styled with the `app` class.
        *   **`<header>`**: The application's header section.
            *   **`<h1>Demo AI Sync - Task Board</h1>`**: The main title of the application.
            *   **`<span id="clock"></span>`**: An empty `span` element intended to display a real-time clock, identified by the `clock` ID.
        *   **`<section class="content">`**: The main content area of the application.
            *   **`div class="row"` (Task Input)**: Contains inputs for adding new tasks.
                *   **`<input id="taskInput" type="text" placeholder="Enter task..." />`**: Text input for the task description.
                *   **`<select id="prioritySelect">`**: Dropdown for selecting task priority (High, Medium, Low).
                *   **`<input id="dueDateInput" type="date" />`**: Date input for the task's due date.
                *   **`<button id="addBtn">Add Task</button>`**: Button to submit a new task.
            *   **`div class="row"` (Filter/Sort/Search)**: Contains controls for managing the task list display.
                *   **`<select id="filterSelect">`**: Dropdown for filtering tasks by status (All, Active, Done).
                *   **`<select id="sortSelect">`**: Dropdown for sorting tasks (Newest, Oldest, Priority, Due Date).
                *   **`<input id="searchInput" type="text" placeholder="Search tasks..." />`**: Text input for searching tasks.
                *   **`<button id="clearCompletedBtn" class="button-clear">Clear Completed</button>`**: Button to remove all completed tasks.
            *   **`div class="row"` (Summary)**: Displays a summary of tasks.
                *   **`<div class="meta" id="summary">0 tasks</div>`**: Shows the count of tasks, identified by the `summary` ID.
            *   **`div class="row"` (Bulk Actions/Import/Export)**: Contains buttons for bulk actions and data management.
                *   **`<button id="markAllDoneBtn" class="button-clear">Mark All Done</button>`**: Button to mark all tasks as completed.
                *   **`<button id="markAllActiveBtn" class="button-clear">Mark All Active</button>`**: Button to mark all tasks as active.
                *   **`<button id="exportBtn" class="button-clear">Export JSON</button>`**: Button to export tasks to a JSON file.
                *   **`<button id="importBtn" class="button-clear">Import JSON</button>`**: Button to initiate task import.
            *   **`<ul id="taskList"></ul>`**: An empty unordered list where tasks will be dynamically inserted, identified by the `taskList` ID.
            *   **`<div id="emptyState" class="empty">No tasks yet. Add your first task.</div>`**: A message displayed when there are no tasks, identified by the `emptyState` ID.
            *   **`<input id="importFileInput" type="file" accept="application/json" style="display:none;" />`**: A hidden file input used for selecting JSON files for import, identified by the `importFileInput` ID.
*   **`<script>`**: Contains all the JavaScript code embedded directly into the document, responsible for dynamic behavior.

## CSS Styling

The embedded `<style>` block in `sample-app.html` defines the visual appearance of the Task Manager.

*   **CSS Variables (`:root`)**:
    *   Defines a set of custom properties for colors and borders: `--bg`, `--card`, `--text`, `--muted`, `--primary`, `--success`, `--danger`, `--border`. This allows for consistent theming and easier updates.
*   **General/Global Styles**:
    *   `*`: Sets `box-sizing` to `border-box` for all elements.
    *   `body`: Configures basic typography (`font-family`), sets a linear gradient background, defines text color using `--text`, ensures minimum height, centers content using `display: grid` and `place-items: center`, and adds padding.
*   **`.app`**: Styles the main application container:
    *   Sets responsive width, background (`--card`), border, border-radius, and a subtle `box-shadow`. `overflow: hidden` clips content that exceeds the element's boundaries.
*   **`header`**: Styles the top header bar:
    *   Dark background, white text, padding, and a flex layout to align items and space them out.
    *   `header h1` and `header span` specifically style the title and clock/info text.
*   **`.content`**: Styles the main content area with padding and a grid layout for its children.
*   **`.row`**: Provides a general grid layout for rows of elements, often with two columns and a gap. Specific rows override `grid-template-columns` for custom layouts.
*   **Form Elements (`input, select, button`)**:
    *   Applies consistent font inheritance, border-radius, border, and padding.
    *   `input:focus, select:focus`: Defines blue outline and border color on focus.
    *   `button`: Sets cursor to pointer, removes default border, applies primary background color (`--primary`), white text, and `font-weight`.
    *   `.button-clear`: A variant style for buttons with a darker background.
*   **List Styles (`ul`, `li`)**:
    *   `ul`: Removes default list styling, margins, and padding, and uses a grid layout for task items.
    *   `li`: Styles individual task items with a border, border-radius, padding, grid layout, and white background.
*   **Utility Classes**:
    *   `.meta`: Styles secondary information text with a muted color and smaller font size.
    *   `.badge`: Styles small, rounded text labels (e.g., for priority).
    *   `.priority-high`, `.priority-medium`, `.priority-low`: Specific background and text colors for different priority badges.
    *   `.overdue`: Styles text to highlight overdue status with red color and bold font.
    *   `.controls`: Styles the container for action buttons within a task item using flexbox.
    *   `.done`: Applies `text-decoration: line-through` and a muted color to completed task text.
    *   `.btn-success`, `.btn-danger`: Applies success (green) or danger (red) background colors to buttons.
    *   `.empty`: Styles the "No tasks yet" message with padding, centered text, muted color, and a dashed border.

## JavaScript Functionality

The embedded JavaScript provides all the dynamic behavior for the Task Manager application.

*   **DOM Element References**: Variables are declared to store references to key HTML elements, allowing for easier manipulation (e.g., `taskInput`, `addBtn`, `taskList`).
*   **Constants**:
    *   `STORAGE_KEY`: A string constant used as the key for `localStorage` to save and load tasks.
    *   `tasks`: An array initialized as empty, which will hold all task objects.
*   **`formatDateTime(d)`**:
    *   **Description**: Formats a `Date` object into a localized date and time string.
    *   **Parameters**: `d` (optional `Date` object, defaults to `new Date()`).
*   **`renderClock()`**:
    *   **Description**: Updates the text content of the `clock` span with the current formatted date and time.
*   **`createTask(text, priority, dueDate)`**:
    *   **Description**: Creates and returns a new task object with a unique ID, text, priority, due date, completion status (`done: false`), and `createdAt` timestamp.
    *   **Parameters**: `text` (string), `priority` (string), `dueDate` (string).
*   **`saveTasks()`**:
    *   **Description**: Serializes the `tasks` array to a JSON string and saves it to `localStorage` using `STORAGE_KEY`.
*   **`loadTasks()`**:
    *   **Description**: Retrieves tasks from `localStorage`, parses the JSON string, and populates the `tasks` array. It includes error handling for invalid JSON and filters/cleans incoming task objects to ensure a consistent structure. New unique IDs are assigned if existing ones are missing.
*   **`addTask()`**:
    *   **Description**: Reads values from the task input fields, validates the task text, creates a new task, adds it to the beginning of the `tasks` array, clears input fields, saves tasks, and re-renders the task list.
*   **`toggleTask(id)`**:
    *   **Description**: Finds a task by its ID and toggles its `done` status. Saves tasks and re-renders.
*   **`editTask(id)`**:
    *   **Description**: Finds a task by its ID, prompts the user to edit the task's text, updates the task if valid input is provided, saves tasks, and re-renders.
*   **`removeTask(id)`**:
    *   **Description**: Finds a task by its ID and removes it from the `tasks` array. Saves tasks and re-renders.
*   **`clearCompletedTasks()`**:
    *   **Description**: Removes all tasks from the `tasks` array that have `done: true`. Saves tasks and re-renders.
*   **`markAllDone()`**:
    *   **Description**: Sets `done: true` for all tasks in the `tasks` array. Saves tasks and re-renders.
*   **`markAllActive()`**:
    *   **Description**: Sets `done: false` for all tasks in the `tasks` array. Saves tasks and re-renders.
*   **`exportTasks()`**:
    *   **Description**: Creates a JSON `payload` containing the current tasks and an `exportedAt` timestamp. It then creates a `Blob` and a temporary anchor (`<a>`) element to trigger a file download (`tasks-YYYY-MM-DDTHH-MM-SS.json`) of the JSON data.
*   **`importTasksFromFile(file)`**:
    *   **Description**: Takes a `File` object (expected to be JSON). Uses `FileReader` to read the file content, parses the JSON, validates and cleans the incoming task data, replaces the current `tasks` array, saves tasks, and re-renders. Displays an alert for invalid JSON.
*   **`getFilteredTasks()`**:
    *   **Description**: Applies filtering based on the selected status (`filterSelect`) and search query (`searchInput`). Then, it applies sorting based on the `sortSelect` value (newest, oldest, priority, or due date). Returns the resulting array of tasks. A `priorityRank` object is used for priority sorting.
*   **`render()`**:
    *   **Description**: This is the primary function for updating the UI.
        *   Clears the existing content of `taskList`.
        *   Retrieves the filtered and sorted tasks using `getFilteredTasks()`.
        *   Iterates through each task to dynamically create `<li>` elements:
            *   Each `<li>` displays the task text (with `done` strikethrough if applicable), priority badge, formatted due date (with "Overdue" status if applicable), and creation date.
            *   Includes "Done/Undo", "Edit", and "Delete" buttons.
            *   Attaches event listeners to these buttons to call `toggleTask`, `editTask`, and `removeTask` with the task's ID.
        *   Appends the created `<li>` elements to `taskList`.
        *   Updates the `summary` text with task counts (total, done, showing).
        *   Toggles the visibility of the `emptyState` message.
        *   Disables/enables and adjusts opacity/cursor for `clearCompletedBtn`, `markAllDoneBtn`, and `markAllActiveBtn` based on the current state of tasks.
*   **Event Listeners**:
    *   `addBtn` click: Calls `addTask()`.
    *   `taskInput` keydown (Enter key): Calls `addTask()`.
    *   `filterSelect` change: Calls `render()`.
    *   `sortSelect` change: Calls `render()`.
    *   `searchInput` input: Calls `render()`.
    *   `clearCompletedBtn` click: Calls `clearCompletedTasks()`.
    *   `markAllDoneBtn` click: Calls `markAllDone()`.
    *   `markAllActiveBtn` click: Calls `markAllActive()`.
    *   `exportBtn` click: Calls `exportTasks()`.
    *   `importBtn` click: Programmatically clicks the hidden `importFileInput`.
    *   `importFileInput` change: Calls `importTasksFromFile()` with the selected file and resets the file input.
*   **Initialization Logic**:
    *   `loadTasks()`: Loads any previously saved tasks when the page loads.
    *   `setInterval(renderClock, 1000)`: Sets up an interval to update the clock every second.
    *   `renderClock()`: Calls `renderClock` immediately to display the clock on load.
    *   `render()`: Calls `render` immediately to display the initial task list on load.

## Features

- **Basic Arithmetic Function (Python)**: Provides a Python function to add two numbers.
- **Real-time Clock Display**: Shows the current date and time in the application header.
- **Task Creation**: Users can add new tasks with a description, select a priority (High, Medium, Low), and optionally set a due date.
- **Task Persistence**: Tasks are saved to and loaded from the browser's `localStorage`, maintaining state across browser sessions.
- **Task Management**:
    - **Toggle Completion Status**: Mark tasks as "Done" or "Undo" their completion.
    - **Edit Task**: Modify the text description of an existing task via a prompt.
    - **Delete Task**: Remove individual tasks from the list.
- **Bulk Task Actions**:
    - **Clear Completed**: Remove all tasks marked as "Done".
    - **Mark All Done**: Set all existing tasks to a "Done" state.
    - **Mark All Active**: Set all existing tasks to an "Active" (not done) state.
- **Task Filtering**: Filter tasks by status: "All", "Active" (not done), or "Done".
- **Task Sorting**: Sort tasks by:
    - "Newest" (creation date, descending)
    - "Oldest" (creation date, ascending)
    - "Priority" (High > Medium > Low)
    - "Due Date" (ascending)
- **Task Search**: Search for tasks by keywords in their descriptions.
- **Task Summary**: Displays a summary showing the total number of tasks, how many are done, and how many are currently visible based on filters/search.
- **Overdue Task Indication**: Tasks with a due date in the past that are not marked as done are visually highlighted as "Overdue".
- **Empty State Display**: Shows a "No tasks yet" message when the task list is empty.
- **Data Export**: Export all current tasks to a JSON file, including an export timestamp.
- **Data Import**: Import tasks from a user-selected JSON file, which can either be an array of tasks or an object containing a `tasks` array.

## How to Use/Run

### To Use the Python `add` function (`app.py`):

1.  **Save the file:** Save the provided Python code as `app.py`.
2.  **Run in an interpreter:** Open a Python interpreter (e.g., by typing `python` or `python3` in your terminal).
3.  **Import and call the function:**
    ```python
    from app import add
    result = add(10, 5)
    print(result) # This will output 15
    ```

### To Use the Task Manager Web Application (`sample-app.html`):

1.  **Save the file:** Save the provided HTML code as `sample-app.html`.
2.  **Open in a Web Browser:** Navigate to the saved `sample-app.html` file in your operating system's file explorer and open it with any modern web browser (e.g., Chrome, Firefox, Edge, Safari).
3.  **Interact with the application:**
    *   **Add Tasks:** Type a task description into the "Enter task..." input field, select a priority and an optional due date, then click "Add Task" or press Enter.
    *   **Manage Tasks:** For each task, you can click "Done" (or "Undo"), "Edit", or "Delete".
    *   **Filter/Sort/Search:** Use the dropdowns and search input at the top to filter, sort, and search your tasks.
    *   **Bulk Actions:** Use the "Mark All Done", "Mark All Active", and "Clear Completed" buttons for mass operations.
    *   **Export/Import:** Use "Export JSON" to download your tasks as a file, and "Import JSON" to load tasks from a previously saved file.
    *   The application will automatically save your tasks in your browser's local storage.