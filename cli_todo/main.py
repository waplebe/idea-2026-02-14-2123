import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="A simple command-line todo list.")
    parser.add_argument("task", nargs='*', help="The task to add.")
    parser.add_argument("-c", "--complete", nargs='?', help="Mark a task as complete.")
    parser.add_argument("--completed", action="store_true", help="View only completed tasks.")

    args = parser.parse_args()

    if not args.task:
        print("No tasks provided.")
        return

    tasks = []
    completed_tasks = []

    # Load tasks from file
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as f:
            for line in f:
                task = line.strip()
                if task:
                    tasks.append(task)

    # Process tasks
    for task in args.task:
        if task:
            tasks.append(task)

    for task in tasks:
        if args.complete and task in args.task:
            completed_tasks.append(task)
        else:
            tasks.remove(task)

    # Print tasks
    if args.completed:
        print("Completed Tasks:")
        for task in completed_tasks:
            print(f"- {task}")
    else:
        print("Tasks:")
        for task in tasks:
            print(f"- {task}")

    # Save tasks to file
    try:
        with open("todo.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()