thislist = []
#Function to show the user Menue
def viewMenue():
    print(f"1. Add a Task")
    print(f"2. Read a Tasks")
    print(f"3. Update a Task")
    print(f"4. Delete a Task")
    print(f"5. Exit a Program")
    
#Function to show the user to add the Task
def addTasks():
    print("Add tasks")
    task = input("What you want to add to do list :")
    thislist.append(task)
    print()

#Function to show the user to read the Tasks
def readTasks():
    print("\n")
    print("*******************************")
    for i in range(len(thislist)):
        print(f"{i+1}. {thislist[i]}")
    print("*******************************")
    print("\n")
    
#Function to show the user to update the Tasks
def updateTasks():
    try:
        print("updateTasks")
        readTasks()
        index = int(input("Enter the task number to update :"))
        newTask = input("Enter a new task :")
        thislist[index-1] = newTask
    except ValueError:
        print("Invalid Index you entered")
        
        
#Function to show the user to delete the Tasks
def deleteTasks():
    try:
        readTasks()
        print("delete task")
        index = int(input("Enter the task number to delete :"))
        thislist.pop(index)
    except ValueError:
        print("You entered an invalid number")

#This is main by which user call different functions
while True:
    viewMenue()
    do = int(input("Enter the number (1 to 5) of the above tasks :"))
    if do == 1:
        addTasks()
    elif do == 2:
        readTasks()
    elif do == 3:
        updateTasks()
    elif do == 4:
        deleteTasks()
    elif do == 5:
        print("\n")
        print("*******************************")
        print("Thanks for using a program")
        print("*******************************")
        print("\n")
        break
    else:
        print("You entered an Invalid input!")
        
        
        
        
