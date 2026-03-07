import json
from Task import Task
from datetime import datetime
import pandas as pd

class ToDoList:
    def __init__(self):
        self._Tasks = []

    def loadList(self):
        try:
            with open("List.json", 'r') as file:
                self._Tasks.clear()
                data = json.load(file)
                for item in data:
                    loaded_task = Task(item["Task"], item["Completed"], item["Date"])
                    self._Tasks.append(loaded_task)
        except FileNotFoundError:
            print("File not found")

    def addTask(self,text):
        self._Tasks.append(Task(text))

    def remTask(self, id):
        if 0 <= id - 1 < len(self._Tasks): 
            self._Tasks.pop(id - 1)

    def clearList(self):
        self._Tasks.clear()

    def saveList(self):
        with open("List.json",'w') as file:
            dict_list = [task.to_dict() for task in self._Tasks]
            json.dump(dict_list, file, indent=4)
            print("List saved!")

    def get_tasks(self):
        return self._Tasks
    
    def Done(self,id):
        if 0 <= id - 1 < len(self._Tasks): 
            task = self._Tasks[id-1]
            task.markDone()

    def DataFrameConv(self):
        dataframe = pd.read_json("List.json")