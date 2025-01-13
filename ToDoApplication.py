task_list = []
#main To Do Application Menu for user enter one of the 4 options
def todo_menu():
    while True:
        print("\nHello, Welcome to the To Do Application! Let's Manage your 'To Do List'! Menu options:")
        print("Add task")
        print("View tasks")
        print("Delete task")
        print("Exit")
        try:
            menu_selection = input("Enter menu option: ")
            if menu_selection == "Add task":
                add_task()
            elif menu_selection == "View tasks":
                view_tasks()
            elif menu_selection == "Delete task":
                delete_task()
            elif menu_selection == "Exit":
                break
            else: 
                print("Invalid menu selection. Be sure to enter 'Add task', 'View tasks', 'Delete task', or 'Exit' exactly as typed in the menu.")
        except ValueError:
            print("Must enter one of the four menu options. Be sure to enter 'Add task', 'View tasks', 'Delete task', or 'Exit' exactly as typed in the menu.")
        except TypeError:
            print("Must enter one of the four menu options. Be sure to enter 'Add task', 'View tasks', 'Delete task', or 'Exit' exactly as typed in the menu.")
        finally:
            print(f"You entered: {menu_selection}")          
#Function for adding tasks
def add_task():
    task = input("Enter the task that you would like to add to your 'To Do List': ")
    task_list.append(task)
    print(f"{task} was add to your list of things to do")  
#Function for viewing tasks
def view_tasks():
    if len(task_list) == 0:
        print("There are no tasks to veiw. Add a task to your 'To Do List' first.")
    else:
        print("Here is your current 'To Do List' list:")
        for task in task_list:
            print(task)
#Function for deleting tasks
def delete_task():
    global task_list
    if len(task_list) == 0:
        print("There are no tasks to delete.")
    else:
        print("Here is your current 'To Do List' list:")
        for task in task_list:
            print(task)
        try:
            task_to_delete = input("Which of your tasks do you want to delete? ")
            task_list.remove(task_to_delete)
        except ValueError:
            print("Must enter task exactly as typed in the list")
        finally:
            print("Updated task list:")
            for task in task_list:
                print(task)           
todo_menu()
