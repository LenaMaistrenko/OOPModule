class Task:
    def __init__(self, name, description, assignee, deadline):
        self.name = name
        self.description = description
        self.assignee = assignee
        self.deadline = deadline
        self.status = "To Do"

    def update_status(self, status):
        self.status = status

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "assignee": self.assignee,
            "deadline": self.deadline,
            "status": self.status
        }

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data['name'], json_data['description'], json_data['assignee'], json_data['deadline'])

    def __str__(self):
        return f"Task: {self.name}\nDescription: {self.description}\nAssignee: {self.assignee}\nDeadline: {self.deadline}\nStatus: {self.status}"
