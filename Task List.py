#To Do List app

#Initiate a list
tasks  = [ ]

#View tasks
def view_task():
    if len(tasks) == 0:
        print("Your task list is empty")
    else:
        print("You have the following tasks: ")
        for i, task in enumerate(tasks):1
        print(f"{i+1}. {task}")

#Add tasks
def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"{task} has been added to your list.")



#Remove tasks
def remove_task():
    if len(tasks) == 0:
        print("There are no tasks for you to remove.")
    try:     
        task_num = int(input("\nEnter the # of the task you would like to remove: ")) - 1
        removed_task = tasks.pop(task_num)
        print(f"{removed_task} has been removed for your list.")
    except (IndexError, ValueError):
        print("Invalid task number. Please try again.")

#Complete tasks
def complete_task():
    task = int(input("\nEnter a task to mark completed: ")) - 1
    completed_task = tasks.pop(task)
    print(f"{completed_task} has been completed!")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Remove Tasks")
        print("4. Complete Tasks")
        print("5. Quit")
        
        choice = int(input("\nChoose an option (1-5): "))

        if choice == 1:
            view_task()
        elif choice == 2:
            add_task()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            complete_task()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please try again")

main()
