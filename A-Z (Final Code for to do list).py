import tkinter as tk
from tkinter import simpledialog, colorchooser

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        # Create task selection box
        self.task_selection_label = tk.Label(self.root, text="Select Task")
        self.task_selection_label.pack(pady=5)
        self.task_selection_box = tk.Listbox(self.root, width=40, height=5)
        self.task_selection_box.pack(pady=10)

        # Create task entry box
        self.task_entry_box = tk.Entry(self.root, width=40)
        self.task_entry_box.pack(pady=5)

        # Create buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        self.add_task_button = tk.Button(button_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.TOP, padx=5, pady=5)

        self.delete_task_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(side=tk.TOP, padx=5, pady=5)

        self.mark_task_done_button = tk.Button(button_frame, text="Mark as Done", command=self.mark_task_done)
        self.mark_task_done_button.pack(side=tk.TOP, padx=5, pady=5)

        # Create task list box
        self.task_list_label = tk.Label(self.root, text="To Do List")
        self.task_list_label.pack(pady=5)
        self.task_list_box = tk.Listbox(self.root, width=40, height=10)
        self.task_list_box.pack(pady=10)

        # Create customize bg color button
        self.customize_bg_color_button = tk.Button(self.root, text="Customize BG Color", command=self.customize_bg_color)
        self.customize_bg_color_button.pack(pady=5)

        # Load tasks from file
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    self.tasks.append(line.strip())
                    self.task_selection_box.insert(tk.END, line.strip())
                    self.task_list_box.insert(tk.END, line.strip())
        except FileNotFoundError:
            pass

    def add_task(self):
        task = self.task_entry_box.get()
        if task:  # Check if the entry box is not empty
            self.tasks.append(task)  # Add the task to the tasks list
            self.task_selection_box.insert(tk.END, task)  # Add the task to the selection box
            self.task_list_box.insert(tk.END, task)  # Add the task to the task list box
            self.task_entry_box.delete(0, tk.END)  # Clear the entry box after adding the task

    def delete_task(self):
        selected_task_index = self.task_selection_box.curselection()
        if selected_task_index:
            task = self.task_selection_box.get(selected_task_index)
            self.tasks.remove(task)  # Remove from the tasks list
            self.task_selection_box.delete(selected_task_index)  # Remove from the selection box
            self.task_list_box.delete(selected_task_index)  # Remove from the task list box

    def mark_task_done(self):
        selected_task_index = self.task_selection_box.curselection()
        if selected_task_index:
            task = self.task_selection_box.get(selected_task_index)
            # Here you might want to mark the task done in some way, e.g., change its appearance
            self.task_selection_box.delete(selected_task_index)  # Remove from the selection box
            self.task_list_box.delete(selected_task_index)  # Remove from the task list box
            # Optionally, you could append it to a "done" list or change its appearance

    def customize_bg_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.root.configure(bg=color)

if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()