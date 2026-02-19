import unittest
import main
import os

class TestMain(unittest.TestCase):

    def setUp(self):
        # Clear the todo.txt file before each test
        if os.path.exists("todo.txt"):
            os.remove("todo.txt")

    def test_add_tasks(self):
        main.main("task1", "task2")
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].strip(), "task1")
        self.assertEqual(tasks[1].strip(), "task2")

    def test_complete_task(self):
        main.main("-c", "task1")
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].strip(), "task1")

    def test_view_completed_tasks(self):
        main.main("--completed")
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertEqual(len(tasks), 0)

    def test_view_all_tasks(self):
        main.main()
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertEqual(len(tasks), 0)

    def test_no_tasks_provided(self):
        main.main()
        self.assertEqual(print("No tasks provided."), True)

    def test_complete_nonexistent_task(self):
        main.main("-c", "task1")
        self.assertTrue(os.path.exists("todo.txt"))
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertEqual(len(tasks), 0)

    def test_add_and_complete_task(self):
        main.main("task1", "-c", "task1")
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertEqual(len(tasks), 0)

    def test_add_multiple_tasks_and_complete_some(self):
        main.main("task1", "task2", "-c", "task1")
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].strip(), "task2")

    def test_clear_list(self):
        main.main("-c", "task1", "-c", "task2")
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertEqual(len(tasks), 0)