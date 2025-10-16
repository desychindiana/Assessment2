def menu():
    while True:
        print("""
        =====================================
        || Welcome to the Password Manager  ||
        || Developed by Apps2U for DigiCore ||
        =====================================
        Securely manage and store your credentials        
              
        Please make your selection below by typing 1, 2 or 3
        1. Add a new credential
        2. View stored credentials      
        3. Exit
        """)
        choice = input(">")


        if choice == "1":
            add_credential()
        elif choice == "2":
            view_credential()
        elif choice == "3":
            exit()
            break
        else:
            print("Invalid choice. Please type 1, 2, or 3")
        
def add_credential():
    print("You have selected option 1. Please enter the information below:")
    username = input("Username: ")
    password = input("Password: ")
    url = input("URL: ")

def view_credential():
    print("You have selected option 2.")

def exit():
    print("You have selected option 3. Exiting now...")

menu()