# Project Documentation

This document provides a comprehensive overview of the codebase, strictly adhering to the provided files and their contents.

## Overview

The project currently consists of a single HTML file (`sample-app.html`) that implements a client-side task management application, and an empty Python file (`app.py`). The task application, titled "Demo AI Sync - Task Board," runs entirely in the browser and provides functionalities for adding, managing, and filtering tasks.

## Files Documented

### `app.py`

This file is present in the project but is **empty**. There is no Python code or functionality to document.

### `sample-app.html`

This is a standalone HTML document that contains a complete client-side task board application. It leverages HTML for structure, CSS for styling, and JavaScript for all interactive logic.

#### Description

`sample-app.html` creates an interactive "Task Board" where users can manage their tasks. It features a responsive design and includes various controls for task input, filtering, sorting, and searching. All task data is stored in memory within the browser and is not persisted.

#### Features

The application provides the following functionalities:

*   **Task Creation:**
    *   Input field for task description.
    *   Dropdown for selecting task priority (High, Medium, Low).
    *   Date picker for setting a due date.
    *   "Add Task" button to create a new task. Newly added tasks appear at the top of the list.
*   **Task Management:**
    *   **Toggle Completion:** Mark tasks as "Done" or "Undo" their completion status. Completed tasks are visually struck through.
    *   **Edit Task:** Prompt to edit the text description of an existing task.
    *   **Delete Task:** Remove individual tasks from the list.
*   **Task Filtering:**
    *   Filter tasks by status: "All", "Active" (not done), or "Done".
*   **Task Sorting:**
    *   Sort tasks by: "Newest" (default, by creation date descending), "Oldest" (by creation date ascending), "Priority" (High > Medium > Low), or "Due Date" (ascending, tasks without a due date appear last).
*   **Task Search:**
    *   Live search functionality to find tasks by text content.
*   **Task Status Indicators:**
    *   Displays task priority using colored badges (HIGH, MEDIUM, LOW).
    *   Indicates if a task is "Overdue" if it has a due date in the past and is not marked as done.
    *   Shows the creation date and due date for each task.
*   **Summary and Empty State:**
    *   Displays a summary of total tasks, done tasks, and currently visible tasks.
    *   Shows a "No tasks yet" message when the task list is empty or all tasks are filtered out.
*   **Clear Completed Tasks:**
    *   A button to remove all tasks that are marked as "Done". This button is disabled when no tasks are completed.
*   **Real-time Clock:**
    *   A clock in the header displays the current date and time, updating every second.

#### Technologies Used

*   **HTML5:** Provides the structure and content of the web page.
*   **CSS3:** Embedded within the `<style>` tags, it provides all the styling for the application, including a custom color palette defined using CSS variables and responsive layout principles.
*   **JavaScript (ES6+):** Embedded within the `<script>` tags, it handles all the application logic, including DOM manipulation, event handling, data management (in-memory array), and UI updates.

#### File Structure

The `sample-app.html` file is a single, self-contained document with the following sections:

1.  **`<!doctype html>` and `<html>` root:** Standard HTML5 document declaration.
2.  **`<head>`:**
    *   `meta` tags for character set and viewport configuration.
    *   `<title>`: Sets the browser tab title to "Demo AI Sync - Sample App".
    *   `<style>` block: Contains all the CSS rules for the application's visual presentation.
3.  **`<body>`:**
    *   `<main class="app">`: The main container for the entire task board interface.
        *   `<header>`: Contains the application title and the real-time clock display (`<span id="clock">`).
        *   `<section class="content">`: The main interactive area.
            *   `div.row` for task input controls: `taskInput` (text), `prioritySelect` (dropdown), `dueDateInput` (date), `addBtn` (button).
            *   `div.row` for filtering/sorting/searching controls: `filterSelect` (dropdown), `sortSelect` (dropdown), `searchInput` (text), `clearCompletedBtn` (button).
            *   `div.row` for `summary` (`div.meta`).
            *   `<ul id="taskList">`: The unordered list where individual tasks are dynamically rendered by JavaScript.
            *   `<div id="emptyState" class="empty">`: Message displayed when no tasks are visible.
    *   `<script>` block: Contains all the JavaScript code that powers the application's interactivity.

