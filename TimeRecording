import csv
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

class TaskTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Tracker")
        self.tasks = []

        # Task name
        tk.Label(root, text="Task Name").grid(row=0, column=0)
        self.task_name_entry = tk.Entry(root)
        self.task_name_entry.grid(row=0, column=1)

        # Start time
        tk.Label(root, text="Start Time (HH:MM)").grid(row=1, column=0)
        self.start_time_entry = tk.Entry(root)
        self.start_time_entry.grid(row=1, column=1)

        # End time
        tk.Label(root, text="End Time (HH:MM)").grid(row=2, column=0)
        self.end_time_entry = tk.Entry(root)
        self.end_time_entry.grid(row=2, column=1)

        # Add task button
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=3, column=0, columnspan=2)

    def add_task(self):
        task_name = self.task_name_entry.get()
        start_time_str = self.start_time_entry.get()
        end_time_str = self.end_time_entry.get()

        try:
            current_date = datetime.now().date()
            start_time = datetime.strptime(start_time_str, '%H:%M').time()
            end_time = datetime.strptime(end_time_str, '%H:%M').time()

            start_datetime = datetime.combine(current_date, start_time)
            end_datetime = datetime.combine(current_date, end_time)
            duration = (end_datetime - start_datetime).total_seconds() / 3600  # duration in hours

            task = {
                'task_name': task_name,
                'date': current_date,
                'start_time': start_time,
                'end_time': end_time,
                'duration': duration
            }
            self.tasks.append(task)
            self.write_task_to_csv(task)
            messagebox.showinfo("Success", "Task added and saved to CSV successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")

    def write_task_to_csv(self, task):
        filename = 'C:/users/NAME/LOCATION/task_tracker.csv'  # Change this to your desired path
        file_exists = os.path.isfile(filename)

        with open(filename, 'a', newline='') as csvfile:
            fieldnames = ['task_name', 'date', 'start_time', 'end_time', 'duration']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                'task_name': task['task_name'],
                'date': task['date'].strftime('%Y-%m-%d'),
                'start_time': task['start_time'].strftime('%H:%M'),
                'end_time': task['end_time'].strftime('%H:%M'),
                'duration': task['duration']
            })

# Create the main window
root = tk.Tk()
app = TaskTrackerApp(root)
root.mainloop()
