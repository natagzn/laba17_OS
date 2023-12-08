#!/usr/bin/env python3.10

import subprocess
import tkinter as tk
from tkinter import messagebox
import psutil


class ProcessManager:
    def __init__(self):
        self.proc = []
        self.c = 0
        self.pri = [
            "Idle",
            "BelowNormal",
            "Normal",
            "AboveNormal",
            "High",
            "RealTime"
        ]
        self.index_last_process = 0

        self.root = tk.Tk()
        self.root.title("Process Manager")

        self.create_widgets()

    def create_widgets(self):
        # Set window background color to milky coffee style
        self.root.configure(bg="#ffaa50")  # You can adjust the color code as needed

        # Frame for process creation
        create_frame = tk.Frame(self.root, bg="#ffaa50")  # Set background color to milky coffee style
        create_frame.pack(pady=10)

        tk.Label(create_frame, text="Number of Processes:", bg="#ffaa50").grid(row=0, column=0, padx=5)
        self.num_processes_entry = tk.Entry(create_frame)
        self.num_processes_entry.grid(row=0, column=1, padx=5)
        tk.Button(create_frame, text="Create Processes", command=self.create_processes, bg="white").grid(row=0, column=2, padx=5)

        # Frame for process management
        manage_frame = tk.Frame(self.root, bg="#ffaa50")
        manage_frame.pack(pady=10)

        tk.Label(manage_frame, text="Process Management:", bg="#ffaa50", font=("Helvetica", 12)).grid(row=0, column=0, columnspan=2)

        tk.Label(manage_frame, text="Select Process:", bg="#ffaa50").grid(row=1, column=0, sticky='w', padx=5)
        self.process_select_combo = tk.StringVar()
        self.process_select_combo.set("0")
        tk.OptionMenu(manage_frame, self.process_select_combo, *map(str, range(8))).grid(row=1, column=1, sticky='w', padx=5)

        tk.Label(manage_frame, text="Select Priority:", bg="#ffaa50").grid(row=2, column=0, sticky='w', padx=5)
        self.priority_select_combo = tk.StringVar()
        self.priority_select_combo.set("Normal")
        tk.OptionMenu(manage_frame, self.priority_select_combo, *self.pri).grid(row=2, column=1, sticky='w', padx=5)

        tk.Button(manage_frame, text="Set Priority", command=self.set_priority, bg="white").grid(row=3, column=0, sticky='w', padx=5)
        tk.Button(manage_frame, text="Kill Process", command=self.kill_process, bg="white").grid(row=3, column=1, sticky='w', padx=5)
        tk.Button(manage_frame, text="Suspend Process", command=self.suspend_process, bg="white").grid(row=4, column=0, sticky='w', padx=5)
        tk.Button(manage_frame, text="Resume Process", command=self.resume_process, bg="white").grid(row=4, column=1, sticky='w', padx=5)

    def create_processes(self):
        try:
            self.c = int(self.num_processes_entry.get())
            for i in range(self.c):
                process = subprocess.Popen(["python3.10", "subprocessor.py"])
                self.proc.append(process)
                self.index_last_process += 1
            tk.messagebox.showinfo("Info", f"{self.c} processes created successfully")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {e}")

    def set_priority(self):
        i = int(self.process_select_combo.get())
        k = self.pri.index(self.priority_select_combo.get())
        if 0 <= i < self.index_last_process and k >= 0:
            try:
                process = psutil.Process(self.proc[i].pid)

                # Set process priority
                process.nice(k - psutil.NORMAL_PRIORITY_CLASS)  # Adjust priority value

                tk.messagebox.showinfo("Info", f"Process {i} priority set to {self.pri[k]}")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {e}")

    def kill_process(self):
        i = int(self.process_select_combo.get())
        if 0 <= i < self.index_last_process:
            try:
                self.proc[i].kill()
                tk.messagebox.showinfo("Info", f"Process {i} killed")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {e}")

    def suspend_process(self):
        i = int(self.process_select_combo.get())
        if 0 <= i < self.index_last_process:
            try:
                process = psutil.Process(self.proc[i].pid)
                process.suspend()
                tk.messagebox.showinfo("Info", f"Process {i} suspended")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {e}")

    def resume_process(self):
        i = int(self.process_select_combo.get())
        if 0 <= i < self.index_last_process:
            try:
                process = psutil.Process(self.proc[i].pid)
                process.resume()
                tk.messagebox.showinfo("Info", f"Process {i} resumed")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {e}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ProcessManager()
    app.run()
