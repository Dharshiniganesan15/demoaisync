# Codebase Documentation

This document provides a comprehensive overview of the codebase, adhering strictly to the provided files and their contents without inferring or inventing features.

## Overview

This codebase primarily consists of a single HTML file, `sample-app.html`, which implements a client-side Task Manager application. The application leverages embedded CSS for styling and embedded JavaScript for all its functionality, including task management, data persistence via browser local storage, and user interface interactions. The `app.py` file is present but empty, indicating no server-side Python logic is currently implemented or provided.

## File Structure

- `app.py`: An empty Python file.
- `sample-app.html`: The main application file containing HTML structure, embedded CSS styling, and embedded JavaScript logic for a task manager.

## File: app.py

This file is empty.

## File: sample-app.html

This file contains the complete front-end implementation of the Task Manager application. It is a self-contained HTML document that includes:
- **HTML Structure**: Defines the layout and elements of the task manager interface.
- **CSS Styling**: Embedded within a `<style>` tag, it provides the visual presentation and responsiveness of the application.
- **JavaScript Functionality**: Embedded within a `<script>` tag, it handles all interactive features, task data management, and client-side logic.
The title of the document is "Task Manager".

## HTML Structure

The `sample-app.html` document defines the following key structural elements:

-   **`<!doctype html>`**: Declares an HTML5 document.
-   **`<html lang="en">`**: The root element, specifying the document language.
-   **`<head>`**: Contains metadata and styling:
    -   `<meta charset="UTF-8" />`: Specifies character encoding.
    -   `<meta name="viewport" content="width=device-width, initial-scale=1.0" />`: Configures viewport for responsive design.
    -   `<title>Task Manager</title>`: Sets the browser tab title.
    -   `<style>`: Embeds all CSS rules for the application's appearance.
-   **`<body>`**: Contains the visible content of the web page:
    -   **`<main class="app">`**: The primary container for the entire task manager interface.
        -   **`<header>`**: Displays the application title and a clock.
            -   `<h1>Demo AI Sync - Task Board</h1>`
            -   `<span id="clock"></span>`: Placeholder for the real-time clock.
        -   **`<section class="content">`**: Encapsulates the main interactive elements and task list.
            -   **Task Input Row**: A `div` with `class="row"` for adding new tasks.
                -   `<input id="taskInput" type="text" placeholder="Enter task..." />`
                -   `<select id="prioritySelect">`: Dropdown for task priority (High, Medium, Low).
                -   `<input id="dueDateInput" type="date" />`
                -   `<button id="addBtn">Add Task</button>`
            -   **Filter/Sort/Search Row**: Another `div` with `class="row"` for task management controls.
                -   `<select id="filterSelect">`: Dropdown for filtering tasks by status (All, Active, Done).
                -   `<select id="sortSelect">`: Dropdown for sorting tasks (Newest, Oldest, Priority, Due Date).
                -   `<input id="searchInput" type="text" placeholder="Search tasks..." />`
                -   `<button id="clearCompletedBtn" class="button-clear">Clear Completed</button>`
            -   **Summary Row**: A `div` with `class="row"` displaying task counts.
                -   `<div class="meta" id="summary">0 tasks</div>`
            -   **Bulk Actions Row**: A `div` with `class="row"` for additional actions.
                -   `<button id="markAllDoneBtn" class="button-clear">Mark All Done</button>`
                -   `<button id="markAllActiveBtn" class="button-clear">Mark All Active</button>`
                -   `<button id="exportBtn" class="button-clear">Export JSON</button>`
                -   `<button id="importBtn" class="button-clear">Import JSON</button>`
            -   **Task List**:
                -   `<ul id="taskList"></ul>`: An unordered list where individual tasks are dynamically rendered.
            -   **Empty State Message**:
                -   `<div id="emptyState" class="empty">No tasks yet. Add your first task.</div>`: Displays when no tasks are present.
            -   **Hidden File Input for Import**:
                -   `<input id="importFileInput" type="file" accept="application/json" style="display:none;" />`
    -   **`<script>`**: Embeds all JavaScript code for the application's functionality.

## CSS Styling

