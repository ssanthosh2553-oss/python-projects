import tkinter as tk
from tkinter import simpledialog, messagebox

tasks = []

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Title
title = tk.Label(root, text="📋 TO-DO LIST", font=("Arial", 18, "bold"))
title.pack(pady=10)

# Task listbox
listbox = tk.Listbox(root, font=("Arial", 12), height=10)
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Function to add task
def add_task():
    task = simpledialog.askstring("Add Task", "Enter a new task:")
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        messagebox.showinfo("Success", "✅ Task added successfully")

# Function to delete task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
        messagebox.showinfo("Success", "❌ Task deleted")
    except:
        messagebox.showwarning("Error", "⚠ Please select a task to delete")

# Function to view tasks
def view_tasks():
    if len(tasks) == 0:
        messagebox.showinfo("Tasks", "⚠ No tasks available")
    else:
        task_list = "\n".join([f"{i+1}. {tasks[i]}" for i in range(len(tasks))])
        messagebox.showinfo("Your Tasks", task_list)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Buttons
add_btn = tk.Button(button_frame, text="Add Task", command=add_task, width=10, bg="green", fg="white")
add_btn.grid(row=0, column=0, padx=5)

view_btn = tk.Button(button_frame, text="View Tasks", command=view_tasks, width=10, bg="blue", fg="white")
view_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(button_frame, text="Delete Task", command=delete_task, width=10, bg="red", fg="white")
delete_btn.grid(row=0, column=2, padx=5)

# Run the GUI
root.mainloop()

