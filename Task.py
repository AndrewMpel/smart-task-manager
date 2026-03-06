from datetime import datetime

class Task:
    def __init__(self, text, completed=False, date_str=None):
        self.text = text
        self.completed = completed
        
        if date_str is None:
            now = datetime.now()
            self.date = now.strftime("%Y-%m-%d")
        else:
            self.date = date_str

    def markDone(self):
        self.completed = not self.completed

    def to_dict(self):
        return {
            "Task": self.text,
            "Completed": self.completed,
            "Date": self.date
        }