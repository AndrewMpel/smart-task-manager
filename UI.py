from ToDoList import ToDoList
from Task import Task
from tkinter import *
from tkinter import messagebox

class UI:
    def __init__(self):
        self.todo_list = ToDoList()
        self.task_checkboxes = []  # Store checkbox variables
        
        self.window = Tk()
        self.window.geometry("650x750")
        self.window.title("Smart Task Manager")

        # Configure window style
        self.window.configure(bg="#1a1a2e")
        
        # Title Label with modern styling
        self.titleLabel = Label(
            self.window, 
            text="Smart Task Manager", 
            font=("Segoe UI", 24, 'bold'),
            bg="#1a1a2e",
            fg="#eaeaea"
        )
        self.titleLabel.grid(row=0, column=0, columnspan=3, pady=30)

        # Task input section
        self.textField_label = Label(
            self.window, 
            text="Add a new Task:", 
            font=("Segoe UI", 12),
            bg="#1a1a2e",
            fg="#a0a0a0"
        )
        self.textField_label.grid(row=1, column=0, columnspan=3, padx=30, pady=(20, 5), sticky="w")
        
        self.textField = Entry(
            self.window,
            font=("Segoe UI", 12),
            bg="#16213e",
            fg="#eaeaea",
            insertbackground="#eaeaea",
            relief="flat",
            highlightthickness=2,
            highlightbackground="#0f3460",
            highlightcolor="#e94560"
        )
        self.textField.grid(row=2, column=0, columnspan=3, padx=30, pady=5, sticky="ew", ipady=10)
        self.textField.bind("<Return>", lambda e: self.add_task())
        
        # Add button with modern styling
        self.addButton = Button(
            self.window,
            text="+ Add Task",
            font=("Segoe UI", 11, "bold"),
            bg="#e94560",
            fg="#ffffff",
            activebackground="#ff6b6b",
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8,
            command=self.add_task
        )
        self.addButton.grid(row=3, column=0, columnspan=3, padx=30, pady=15, sticky="e")
        
        # Task list label
        self.listLabel = Label(
            self.window,
            text="Your Tasks:",
            font=("Segoe UI", 12),
            bg="#1a1a2e",
            fg="#a0a0a0"
        )
        self.listLabel.grid(row=4, column=0, columnspan=3, padx=30, pady=(10, 5), sticky="w")
        
        # Scrollable task container
        self.taskContainer = Frame(self.window, bg="#16213e", highlightthickness=2, highlightbackground="#0f3460")
        self.taskContainer.grid(row=5, column=0, columnspan=3, padx=30, pady=5, sticky="nsew")
        
        # Canvas for scrolling
        self.canvas = Canvas(self.taskContainer, bg="#16213e", highlightthickness=0)
        self.scrollbar = Scrollbar(self.taskContainer, orient="vertical", command=self.canvas.yview)
        self.scrollableFrame = Frame(self.canvas, bg="#16213e")
        
        self.scrollableFrame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollableFrame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Make scrollable frame expand to canvas width
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.canvas_frame, width=e.width))
        
        # Enable mousewheel scrolling
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Button frame for action buttons
        self.buttonFrame = Frame(self.window, bg="#1a1a2e")
        self.buttonFrame.grid(row=6, column=0, columnspan=3, padx=30, pady=20, sticky="ew")
        
        # Style for action buttons
        button_style = {
            "font": ("Segoe UI", 10),
            "bg": "#0f3460",
            "fg": "#ffffff",
            "activebackground": "#16213e",
            "activeforeground": "#ffffff",
            "relief": "flat",
            "cursor": "hand2",
            "padx": 15,
            "pady": 6
        }
        
        self.removeButton = Button(
            self.buttonFrame,
            text="✕ Remove Selected",
            command=self.remove_task,
            **button_style
        )
        self.removeButton.pack(side=LEFT, padx=5)
        
        self.clearButton = Button(
            self.buttonFrame,
            text="Clear All",
            command=self.clear_list,
            **button_style
        )
        self.clearButton.pack(side=LEFT, padx=5)
        
        self.saveButton = Button(
            self.buttonFrame,
            text="💾 Save",
            command=self.save_list,
            **button_style
        )
        self.saveButton.pack(side=LEFT, padx=5)
        
        self.loadButton = Button(
            self.buttonFrame,
            text="📂 Load",
            command=self.load_list,
            **button_style
        )
        self.loadButton.pack(side=LEFT, padx=5)
        
        # Configure grid weights
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)
        self.window.grid_rowconfigure(5, weight=1)
        
        # Track selected task for removal
        self.selected_task_index = None
        
        # Load existing tasks on startup
        self.load_list()

    def refresh_task_list(self):
        """Refresh the task list with checkboxes"""
        # Clear existing task widgets
        for widget in self.scrollableFrame.winfo_children():
            widget.destroy()
        self.task_checkboxes.clear()
        
        tasks = self.todo_list.get_tasks()
        
        if not tasks:
            # Show empty state
            emptyLabel = Label(
                self.scrollableFrame,
                text="No tasks yet. Add one above!",
                font=("Segoe UI", 11, "italic"),
                bg="#16213e",
                fg="#6a6a6a",
                pady=30
            )
            emptyLabel.pack(fill=X)
            return
        
        for i, task in enumerate(tasks):
            # Create task card frame
            taskFrame = Frame(
                self.scrollableFrame,
                bg="#1a1a2e",
                pady=15,
                padx=15
            )
            taskFrame.pack(fill=X, padx=10, pady=8)
            
            # Checkbox variable
            var = BooleanVar(value=task.completed)
            self.task_checkboxes.append(var)
            
            # Checkbox (larger)
            checkbox = Checkbutton(
                taskFrame,
                variable=var,
                bg="#1a1a2e",
                activebackground="#1a1a2e",
                selectcolor="#0f3460",
                width=2,
                height=1,
                command=lambda idx=i: self.toggle_task(idx)
            )
            checkbox.grid(row=0, column=0, rowspan=2, padx=(10, 20), sticky="w")
            
            # Task text (larger font)
            text_color = "#6a6a6a" if task.completed else "#eaeaea"
            text_style = "overstrike" if task.completed else "normal"
            
            taskText = Label(
                taskFrame,
                text=task.text,
                font=("Segoe UI", 16, text_style),
                bg="#1a1a2e",
                fg=text_color,
                anchor="w"
            )
            taskText.grid(row=0, column=1, sticky="w", pady=(5, 0))
            
            # Task date (larger)
            dateText = Label(
                taskFrame,
                text=f"📅 {task.date}",
                font=("Segoe UI", 11),
                bg="#1a1a2e",
                fg="#5a5a7a",
                anchor="w"
            )
            dateText.grid(row=1, column=1, sticky="w", pady=(0, 5))
            
            # Status badge (larger)
            if task.completed:
                statusText = "✓ Done"
                statusBg = "#2d6a4f"
                statusFg = "#95d5b2"
            else:
                statusText = "○ Pending"
                statusBg = "#e94560"
                statusFg = "#ffffff"
            
            statusBadge = Label(
                taskFrame,
                text=statusText,
                font=("Segoe UI", 11, "bold"),
                bg=statusBg,
                fg=statusFg,
                padx=15,
                pady=5
            )
            statusBadge.grid(row=0, column=2, rowspan=2, padx=15, sticky="e")
            
            # Delete button for individual task (larger)
            deleteBtn = Button(
                taskFrame,
                text="✕",
                font=("Segoe UI", 14, "bold"),
                bg="#1a1a2e",
                fg="#e94560",
                activebackground="#1a1a2e",
                activeforeground="#ff6b6b",
                relief="flat",
                cursor="hand2",
                padx=10,
                pady=5,
                command=lambda idx=i: self.remove_single_task(idx)
            )
            deleteBtn.grid(row=0, column=3, rowspan=2, padx=10, sticky="e")
            
            # Configure column weights
            taskFrame.grid_columnconfigure(1, weight=1)

    def toggle_task(self, index):
        """Toggle task completion status"""
        task_id = index + 1
        self.todo_list.Done(task_id)
        self.refresh_task_list()

    def add_task(self):
        """Add a new task"""
        text = self.textField.get().strip()
        if text:
            self.todo_list.addTask(text)
            self.textField.delete(0, END)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def remove_single_task(self, index):
        """Remove a specific task by index"""
        task_id = index + 1
        self.todo_list.remTask(task_id)
        self.refresh_task_list()

    def remove_task(self):
        """Remove completed tasks"""
        tasks = self.todo_list.get_tasks()
        completed = [i for i, t in enumerate(tasks) if t.completed]
        if completed:
            if messagebox.askyesno("Confirm", "Remove all completed tasks?"):
                # Remove from end to start to maintain indices
                for i in reversed(completed):
                    self.todo_list.remTask(i + 1)
                self.refresh_task_list()
        else:
            messagebox.showinfo("Info", "No completed tasks to remove!")

    def mark_done(self):
        """Mark the selected task as done"""
        selection = self.taskListbox.curselection()
        if selection:
            task_id = selection[0] + 1  # Convert to 1-based index
            self.todo_list.Done(task_id)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as done!")

    def clear_list(self):
        """Clear all tasks"""
        if self.todo_list.get_tasks():
            if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
                self.todo_list.clearList()
                self.refresh_task_list()
        else:
            messagebox.showinfo("Info", "The list is already empty!")

    def save_list(self):
        """Save tasks to file"""
        self.todo_list.saveList()
        messagebox.showinfo("Success", "Tasks saved successfully!")

    def load_list(self):
        """Load tasks from file"""
        self.todo_list.loadList()
        self.refresh_task_list()

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = UI()
    app.start()