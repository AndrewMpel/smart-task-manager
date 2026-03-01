from ToDoList import ToDoList
from Task import Task
todo_list = ToDoList()

while True:
    if todo_list.get_tasks() != []:
        for i, task in enumerate(todo_list.get_tasks()):
            print(f"{i + 1}.Task: {task.text}, Date: {task.date}, Completed: {task.completed}")
            
    print("=======================================")
    print("1. Add Task\n2. Remove Task\n3. Clear List\n4. Save List\n5. Load List\n6. Mark Done\n7. Exit")
    try:
        x = int(input("-> "))
        
        if x == 1:
            text = input("Write a note to add: ")
            todo_list.addTask(text)
        elif x == 2:
            id = int(input("Select the number of the task to remove: "))
            todo_list.remTask(id)
        elif x == 3:
            todo_list.clearList()
        elif x == 4:
            todo_list.saveList()
        elif x == 5:
            todo_list.loadList()
        elif x == 6:
             id = int(input("Select the number of the task to change: "))
             todo_list.Done(id)
        elif x == 7:
            break
    except ValueError:
        print("Please enter a valid number.")
        continue
