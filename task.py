class TaskList:
    """A class to manage a list of tasks."""

    def __init__(self):
        """Initialise an empty list of tasks."""
        self.tasks = []

    def add_task(self, task: str):
        """Add a task to the task list."""

        if not isinstance(task, str):
            raise ValueError("Task must be a string")

        self.tasks.append(task)

    def display_tasks(self):
        """Display all tasks in the task list."""

        for task in self.tasks:
            print(task)