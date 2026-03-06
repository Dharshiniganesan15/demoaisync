# Project Documentation: Demo AI Sync - Sample App

This documentation describes the provided codebase, focusing strictly on the contents of the given files.

## Overview

The primary component of this project is a client-side web application (`sample-app.html`) that implements a basic task board. It allows users to add, mark as complete, delete, and filter tasks. All data is managed in-memory within the browser session and is not persistent across page refreshes or browser closures.

The `app.py` file is present but currently empty, indicating no Python backend functionality is implemented or utilized by the web application.

## File Structure

*   `app.py`: A Python file.
*   `sample-app.html`: An HTML file containing the entire web application (HTML structure, CSS styles, and JavaScript logic).

## `app.py` Analysis

*   **Language:** Python
*   **Content:** The file `app.py` is entirely empty.
*   **Functionality:** As the file contains no code, it provides no functionality to the project. It is not referenced or used by `sample-app.html`.

## `sample-app.html` Analysis

This file contains a self-contained web application written in HTML, CSS, and JavaScript.

### HTML Structure

The HTML defines the layout and user interface elements of the task board:

*   **Document Structure:** A standard HTML5 document with a `head` and `body`.
*   **Metadata:** Sets character encoding (`UTF-8`), viewport for responsiveness, and the page title "Demo AI Sync - Sample App".
*   **Main Application Container (`.app`):**
    *   **Header:** Displays "Demo AI Sync - Task Board" and a `span` element (`#clock`) for showing the current date and time.
    *   **Content Section (`.content`):**
        *   **Task Input:** An `input` field (`#taskInput`) for entering new tasks and an "Add Task" `button` (`#addBtn`).
        *   **Filter & Summary:**
            *   A `select` dropdown (`#filterSelect`) with options to filter tasks: "All", "Active", "Done".
            *   A `div` (`#summary`) to display the current task count (e.g., "0 tasks (0 done)").
        *   **Task List:** An unordered list (`#taskList`) where individual task items will be displayed.
        *   **Empty State:** A `div` (`#emptyState`) which is shown when there are no tasks in the list, displaying "No tasks yet. Add your first task."

### CSS Styling

The page includes embedded CSS within a `<style>` block in the `head` section, providing a clean and modern user interface:

*   **CSS Variables:** Defines custom properties (`--bg`, `--card`, `--text`, etc.) for consistent theming and easy modification of colors.
*   **Global Styles:** Resets default browser styles and sets `box-sizing` to `border-box`.
*   **Body Styling:** Sets a gradient background, `Segoe UI` font family, and centers the `.app` container vertically and horizontally.
*   **App Container (`.app`):** Styles the main application box with a white background, rounded corners, border, and shadow.
*   **Header Styling:** Applies a dark background, white text, and uses flexbox for alignment of the title and clock.
*   **Content Styling:** Uses CSS Grid for layout within the main content area, with defined gaps between elements.
*   **Form Elements (`input`, `select`, `button`):** Provides consistent styling for input fields, select boxes, and buttons, including focus states.
*   **Task List Styling (`ul`, `li`):** Styles the unordered list and individual list items with borders, padding, and grid layout for task text and controls.
*   **Specific Utility Classes:**
    *   `.meta`: For secondary text (e.g., creation timestamp).
    *   `.controls`: Flexbox container for action buttons within a task item.
    *   `.done`: Applies a line-through text decoration and muted color for completed tasks.
    *   `.btn-success`, `.btn-danger`: Styles for success (green) and danger (red) themed buttons.
    *   `.empty`: Styles the placeholder message when the task list is empty.

### JavaScript Functionality

All interactive logic for the task board is implemented in an embedded `<script>` block at the end of the `body`.

*   **DOM Element References:** Obtains references to key HTML elements using their IDs (e.g., `taskInput`, `addBtn`, `taskList`).
*   **`tasks` Array:** An empty JavaScript array `const tasks = [];` is used to store all task objects in memory. Each task object has `id`, `text`, `done` (boolean), and `createdAt` properties.
*   **Date & Time Utilities:**
    *   `formatDateTime(d = new Date())`: Formats a `Date` object into a locale-specific string.
    *   `renderClock()`: Updates the text content of the `#clock` element with the current date and time using `formatDateTime()`. This function is called every second via `setInterval`.
