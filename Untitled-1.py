class Task:
  def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class ToDoList:
  def __init__(self):
        self.tasks = []

def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)

def mark_task_as_completed(self, task_index):
        self.tasks[task_index].completed = True

def update_task_description(self, task_index, new_description):
        self.tasks[task_index].description = new_description

def remove_task(self, task_index):
        del self.tasks[task_index]

def print_to_do_list(self):
    for task in self.tasks:
     if task.completed:
                print("[X]", task.description)
    else:
                print("[ ]", task.description)

def main():
    to_do_list = ToDoList()

    while True:
        print("To-Do List:")
        to_do_list.print_to_do_list()

        command = input("Enter a command (add, mark, update, remove, or quit):")

        if command == "add":
            description = input("Enter a task description: ")
            to_do_list.add_task(description)
        elif command == "mark":
            task_index = int(input("Enter the task index to mark as completed:"))
            to_do_list.mark_task_as_completed(task_index)
        elif command == "update":
            task_index = int(input("Enter the task index to update:"))
            new_description = input("Enter the new task description: ")
            to_do_list.update_task_description(task_index, new_description)
        elif command == "remove":
            task_index = int(input("Enter the task index to remove:"))
            to_do_list.remove_task(task_index)
        elif command == "quit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()