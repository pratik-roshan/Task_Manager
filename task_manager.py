import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")

        self.tasks = []

        self.task_name_var = tk.StringVar()
        self.priority_var = tk.IntVar()

        # Task Name Entry
        tk.Label(master, text="Task Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(master, textvariable=self.task_name_var).grid(row=0, column=1, padx=10, pady=10)

        # Priority Entry
        tk.Label(master, text="Priority (1-7):").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(master, textvariable=self.priority_var).grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        tk.Button(master, text="Add Task", command=self.add_task).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(master, text="Delete Task", command=self.delete_task).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(master, text="Prioritize Tasks", command=self.prioritize_tasks).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(master, text="Mark as Completed", command=self.mark_as_completed).grid(row=4, column=0, columnspan=2, pady=10)

        # Task List
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, height=10, width=50)
        self.task_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Populate initial tasks
        self.update_task_list()

    def add_task(self):
        task_name = self.task_name_var.get()
        priority = self.priority_var.get()

        if task_name and 1 <= priority <= 7:
            task = {'name': task_name, 'priority': priority, 'completed': False}
            self.tasks.append(task)
            self.update_task_list()
            messagebox.showinfo("Success", f"Task '{task_name}' added with priority {priority}.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter valid task name and priority (1-7).")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            task_name = self.tasks[selected_index]['name']
            del self.tasks[selected_index]
            self.update_task_list()
            messagebox.showinfo("Success", f"Task '{task_name}' deleted.")
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")

            
    def prioritize_tasks(self):
        # Separate completed and uncompleted tasks
        uncompleted_tasks = [task for task in self.tasks if not task['completed']]
        completed_tasks = [task for task in self.tasks if task['completed']]

        # Sort uncompleted tasks by priority (higher priority first)
        uncompleted_tasks = sorted(uncompleted_tasks, key=lambda x: x['priority'], reverse=False)

        # Combine uncompleted and completed tasks
        self.tasks = uncompleted_tasks + completed_tasks

        # Update the task list in the GUI
        self.update_task_list()


    def mark_as_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            task_name = self.tasks[selected_index]['name']
            self.tasks[selected_index]['completed'] = True
            self.update_task_list()
            messagebox.showinfo("Success", f"Task '{task_name}' marked as completed.")
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task['completed'] else "Not Completed"
            self.task_listbox.insert(tk.END, f"Task: {task['name']}, Priority: {task['priority']}, Status: {status}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
