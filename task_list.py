"""
task_list.py
A simple task management system to demonstrate unit testing.

This is the code we'll write tests for. Students will test the
add_task() and display_tasks() methods.
"""


class TaskList:
    """A class to manage a list of tasks."""
    
    def __init__(self):
        """
        Initialize an empty list of tasks.
        
        This runs when you create a new TaskList:
            task_list = TaskList()
        """
        # Create an empty list to store tasks
        self.tasks = []
    
    def add_task(self, task: str):
        """
        Add a task to the task list.
        
        Args:
            task (str): The task to be added
        
        Raises:
            ValueError: If task is not a string
        
        Example:
            >>> task_list = TaskList()
            >>> task_list.add_task("Buy Groceries")
            >>> print(task_list.tasks)
            ['Buy Groceries']
        """
        # Check if task is actually a string
        if not isinstance(task, str):
            raise ValueError("Task must be a string")
        
        # If it passes the check, add it to the list
        self.tasks.append(task)
    
    def display_tasks(self):
        """
        Display all tasks in the task list.
        
        Prints each task on a new line.
        
        Example:
            >>> task_list = TaskList()
            >>> task_list.add_task("Buy Groceries")
            >>> task_list.add_task("Write Code")
            >>> task_list.display_tasks()
            Buy Groceries
            Write Code
        """
        # Loop through each task
        for task in self.tasks:
            # Print the task
            print(task)
    
    def get_task_count(self):
        """
        Get the number of tasks in the list.
        
        Returns:
            int: The number of tasks
        
        Example:
            >>> task_list = TaskList()
            >>> task_list.add_task("Task 1")
            >>> task_list.add_task("Task 2")
            >>> task_list.get_task_count()
            2
        """
        return len(self.tasks)
    
    def clear_tasks(self):
        """
        Remove all tasks from the list.
        
        Example:
            >>> task_list = TaskList()
            >>> task_list.add_task("Task 1")
            >>> task_list.clear_tasks()
            >>> task_list.get_task_count()
            0
        """
        self.tasks = []


# ============================================
# EXAMPLE USAGE (You can run this directly)
# ============================================

if __name__ == "__main__":
    # Create a new task list
    task_list = TaskList()
    
    # Add some tasks
    task_list.add_task("Buy Groceries")
    task_list.add_task("Mark Assessments")
    task_list.add_task("Write Unit Tests")
    
    # Display all tasks
    print("Tasks to do:")
    task_list.display_tasks()
    
    # Show how many tasks we have
    print(f"\nTotal tasks: {task_list.get_task_count()}")
