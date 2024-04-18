class ProjectNotFoundError(Exception):
    def __init__(self, project_name):
        self.project_name = project_name

    def __str__(self):
        return f"Project '{self.project_name}' not found."

class TaskNotFoundError(Exception):
    def __init__(self, task_name):
        self.task_name = task_name

    def __str__(self):
        return f"Task '{self.task_name}' not found."
