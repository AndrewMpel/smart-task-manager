import json


tasks = []

def addTask(text):

    tasks.append({"Task":text,"Completed":False})

def remTask(id):
    if 0 <= id - 1 < len(tasks): 
        tasks.pop(id - 1)

def clearList():
    tasks.clear()

def saveList():
    with open("List.json",'w') as file:
        json.dump(tasks,file,indent=4)
        print("List saved!")

def markDone(id):
     if 0 <= id - 1 < len(tasks): 
        tasks[id - 1]["Completed"] = True

def loadList():
    global tasks
    try:
        with open("List.json", 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("File not found")
while True:
    if tasks != []:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
            
    print("=======================================")
    print("1. Add Task\n2. Remove Task\n3. Clear List\n4. Save List\n5. Load List\n6. Mark Done\n7. Exit")
    try:
        x = int(input("-> "))
        
        if x == 1:
            text = input("Write a note to add: ")
            addTask(text)
        elif x == 2:
            id = int(input("Select the number of the task to remove: "))
            remTask(id)
        elif x == 3:
            clearList()
        elif x == 4:
            saveList()
        elif x == 5:
            loadList()
        elif x == 6:
             id = int(input("Select the number of the task to change: "))
             markDone(id)
        elif x == 7:
            break
    except ValueError:
        print("Please enter a valid number.")
        continue