*   **Task Management Functions:**
    *   `createTask(text)`: Generates a new task object with a unique ID (using `crypto.randomUUID()`), the provided `text`, `done: false`, and `createdAt` timestamp.
    *   `addTask()`:
        *   Retrieves the trimmed value from `taskInput`.
        *   If the input is not empty, it calls `createTask()` to create a new task.
        *   Adds the new task to the *beginning* of the `tasks` array using `unshift()`.
        *   Clears the `taskInput` field and calls `render()` to update the UI.
        *   Sets focus back to `taskInput`.
    *   `toggleTask(id)`: Finds a task by its `id` and flips its `done` status (`true` to `false`, or `false` to `true`). Calls `render()`.
    *   `removeTask(id)`: Finds a task by its `id` and removes it from the `tasks` array using `splice()`. Calls `render()`.
*   **Task Filtering:**
    *   `getFilteredTasks()`: Returns a subset of the `tasks` array based on the current value of `filterSelect` ("all", "active", or "done").
*   **UI Rendering (`render()`):**
    *   This is the core function that updates the `taskList` UI based on the current state of the `tasks` array and the filter selection.
    *   Clears existing `taskList` content.
    *   Iterates through the `getFilteredTasks()` result.
    *   For each task, it dynamically creates an `<li>` element with:
        *   The task text, applying the `.done` class if `task.done` is `true`.
        *   The creation timestamp formatted using `toLocaleString()`.
        *   Two `button` elements: one to "Done"/"Undo" (toggling `task.done`) and one to "Delete".
    *   Attaches event listeners to these dynamically created buttons to call `toggleTask()` and `removeTask()` with the correct task ID.
    *   Appends the new `<li>` to `taskList`.
    *   Updates the `summary` element with the total number of tasks and the count of done tasks.
    *   Controls the visibility of the `emptyState` div based on whether there are tasks to display.
*   **Event Listeners:**
    *   `addBtn` `click` event: Triggers `addTask()`.
    *   `taskInput` `keydown` event: Triggers `addTask()` if the "Enter" key is pressed.
    *   `filterSelect` `change` event: Triggers `render()` to re-filter and display tasks.
*   **Initialization:**
    *   `setInterval(renderClock, 1000)`: Starts the clock update loop immediately.
    *   `renderClock()`: Calls `renderClock()` once to display the initial time without delay.
    *   `render()`: Calls `render()` once to display the initial (empty) task list.

## Features (from `sample-app.html`)

*   **Task Management:**
    *   Add new tasks.
    *   Mark tasks as done or undo their completion.
    *   Delete tasks.
*   **Task Filtering:** Filter tasks to view "All", "Active" (not done), or "Done" tasks.
*   **Task Summary:** Displays the total number of tasks and how many are completed.
*   **Real-time Clock:** Shows the current date and time in the header, updated every second.
*   **Empty State:** A message is displayed when there are no tasks to show.
*   **Responsive Design:** Uses `viewport` meta tag and some relative sizing in CSS, though not extensively demonstrated for various screen sizes.
*   **In-Memory Storage:** All tasks are stored in the browser's JavaScript memory and are reset upon page refresh or closing the browser tab.

## How to Use/Run

1.  **Open `sample-app.html`:** Simply open the `sample-app.html` file in any modern web browser (e.g., Chrome, Firefox, Edge, Safari).
2.  **Add Tasks:** Type a task description into the "Enter task..." input field and either click the "Add Task" button or press `Enter`.
3.  **Manage Tasks:**
    *   Click the "Done" button next to a task to mark it as complete (it will be struck through). The button will change to "Undo".
    *   Click the "Undo" button to revert a task's completion status.
    *   Click the "Delete" button to remove a task permanently.
4.  **Filter Tasks:** Use the dropdown menu to switch between "All", "Active", and "Done" tasks.
5.  **Observe Clock:** The clock in the header will update every second.

Since `app.py` is empty, there is no server-side component to run.
