class Todo:
    def __init__(self):
        self.tasks = []  # Instance-level list instead of class-level
        self.run()

    def display(self):
        """Displays the current tasks with their status"""
        if not self.tasks:
            print("\nNo tasks added yet!\n")
            return

        print("\nYour Tasks:")
        for idx, task in enumerate(self.tasks):
            status = "✔ Completed" if task[1] else "❌ Not Completed"
            print(f"{idx}. {task[0]} - {status}")
        print()

    def add_task(self):
        """Adds a new task"""
        todo = input("\nEnter your task: ")
        self.tasks.append([todo, False])  # Task structure: [task_name, is_completed]
        print(f"'{todo}' added!\n")

    def remove_task(self):
        """Removes a task by index"""
        self.display()
        try:
            pos = int(input("Enter the task number to remove: "))
            removed = self.tasks.pop(pos)
            print(f"Removed: {removed[0]}\n")
        except (ValueError, IndexError):
            print("Invalid index!\n")

    def mark_complete(self):
        """Marks a task as completed"""
        self.display()
        try:
            pos = int(input("Enter the task number to mark as completed: "))
            self.tasks[pos][1] = True
            print(f"Task '{self.tasks[pos][0]}' marked as completed!\n")
        except (ValueError, IndexError):
            print("Invalid index!\n")

    def run(self):
        """Main loop for handling user choices"""
        while True:
            print("\nYour Choices:")
            print("1: Add Task")
            print("2: Remove Task")
            print("3: Show Tasks")
            print("4: Mark Task as Completed")
            print("5: Exit")

            try:
                choice = int(input("\nEnter your choice: "))
            except ValueError:
                print("Invalid input! Please enter a number.\n")
                continue

            match choice:
                case 1:
                    self.add_task()
                case 2:
                    self.remove_task()
                case 3:
                    self.display()
                case 4:
                    self.mark_complete()
                case 5:
                    print("Thank you for using the To-Do List CLI. Goodbye!\n")
                    break
                case _:
                    print("Invalid choice! Please enter a number between 1 and 5.\n")


# Run the To-Do List CLI
sarvs = Todo()
