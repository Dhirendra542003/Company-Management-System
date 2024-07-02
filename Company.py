
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

class TaskManagerApp:
    def init(self, root):
        self.root = root
        self.root.title("Task and Employee Manager")

        # Initialize MySQL connection
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="yourusername",
                password="yourpassword",
                database="task_manager"
            )
            self.mycursor = self.mydb.cursor()
        except Error as e:
            messagebox.showerror("Error", f"Error connecting to MySQL: {e}")

        # Initialize tasks list
        self.tasks = []

        # Task input
        self.task_label = tk.Label(self.root, text="Task:")
        self.task_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)

        # Employee ID input
        self.emp_id_label = tk.Label(self.root, text="Employee ID:")
        self.emp_id_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.emp_id_entry = tk.Entry(self.root)
        self.emp_id_entry.grid(row=1, column=1, padx=10, pady=10)

        # Employee salary input
        self.salary_label = tk.Label(self.root, text="Salary:")
        self.salary_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.salary_entry = tk.Entry(self.root)
        self.salary_entry.grid(row=2, column=1, padx=10, pady=10)

        # Add task button
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=2, padx=10, pady=10)

        # Task list
        self.task_listbox = tk.Listbox(self.root, width=60, height=10)
        self.task_listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        # Buttons for task actions
        mark_complete_button = tk.Button(self.root, text="Mark Complete", command=self.mark_complete)
        mark_complete_button.grid(row=4, column=0, padx=10, pady=10)

        remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=4, column=1, padx=10, pady=10)

        # Add employee button
        add_emp_button = tk.Button(self.root, text="Add Employee", command=self.add_employee)
        add_emp_button.grid(row=4, column=2, padx=10, pady=10)

        # Display employees button
        display_emp_button = tk.Button(self.root, text="Display Employees", command=self.display_employees)
        display_emp_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_complete(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.itemconfig(index, {'fg': 'gray'})
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            self.tasks.pop(index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def add_employee(self):
        emp_id = self.emp_id_entry.get()
        salary = self.salary_entry.get()
        if emp_id and salary:
            try:
                sql = "INSERT INTO employees (emp_id, salary) VALUES (%s, %s)"
                values = (emp_id, salary)
                self.mycursor.execute(sql, values)
                self.mydb.commit()
                messagebox.showinfo("Success", "Employee added successfully.")
                self.emp_id_entry.delete(0, tk.END)
                self.salary_entry.delete(0, tk.END)
            except Error as err:
                messagebox.showerror("Error", f"Error: {err}")
        else:
            messagebox.showwarning("Warning", "Please enter employee ID and salary.")

    def display_employees(self):
        self.task_listbox.delete(0, tk.END)  # Clear task listbox
        try:
            self.mycursor.execute("SELECT * FROM employees")
            employees = self.mycursor.fetchall()
            for emp in employees:
                self.task_listbox.insert(tk.END, f"ID: {emp[0]}, Salary: {emp[1]}")
        except Error as err:
            messagebox.showerror("Error", f"Error: {err}")

if _name_ == "main":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
