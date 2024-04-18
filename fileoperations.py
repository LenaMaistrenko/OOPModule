import json
from projects import Projects
def save_project_to_file(project, filename):
    with open(filename, 'w') as file:
        json.dump(project.to_json(), file)

def load_project_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return Projects.from_json(data)