#### Styling (CSS)

The embedded CSS defines a clear and functional user interface. Key aspects include:

*   **CSS Custom Properties (Variables):** A `:root` block defines various colors (`--bg`, `--card`, `--text`, etc.) for easy theme management.
*   **Layout:** Uses `display: grid` and `flex` for arranging elements, ensuring a structured and responsive layout. `min(980px, 100%)` ensures the app scales gracefully on different screen sizes.
*   **Components:** Specific styles are applied to:
    *   The overall app container, header, and content sections.
    *   Input fields, select boxes, and buttons, including focus states.
    *   Task list items (`<li>`), which are designed to display task text, priority, due date, creation date, and control buttons.
    *   Priority badges (`.priority-high`, `.priority-medium`, `.priority-low`) with distinct background and text colors.
    *   Visual indicators for overdue tasks (`.overdue`) and completed tasks (`.done`).
    *   Styling for control buttons (success, danger, clear actions).
    *   A dashed border style for the empty state message.

#### JavaScript Functionality

The JavaScript code manages the entire application logic:

*   **DOM Element References:** All interactive HTML elements are referenced by their `id` using `document.getElementById()`.
*   **`tasks` Array:** An in-memory array (`const tasks = []`) stores task objects. Each task object has an `id`, `text`, `priority`, `dueDate`, `done` status, and `createdAt` timestamp.
*   **Utility Functions:**
    *   `formatDateTime()`: Formats a `Date` object into a localized string.
    *   `renderClock()`: Updates the header clock display.
*   **Task CRUD (Create, Read, Update, Delete) Operations:**
    *   `createTask()`: Generates a new task object with a `crypto.randomUUID()` for a unique ID.
    *   `addTask()`: Gathers input, creates a new task, adds it to the `tasks` array, clears input fields, and triggers a UI `render`.
    *   `toggleTask(id)`: Changes the `done` status of a task by its ID and triggers a `render`.
    *   `editTask(id)`: Prompts the user to update a task's text and triggers a `render`.
    *   `removeTask(id)`: Deletes a task by its ID from the array and triggers a `render`.
    *   `clearCompletedTasks()`: Iterates and removes all tasks marked as `done`.
*   **Filtering, Sorting, and Searching:**
    *   `getFilteredTasks()`: This core function applies the current filter status ("all", "active", "done"), search query, and sorting order ("newest", "oldest", "priority", "due") to the `tasks` array. It returns a new array of tasks to be displayed.
*   **`render()` Function:**
    *   This is the central function for updating the UI. It clears the `taskList`, calls `getFilteredTasks()` to determine what to display, and then dynamically creates `<li>` elements for each task.
    *   It calculates and applies `overdue` and `done` styling, and sets up event listeners for the "Done"/"Undo", "Edit", and "Delete" buttons on each task item.
    *   It updates the `summary` text, toggles the `emptyState` visibility, and manages the disabled state and styling of the `clearCompletedBtn`.
*   **Event Listeners:** Event listeners are attached to all interactive elements (`addBtn`, `taskInput` (for "Enter" key), `filterSelect`, `sortSelect`, `searchInput`, `clearCompletedBtn`) to trigger the appropriate JavaScript functions and re-render the UI.
*   **Initialization:**
    *   `setInterval(renderClock, 1000)`: Sets up a recurring timer to update the clock every second.
    *   `renderClock()`: Calls the clock renderer immediately on load.
    *   `render()`: Performs an initial render of the task list when the page loads.

#### Limitations

*   **No Data Persistence:** All task data is stored in the browser's memory. If the page is refreshed or closed, all tasks will be lost. There is no server-side component (e.g., `app.py` is empty) or local storage integration to save data.
*   **No Backend Integration:** The application is purely client-side and does not interact with any backend services for data storage, retrieval, or complex processing.

## Usage

To run the `sample-app.html` application:

1.  **Save the file:** Save the provided HTML content as `sample-app.html` on your local machine.
2.  **Open in Browser:** Open the `sample-app.html` file using any modern web browser (e.g., Chrome, Firefox, Safari, Edge).

The task board application will load, and you can begin adding and managing tasks immediately.