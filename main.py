# Завдання 1:
# Бібліотека керування проектами
#
# Опис:
# 	Створіть бібліотеку на Python, яка дозволяє керувати проектами та їх завданнями.
# Бібліотека повинна дозволяти створювати проекти, додавати завдання до проектів,
# визначати відповідальних осіб, статуси завдань та дедлайни. Кожен проект і завдання
# повинні зберігатися у файлах.
#
# Функції:
# 	Створення, оновлення, видалення проектів та завдань.
# Визначення відповідальних осіб і дедлайнів.
# Зберігання та завантаження даних проекту у файл.
#
# Потрібно створити:
# 	Окремі модулі для керування проектами, завданнями, винятками та файловими операціями.
# Обробка ситуацій, як-от спроба доступу до неіснуючого проекту або завдання.
# Використання Git для керування версіями коду бібліотеки.
#
# Тестування:
# 	Розробка модульних тестів для перевірки функціональності бібліотеки.

import json
from tasks import Task
class Projects:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "tasks": [task.to_json() for task in self.tasks]
        }

    def from_json(cls, json_data):
        project = cls(json_data['name'], json_data['description'])
        for task_data in json_data['tasks']:
            task = Task.from_json(task_data)
            project.add_task(task)
        return project

    def __str__(self):
        return f"Project: {self.name}\nDescription: {self.description}"

