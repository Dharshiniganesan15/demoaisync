This document provides a comprehensive overview of the codebase, adhering strictly to the provided files and their contents without inferring or inventing features.

---

# Codebase Documentation

This codebase comprises a Python file (`app.py`) and an HTML file (`sample-app.html`) which includes embedded CSS and JavaScript.

## File: `app.py`

This file is currently empty. It does not contain any Python code or functionality.

## File: `sample-app.html`

The `sample-app.html` file defines a single-page web application titled "Demo AI Sync - Sample App". It is structured as a task board interface, incorporating HTML for structure, CSS for styling, and JavaScript for interactive functionality.

### HTML Structure

The HTML provides the basic layout and elements for the task management application:

*   **Document Metadata:** Sets character encoding to UTF-8, configures the viewport for responsiveness, and sets the page title to "Demo AI Sync - Sample App".
*   **Main Application Container:** A `main` element with the class `app` wraps the entire application content.
*   **Header:**
    *   Displays the application title "Demo AI Sync - Task Board" (`h1`).
    *   Includes a `span` with `id="clock"` to display the current date and time, dynamically updated by JavaScript.
*   **Content Section:** A `section` with the class `content` contains the interactive elements of the task board.
    *   **Add Task Row:**
        *   An `input` field (`id="taskInput"`) for entering new task descriptions.
        *   A `button` (`id="addBtn"`) to add the entered task.
    *   **Filtering and Searching Row:**
        *   A `select` dropdown (`id="filterSelect"`) with options to filter tasks by status: "All", "Active", and "Done".
        *   An `input` field (`id="searchInput"`) for searching tasks by text.
        *   A `button` (`id="clearCompletedBtn"`) with class `button-clear` to remove all completed tasks. This button's disabled state and opacity are controlled by JavaScript.
    *   **Summary Row:**
        *   A `div` with `id="summary"` that displays a summary of tasks, including total tasks, completed tasks, and the number of currently displayed tasks.
    *   **Task List:** An unordered list (`ul` with `id="taskList"`) where individual task items (`li`) are dynamically rendered by JavaScript.
    *   **Empty State:** A `div` with `id="emptyState"` and class `empty` that is displayed when no tasks match the current filters or search query.

### CSS Styling

The embedded CSS defines the visual appearance of the application, using CSS variables for consistent theming:

*   **Root Variables:** Defines custom properties for colors (`--bg`, `--card`, `--text`, `--muted`, `--primary`, `--success`, `--danger`, `--border`).
*   **Global Styles:** Sets `box-sizing` to `border-box` for all elements.
*   **Body Styling:** Configures font family, background gradient, text color, and centers the application vertically and horizontally.
*   **Application Container (`.app`):** Styles the main application box with background, borders, rounded corners, and a subtle shadow.
*   **Header Styling:** Sets a dark background, white text, padding, and uses flexbox for alignment of the title and clock.
*   **Content Section (`.content`):** Applies padding and uses a grid layout for its direct children.
*   **Row Layout (`.row`):** Uses CSS Grid for horizontal arrangement of elements within rows. Specific grid column templates are applied to different rows.
*   **Form Controls (Input, Select, Button):** Provides consistent styling for input fields, select boxes, and buttons, including border-radius, padding, and focus states.
*   **Buttons:** Defines default button styles for background, text color, and font weight. Specific styles are provided for `.button-clear`, `.btn-success`, and `.btn-danger`.
*   **Task List (`ul`):** Removes default list styling and uses a grid layout for spacing.
*   **Task Item (`li`):** Styles individual task items with borders, rounded corners, padding, and a grid layout to arrange task text/meta and controls.
*   **Meta Information (`.meta`):** Styles for secondary text, such as task creation time.
*   **Controls Container (`.controls`):** Uses flexbox to arrange buttons within a task item.
*   **Completed Task (`.done`):** Applies `text-decoration: line-through` and changes color for completed tasks.
*   **Empty State (`.empty`):** Styles the message displayed when no tasks are present.

### JavaScript Functionality

The embedded JavaScript provides the dynamic and interactive behavior of the task board application:

*   **DOM Element References:** Stores references to key HTML elements for manipulation.
*   **`tasks` Array:** An array named `tasks` is initialized to store all task objects. Each task object includes `id`, `text`, `done` status, and `createdAt` timestamp.
*   **`formatDateTime(d)`:** A utility function that formats a given `Date` object (or the current date if none is provided) into a locale-specific string.
*   **`renderClock()`:** Updates the `clock` span element with the current date and time using `formatDateTime()`. This function is called every second by `setInterval`.
*   **`createTask(text)`:**
    *   Generates a new task object.
    *   Assigns a unique ID using `crypto.randomUUID()`.
    *   Stores the trimmed `text` input.
    *   Sets `done` to `false` initially.
    *   Records the `createdAt` timestamp in ISO format.
*   **`addTask()`:**
    *   Retrieves and trims the text from `taskInput`.
    *   If the text is not empty, it creates a new task using `createTask()` and adds it to the beginning of the `tasks` array (`unshift`).
    *   Clears the `taskInput` field.
    *   Calls `render()` to update the UI.
    *   Sets focus back to `taskInput`.
*   **`toggleTask(id)`:**
    *   Finds a task in the `tasks` array by its `id`.
    *   If found, it toggles the `done` status of that task.
    *   Calls `render()` to update the UI.
*   **`removeTask(id)`:**
    *   Finds the index of a task by its `id`.
    *   If found, it removes the task from the `tasks` array using `splice`.
    *   Calls `render()` to update the UI.
*   **`clearCompletedTasks()`:**
    *   Iterates through the `tasks` array in reverse order.
    *   Removes any task where `done` is `true` from the array.
    *   Calls `render()` to update the UI.
*   **`getFilteredTasks()`:**
    *   Filters the `tasks` array based on the selected value of `filterSelect` ("all", "active", "done").
    *   Further filters the results based on the text entered in `searchInput`, performing a case-insensitive substring match.
    *   Returns the array of filtered tasks.
*   **`render()`:** This is the primary function responsible for updating the entire task list and related UI elements:
    *   Retrieves the list of tasks to display using `getFilteredTasks()`.
    *   Clears the current content of `taskList`.
    *   For each filtered task:
        *   Creates a new `li` element.
        *   Populates its `innerHTML` with the task text (applying the `done` class if completed), creation date (formatted), and two buttons: "Done"/"Undo" and "Delete".
        *   Attaches `click` event listeners to these buttons to call `toggleTask()` and `removeTask()` respectively, passing the task's `id`.
        *   Appends the `li` element to `taskList`.
    *   Updates the `summary` div with the total number of tasks, the count of done tasks, and the number of tasks currently being shown.
    *   Toggles the visibility of the `emptyState` message based on whether there are any tasks to display.
    *   Enables/disables the `clearCompletedBtn` and adjusts its opacity based on the count of completed tasks.
*   **Event Listeners:**
    *   `addBtn` listens for `click` events to call `addTask()`.
    *   `taskInput` listens for `keydown` events, calling `addTask()` if the "Enter" key is pressed.
    *   `filterSelect` listens for `change` events to call `render()`.
    *   `searchInput` listens for `input` events to call `render()`.
    *   `clearCompletedBtn` listens for `click` events to call `clearCompletedTasks()`.
*   **Initialization:**
    *   `setInterval(renderClock, 1000)`: Sets up a recurring timer to update the clock every 1000 milliseconds (1 second).
    *   `renderClock()`: An immediate call to display the clock upon page load.
    *   `render()`: An immediate call to render the initial (empty) task list upon page load.