# Import modules using 'import' and 'from'
import random
from math import sqrt

# Define a global variable
global_count = 0

# Define a class
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str, important: bool = False):
        assert task is not None, "Task cannot be None"  # using 'assert' and 'None'
        self.tasks.append((task, important))

    def remove_task(self, index):
        if index < len(self.tasks):
            del self.tasks[index]  # using 'del'
        else:
            raise IndexError("Index out of range")  # using 'raise'

    def display_tasks(self):
        if not self.tasks:  # using 'not'
            print("No tasks available.")
        else:
            for i, (task, important) in enumerate(self.tasks):  # using 'for', 'in'
                tag = "IMPORTANT" if important else "Normal"  # using 'if', 'else'
                print(f"{i}: {task} [{tag}]")

    def filter_important(self):
        return [t for t in self.tasks if t[1] is True]  # using 'is', 'True'

# Use 'def', 'return', 'lambda', and 'pass'
def operation_summary(tasks):
    summary = list(map(lambda t: t[0].upper(), tasks))  # using 'lambda'
    if summary:
        return summary
    else:
        pass  # placeholder if no operation needed

# Using try-except-finally with file I/O and 'with' statement
def read_file(filepath):
    try:
        with open(filepath, 'r') as f:  # using 'with', 'as'
            print(f.read())
    except FileNotFoundError:
        print("File not found!")  # using 'except'
    finally:
        print("File reading complete.")  # using 'finally'

# Using 'while', 'continue', and 'break'
def loop_until_five():
    count = 0
    while True:
        count += 1
        if count == 3:
            continue  # skip number 3
        if count == 6:
            break  # stop at 6
        print("Count:", count)

# Demonstrate 'nonlocal' in a nested function
def counter():
    count = 0
    def increment():
        nonlocal count  # modify enclosing scope variable
        count += 1
        return count
    return increment

# Main logic
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Finish Python assignment", True)
    manager.add_task("Play volleyball")
    manager.display_tasks()

    print("Important tasks:", operation_summary(manager.filter_important()))

    inc = counter()
    print("Counter 1:", inc())  # should print 1
    print("Counter 2:", inc())  # should print 2

    loop_until_five()

    read_file("sample.txt")  # Create sample.txt to test or let it fail