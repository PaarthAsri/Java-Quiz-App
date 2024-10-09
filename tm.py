import tkinter as tk
from tkinter import ttk, messagebox

# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    title = title_entry.get()
    description = description_entry.get("1.0", tk.END)
    if title.strip() == "":
        messagebox.showerror("Error", "Please enter a title for the task.")
        return
    tasks.append({"title": title, "description": description})
    tasks_listbox.insert(tk.END, title)
    clear_entries()
    messagebox.showinfo("Success", "Task added successfully!")

# Function to clear entry fields
def clear_entries():
    title_entry.delete(0, tk.END)
    description_entry.delete("1.0", tk.END)

# Function to view selected task details
def view_selected_task(event):
    selection = tasks_listbox.curselection()
    if selection:
        idx = selection[0]
        task = tasks[idx]
        title_entry.delete(0, tk.END)
        title_entry.insert(0, task["title"])
        description_entry.delete("1.0", tk.END)
        description_entry.insert(tk.END, task["description"])

# Function to delete a task
def delete_task():
    selection = tasks_listbox.curselection()
    if selection:
        idx = selection[0]
        deleted_task = tasks.pop(idx)
        tasks_listbox.delete(idx)
        messagebox.showinfo("Success", f"Task '{deleted_task['title']}' deleted successfully!")
    else:
        messagebox.showerror("Error", "Please select a task to delete.")

# Create main window
root = tk.Tk()
root.title("Task Manager")

# Add style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="white", background="#4CAF50", font=('Helvetica', 10))
style.map("TButton", foreground=[('pressed', 'black'), ('active', 'blue')])

# Create GUI elements with styling
title_label = ttk.Label(root, text="Title:")
title_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

title_entry = ttk.Entry(root, width=50)
title_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=5)

description_label = ttk.Label(root, text="Description:")
description_label.grid(row=1, column=0, sticky="nw", padx=10, pady=5)

description_entry = tk.Text(root, width=50, height=4)
description_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=5)

add_button = ttk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=2, column=0, padx=10, pady=5)

delete_button = ttk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=1, padx=10, pady=5)

tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.grid(row=3, column=0, columnspan=4, padx=10, pady=5)
tasks_listbox.bind("<<ListboxSelect>>", view_selected_task)

# Main loop
root.mainloop()
