import unittest
from projects import Projects
from tasks import Task

class TestProject(unittest.TestCase):
    def test_create_project(self):
        project = Projects("Test Project", "This is a test project")
        self.assertEqual(project.name, "Test Project")
        self.assertEqual(project.description, "This is a test project")

    def test_add_task_to_project(self):
        project = Projects("Test Project", "This is a test project")
        task = Task("Test Task", "This is a test task", "John Doe", "2024-05-01")
        project.add_task(task)
        self.assertIn(task, project.tasks)

    # Add more test cases for other functionalities

class TestTask(unittest.TestCase):
    def test_create_task(self):
        task = Task("Test Task", "This is a test task", "John Doe", "2024-05-01")
        self.assertEqual(task.name, "Test Task")
        self.assertEqual(task.description, "This is a test task")

    # Add more test cases for other functionalities

if __name__ == '__main__':
    unittest.main()
