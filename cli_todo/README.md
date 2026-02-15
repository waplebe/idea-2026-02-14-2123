# Simple CLI Todo List

This is a very basic command-line tool for managing a todo list.

## Usage

To add tasks, run the script with the task(s) as arguments:

```bash
python main.py task1 task2 task3
```

This will print the list of tasks to the console.

## Persistence

Now the todo list is saved to a file named `todo.txt`.  Each task is added to this file when you run the script.  To view the list, run the script again.  To clear the list, delete the `todo.txt` file.