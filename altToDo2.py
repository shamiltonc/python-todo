import os
import dill;

# Create Todo class.
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(self.tasks[task])

    def show_tasks(self):
        print("\nYour To-Do's:")
        for index, task in enumerate(self.tasks):
            print(f"\033[1;34m{index + 1}. \033[1;37m{task}")

    def clear_tasks(self):
        self.tasks = []

    def download_file(self):
        # Download to-do list.
        # Get current working directory.
        os.getcwd()
        # Change directory to the Downloads folder.
        downloadsFolder = os.path.join( os.getenv('USERPROFILE'), 'Downloads') 
        os.chdir(downloadsFolder)
        # Creating the new text file.
        newFile = open('To-Do.txt', 'w+') 
        #Convert list to string.
        stringTasks = '\n'.join(map(str, todo_list.tasks))
        # Write to the new file.
        newFile.write(stringTasks)
        newFile.close()

        print("Your file has been downloaded! It's in your Downloads folder.")

    def upload_file(self, fileNameInput):
        # Upload a to-do list.
        fileName = fileNameInput + ".txt"
        #Upload file
        os.getcwd()
        downloadsFolder = os.path.join( os.getenv('USERPROFILE'), 'Downloads') 
        os.chdir(downloadsFolder)
        myFile = os.open(fileName, os.O_RDONLY)
        myData = os.read(myFile, 105)
        myStr = myData.decode("UTF-8")
        todo_list.tasks = list(myStr.split("\n"))
        todo_list.show_tasks()

    def __exit__(self):
        self.logFile.close()

todo_list = TodoList()

def introduction():
    # Print an itroduction to the program.
    print("Your To-Do List")
    print("\nUpon starting, this program will upload a file in your Downloads folder called 'To-Do.txt'.")
    begin = input("\nAre you ready to begin? Y/N: ")
    if begin == "Y":
        # Perform initial upload of the user's to-do list, if it exists.
        uploadInitial()
        # Show tasks.
        todo_list.show_tasks()
        # Start menu.
        showMenu()

# Print out your todo list.
#todo_list.show_tasks()

def uploadInitial():
    os.getcwd()
    downloadsFolder = os.path.join( os.getenv('USERPROFILE'), 'Downloads') 
    os.chdir(downloadsFolder)
    check_file = os.path.isfile(downloadsFolder + "/To-Do.txt")
    #print(check_file)
    if check_file == True:
        todo_list.upload_file("To-Do")
    elif check_file == False:
        print("\nNo file in your Downloads called 'To-Do.txt'!")

def showMenu():
    # Options.
    print("\nOptions: ")
    print("1. Create task")
    print("2. Delete task")
    print("3. Show tasks")
    print("4. Download list")
    print("5. Upload list")
    print("6. Save session")
    print("7. Load session")
    print("8. Exit")

    makeChoice(input("\nYour choice: "))
    
def makeChoice(choice):
    # Input your choice.
    if choice == "1":
        #Create a task.
        newTask = input("What is your task? > ")
        if isinstance (newTask, str):
            todo_list.add_task(newTask)

    elif choice == "2":
        #Delete a task.
        deleteInput = input("What # task are you deleting? > ")
        # If input is numeric, then convert it into an integer.
        if deleteInput.isnumeric():
            deleteTask = int(deleteInput) - 1
        # Else, print error.
        else:
            print("Error: Input was not numeric.")
            
        # If task exists, then delete it.
        if 0 <= deleteTask < len(todo_list.tasks):
            todo_list.remove_task(deleteTask)
        # Else if task doesn't exist, return an error.
        else:
            print("Not a valid selection. Please try again!")

    elif choice == "3":
        #Show tasks.
        todo_list.show_tasks()
    
    elif choice == "4":
        # Download to-do list.
        todo_list.download_file()
    
    elif choice == "5":
        # Get name of file.
        print("Upload a file from your Downloads folder. Make sure it's a .txt file.")
        fileNameInput = input("What is the name of the file? No quotes or file extension. > ")

        # If input is a string, upload the todo list.
        if isinstance(fileNameInput, str):
            # Upload to-do list.
            todo_list.upload_file(fileNameInput)
        # Else, print an error.
        else:
            print("Invalid input!")

    elif choice == "6":
        #Save session.
        dill.dump_session('./todo_session.pkl')
    
    elif choice =="7":
        #Load session.
        dill.load_session('./todo_session.pkl')

    elif choice =="8":
        #Exit program.
        return

    elif choice == "":
        #Print error if Enter is entered.
        print("\nPlease make a choice.")
         
    else:
        #Print error if selectioni isn't valid.
        print("\nNot a valid selection.")

    # Show menu again after selection is made.
    showMenu()

def main():
   # Show the introduction at start of program.
   introduction()

if __name__=="__main__":
    main()