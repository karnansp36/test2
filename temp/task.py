import tkinter as tk
from tkinter import messagebox
import sqlite3
import mysql.connector
# pip install mysql-connector-python

# ---------------- DATABASE ----------------
# def connect_db():
#     return sqlite3.connect("tasks.db")

def connect_db():
   return mysql.connector.connect(
       host="localhost",
       user="root",       
       password="kalkimaster3.6.9",
       database="dj_pro",
       port = 3306
   )
    
# def create_table():
#      conn = connect_db()
#      cursor = conn.cursor()
#      cursor.execute("""
#          CREATE TABLE IF NOT EXISTS tasks (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              title TEXT NOT NULL,
#              description TEXT
#          )
#      """)
#      conn.commit()
#      conn.close()

# ---------------- CRUD OPERATIONS ----------------
def add_task():
    title = title_entry.get()
    desc = desc_entry.get("1.0", tk.END).strip()

    if title == "":
        messagebox.showwarning("Validation", "Title is required")
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (title, desc))
    conn.commit()
    conn.close()

    clear_fields()
    load_tasks()

def load_tasks():
    task_list.delete(0, tk.END)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    # rows = [{"id":1, "title":"django"}, {"id":2, "title":"django"}]
    # rows = [(1, "django"), (2, "django")]
    for row in rows:
   
        task_list.insert(tk.END, f"{row[0]} - {row[1]}")

def get_task(event):
    selected = task_list.get(tk.ACTIVE)
    if not selected:
        return
    # a = "1 - ti - tle"
    # a =[ "1", "ti" , "tle"]
    task_id = selected.split(" - ")[0]

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT title, description FROM tasks WHERE id=%s", (task_id,))
    task = cursor.fetchone()
    conn.close()

    clear_fields()
    title_entry.insert(0, task[0])
    desc_entry.insert("1.0", task[1])

def update_task():
    selected = task_list.get(tk.ACTIVE)
    if not selected:
        messagebox.showwarning("Select", "Select a task to update")
        return

    task_id = selected.split(" - ")[0]
    title = title_entry.get()
    desc = desc_entry.get("1.0", tk.END).strip()

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title=%s, description=%s WHERE id=%s",
        (title, desc, task_id)
    )
    conn.commit()
    conn.close()

    clear_fields()
    load_tasks()

def delete_task():
    selected = task_list.get(tk.ACTIVE)
    if not selected:
        messagebox.showwarning("Select", "Select a task to delete")
        return

    task_id = selected.split(" - ")[0]

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()

    clear_fields()
    load_tasks()

def clear_fields():
    title_entry.delete(0, tk.END)
    desc_entry.delete("1.0", tk.END)

# ---------------- UI ----------------
root = tk.Tk()
root.title("Task Management App")
root.geometry("500x450")

tk.Label(root, text="Task Title").pack(pady=5)
title_entry = tk.Entry(root, width=50)
title_entry.pack()

tk.Label(root, text="Task Description").pack(pady=5)
desc_entry = tk.Text(root, width=50, height=5)
desc_entry.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=10, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=10, command=update_task).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_task).grid(row=0, column=2, padx=5)

tk.Label(root, text="Tasks").pack()
task_list = tk.Listbox(root, width=60)
task_list.pack(pady=5)
task_list.bind("<<ListboxSelect>>", get_task)

# ---------------- INIT ----------------
# create_table()
load_tasks()
root.mainloop()