The embedded CSS defines the visual aesthetics of the Task Manager. Key styling features include:

-   **CSS Variables (`:root`)**: Defines a set of custom properties for colors (`--bg`, `--card`, `--text`, `--muted`, `--primary`, `--success`, `--danger`, `--border`) to ensure consistency and ease of modification.
-   **Box Model**: Universal `box-sizing: border-box;` is applied.
-   **Body Styling**: Sets a "Segoe UI" font stack, a linear gradient background from `#eef4ff` to `--bg`, centered content using `display: grid` and `place-items: center`, and basic padding.
-   **App Container (`.app`)**: Styles the main application wrapper with a white background (`--card`), border (`--border`), rounded corners (`14px`), and a subtle box shadow. It also limits its maximum width.
-   **Header Styling**: Features a dark background (`#0f172a`), white text, and a flex layout to align the title and clock.
-   **Content Area (`.content`)**: Provides padding and uses a grid layout with `gap` for internal spacing.
-   **Row Layouts (`.row`)**: Utilizes `display: grid` to arrange elements within specific sections, with custom `grid-template-columns` applied inline for different control groups.
-   **Form Elements (`input`, `select`, `button`)**: Applies a consistent font, border-radius, padding, and border styles. Focus states (`:focus`) are visually indicated with an outline.
-   **Buttons**:
    -   Default buttons (`button`) have a `var(--primary)` background and white text.
    -   `.button-clear`: Styles for secondary actions with a darker background (`#334155`).
    -   `.btn-success`: Uses `var(--success)` background.
    -   `.btn-danger`: Uses `var(--danger)` background.
-   **Task List (`ul`, `li`)**:
    -   `ul`: Removes default list styling and uses a grid layout with a gap.
    -   `li`: Individual task items are styled with a border, rounded corners, padding, and a grid layout for content and controls.
-   **Metadata (`.meta`)**: Applies muted text color and smaller font size for secondary information like due dates and creation times.
-   **Badges (`.badge`)**: Styles for priority indicators, featuring rounded corners, specific padding, font size, and bold text.
    -   `priority-high`: Reddish background/text.
    -   `priority-medium`: Yellowish background/text.
    -   `priority-low`: Greenish background/text.
-   **Overdue Indicator (`.overdue`)**: Applies red text and bold font weight to highlight overdue tasks.
-   **Task Controls (`.controls`)**: Uses a flex layout for action buttons within each task item.
-   **Done Task (`.done`)**: Applies a line-through text decoration and a muted text color.
-   **Empty State (`.empty`)**: Styles the message displayed when no tasks are present with centering, muted text, and a dashed border.

## JavaScript Functionality

The embedded JavaScript code provides all the interactive functionality for the Task Manager application:

-   **DOM Element References**: Variables are declared to store references to various HTML elements by their `id` (e.g., `taskInput`, `addBtn`, `taskList`, `clock`, `summary`, `emptyState`).
-   **Constants**:
    -   `STORAGE_KEY`: A string `demoaisync_task_manager_v2` used as the key for `localStorage` to store task data.
    -   `tasks`: An array `[]` that holds all the task objects in memory.
-   **`formatDateTime(d)`**: A utility function that takes a `Date` object (or defaults to the current date) and returns a locale-specific string representation of the date and time.
-   **`renderClock()`**: Updates the text content of the `clock` span with the current formatted date and time using `formatDateTime()`.
-   **`createTask(text, priority, dueDate)`**: Creates and returns a new task object with properties:
    -   `id`: A unique identifier generated using `crypto.randomUUID()`.
    -   `text`: The task description (trimmed).
    -   `priority`: The task's priority (defaults to "medium").
    -   `dueDate`: An optional due date string.
    -   `done`: A boolean indicating completion status (initializes to `false`).
    -   `createdAt`: The ISO string of the task creation date.
