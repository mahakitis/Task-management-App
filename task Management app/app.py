import tkinter as tk
from tkinter import messagebox, ttk

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Management App")

        self.main_frame = tk.Frame(root, padx=10, pady=10)
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.main_frame, text="--- Welcome to the Task Management App ---", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=(0, 20))

        self.task_frame = tk.Frame(self.main_frame)
        self.task_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.task_frame, height=8, width=50, font=("Helvetica", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.task_entry = tk.Entry(self.main_frame, width=40, font=("Helvetica", 12))
        self.task_entry.pack(pady=10)

        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)

        self.add_task_button = tk.Button(self.button_frame, text="Add Task", width=15, command=self.add_task, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.add_task_button.grid(row=0, column=0, padx=5)

        self.update_task_button = tk.Button(self.button_frame, text="Update Task", width=15, command=self.update_task, bg="#FFC107", fg="black", font=("Helvetica", 12, "bold"))
        self.update_task_button.grid(row=0, column=1, padx=5)

        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", width=15, command=self.delete_task, bg="#F44336", fg="white", font=("Helvetica", 12, "bold"))
        self.delete_task_button.grid(row=0, column=2, padx=5)

        self.exit_button = tk.Button(self.main_frame, text="Exit", width=15, command=root.quit, bg="#9E9E9E", fg="black", font=("Helvetica", 12, "bold"))
        self.exit_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter the updated task.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
