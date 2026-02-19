# Simple CLI Todo List

This is a command-line tool for managing a todo list. It now includes the ability to mark tasks as complete and view the list with completed tasks separately.

## Usage

To add tasks, run the script with the task(s) as arguments:

```bash
python main.py task1 task2 task3
```

To mark a task as complete, use the `-c` flag followed by the task:

```bash
python main.py -c task1
```

To view all tasks, including completed ones, run the script:

```bash
python main.py
```

To view only completed tasks, run the script:

```bash
python main.py --completed
```

## Persistence

The todo list is saved to a file named `todo.txt`. Each task is added to this file when you run the script. To view the list, run the script again. To clear the list, delete the `todo.txt` file.

## Features

*   **Task Addition:** Add new tasks to the list.
*   **Task Completion:** Mark tasks as complete.
*   **Task Listing:** View all tasks, or only completed tasks.

## Error Handling

The script now handles potential errors when writing to the `todo.txt` file and provides informative error messages.

## Testing

Comprehensive unit tests are included to ensure the functionality of the script.

## New Features

*   **Task Deletion:**  Added the ability to delete tasks from the list using the `-d` flag followed by the task.
*   **List Clearing:** Added a command to clear the entire todo list by deleting the `todo.txt` file.
*   **Improved Error Handling:** Enhanced error handling for file operations, providing more specific error messages.
*   **Task Duplication Prevention:** Prevents adding duplicate tasks to the list.

## Improvements

*   **Comprehensive Testing:** Added new unit tests to cover the new features and edge cases.
*   **Clearer Documentation:** Updated the README to reflect the new features and improvements.

## Example Usage

*   **Add tasks:** `python main.py task1 task2`
*   **Mark task as complete:** `python main.py -c task1`
*   **View completed tasks:** `python main.py --completed`
*   **View all tasks:** `python main.py`
*   **Delete a task:** `python main.py -d task1`
*   **Clear the list:** `python main.py -c task1 -c task2 -d task1 -d task2` (or delete todo.txt)