-   **`saveTasks()`**: Serializes the `tasks` array to a JSON string and saves it to the browser's `localStorage` using the `STORAGE_KEY`.
-   **`loadTasks()`**: Retrieves the task data from `localStorage`, parses it as JSON, and populates the `tasks` array. It includes error handling and data cleaning to ensure tasks are valid objects with expected properties.
-   **`addTask()`**:
    -   Retrieves the task text, priority, and due date from input fields.
    -   If text is not empty, it creates a new task using `createTask()`.
    -   Adds the new task to the beginning of the `tasks` array (`unshift`).
    -   Clears the input fields and resets priority/due date selectors.
    -   Calls `saveTasks()` and `render()`.
    -   Sets focus back to the `taskInput`.
-   **`toggleTask(id)`**: Finds a task by its `id` and inverts its `done` status. Calls `saveTasks()` and `render()`.
-   **`editTask(id)`**: Finds a task by its `id`, prompts the user to edit the task's text, updates the task if the input is valid, then calls `saveTasks()` and `render()`.
-   **`removeTask(id)`**: Finds a task by its `id`, removes it from the `tasks` array using `splice`. Calls `saveTasks()` and `render()`.
-   **`clearCompletedTasks()`**: Iterates through the `tasks` array (in reverse to avoid index issues) and removes all tasks where `done` is `true`. Calls `saveTasks()` and `render()`.
-   **`markAllDone()`**: Sets the `done` property of all tasks in the `tasks` array to `true`. Calls `saveTasks()` and `render()`.
-   **`markAllActive()`**: Sets the `done` property of all tasks in the `tasks` array to `false`. Calls `saveTasks()` and `render()`.
-   **`exportTasks()`**:
    -   Creates a JSON payload including the current `tasks` array and an `exportedAt` timestamp.
    -   Creates a `Blob` from the JSON string.
    -   Generates a temporary URL for the Blob.
    -   Creates a hidden `<a>` element, sets its `href` to the Blob URL and `download` attribute for a file name (e.g., `tasks-YYYY-MM-DDTHH-MM-SS.json`).
    -   Programmatically clicks the `<a>` element to trigger a download.
    -   Cleans up the temporary URL and `<a>` element.
-   **`importTasksFromFile(file)`**:
    -   Takes a `File` object as input.
    -   Uses `FileReader` to read the file content as text.
    -   On `onload`, it parses the JSON content, extracts task data (which might be an array directly or nested under a `tasks` property).
    -   Validates and cleans the incoming task data similarly to `loadTasks()`.
    -   Replaces the current `tasks` array with the imported ones.
    -   Calls `saveTasks()` and `render()`.
    -   Includes error handling for invalid JSON files.
-   **`getFilteredTasks()`**:
    -   Applies filtering based on the `filterSelect` value ("all", "active", "done").
    -   Applies searching based on the `searchInput` value (case-insensitive text search).
    -   Applies sorting based on the `sortSelect` value ("newest" (default), "oldest", "priority", "due").
        -   `priorityRank` object is used for priority sorting.
        -   Date objects are used for `createdAt` and `dueDate` sorting.
    -   Returns the processed array of tasks.
-   **`render()`**:
    -   Clears the current content of `taskList`.
    -   Retrieves the tasks to display using `getFilteredTasks()`.
    -   For each task, it dynamically creates an `<li>` element.
    -   Constructs the inner HTML for the task, including task text, priority badge, due date, creation date.
    -   Applies `done` class if the task is completed and `overdue` class if the task has a past due date and is not completed.
    -   Creates "Done" (or "Undo"), "Edit", and "Delete" buttons for each task.
    -   Attaches event listeners to these buttons to call `toggleTask()`, `editTask()`, and `removeTask()` with the respective task `id`.
    -   Appends the created `<li>` to the `taskList`.
    -   Updates the `summary` text to show total, done, and visible task counts.
    -   Toggles the display of `emptyState` based on whether there are tasks to show.
    -   Disables/enables the "Clear Completed", "Mark All Done", and "Mark All Active" buttons based on the current state of tasks.
-   **Event Listeners**:
    -   `addBtn` click and `taskInput` 'Enter' keydown trigger `addTask()`.
    -   `filterSelect`, `sortSelect`, `searchInput` changes/input trigger `render()` to update the displayed tasks.
    -   `clearCompletedBtn` click triggers `clearCompletedTasks()`.
    -   `markAllDoneBtn` click triggers `markAllDone()`.
    -   `markAllActiveBtn` click triggers `markAllActive()`.
    -   `exportBtn` click triggers `exportTasks()`.
    -   `importBtn` click simulates a click on the hidden `importFileInput`.
    -   `importFileInput` change event triggers `importTasksFromFile()` with the selected file.
-   **Initialization**:
    -   `loadTasks()` is called once when the script loads to retrieve previously saved tasks.
    -   `setInterval(renderClock, 1000)` sets up the clock to update every second.
    -   `renderClock()` and `render()` are called immediately to display initial state.

## Features

-   **Task Creation**: Users can add new tasks by entering text, selecting a priority (High, Medium, Low), and optionally setting a due date.
-   **Task Display**: Tasks are listed, showing their text, priority (with visual badges), due date, and creation timestamp.
-   **Task Status Toggle**: Individual tasks can be marked as "Done" or their "Done" status can be undone.
-   **Task Editing**: Users can edit the text of an existing task via a prompt.
-   **Task Deletion**: Individual tasks can be removed from the list.
-   **Task Filtering**: Tasks can be filtered by their completion status: all tasks, only active tasks, or only completed tasks.
-   **Task Sorting**: Tasks can be sorted by creation date (newest or oldest first), by priority, or by due date.
-   **Task Search**: Users can search for tasks by typing keywords into a search input, filtering the list by task text content.
-   **Bulk Task Actions**:
    -   **Clear Completed**: Removes all tasks currently marked as done.
    -   **Mark All Done**: Sets all tasks in the list to a completed state.
    -   **Mark All Active**: Sets all tasks in the list to an active (not done) state.
-   **Data Persistence**: All tasks are automatically saved to and loaded from the browser's `localStorage`, ensuring data is preserved across browser sessions.
-   **Import/Export Functionality**:
    -   **Export JSON**: Exports all current tasks to a JSON file, which can be downloaded.
    -   **Import JSON**: Allows users to import tasks from a local JSON file, replacing the current task list.
-   **Overdue Indication**: Tasks that have a due date in the past and are not marked as done are visually highlighted as "Overdue".
-   **Real-time Clock**: A clock in the header continuously displays the current date and time.
-   **Empty State Message**: A clear message is displayed when there are no tasks matching the current filters/search criteria.
-   **Task Summary**: Provides a dynamic overview of the total number of tasks, how many are completed, and how many are currently visible based on filters/search.

## How to Use/Run

To use this Task Manager application:

1.  **Save the file**: Save the provided content of `sample-app.html` into a file named `sample-app.html` (or any `.html` extension) on your local computer.
2.  **Open in Browser**: Navigate to the saved `sample-app.html` file using your file explorer and open it with any modern web browser (e.g., Chrome, Firefox, Edge, Safari).
3.  **Add a Task**:
    *   Type your task description into the "Enter task..." input field.
    *   Optionally select a priority from the "Medium" dropdown.
    *   Optionally select a due date using the date input.
    *   Click the "Add Task" button or press `Enter` in the task input field.
4.  **Manage Tasks**:
    *   **Toggle Done/Undo**: Click the "Done" (or "Undo") button next to a task to change its completion status.
    *   **Edit Task**: Click the "Edit" button next to a task to open a prompt and modify its text.
    *   **Delete Task**: Click the "Delete" button next to a task to remove it.
5.  **Filter, Sort, Search**:
    *   Use the "All / Active / Done" dropdown to filter tasks by status.
    *   Use the "Sort: Newest / Oldest / Priority / Due Date" dropdown to reorder the task list.
    *   Type in the "Search tasks..." input to find tasks by keywords in their descriptions.
6.  **Use Bulk Actions**:
    *   Click "Clear Completed" to remove all tasks currently marked as done.
    *   Click "Mark All Done" to mark all tasks as completed.
    *   Click "Mark All Active" to mark all tasks as not completed.
7.  **Import/Export Tasks**:
    *   Click "Export JSON" to download your current task list as a `.json` file.
    *   Click "Import JSON" to open a file dialog and select a `.json` file containing tasks to load into the application. (Note: Importing will replace your current tasks).