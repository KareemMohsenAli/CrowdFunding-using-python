# def loginfun():
#     print("login")
import os
import create
import update
import delete
import view
def get_user():
    email = input("Email: ")
    password = input("Password: ")
    f = open("userFile.txt", 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        tmp = line.split(':')
        if tmp[3] == email and tmp[4] == password:
            os.system("clear")
            print("Welcome to the Registration System")
            print("Login Succeeded!")
            login_menu(tmp[0])
            
           
    else:
            print("Login Failed!")
            get_user()





def login_menu(x):
    user_id=x
    print("--------------- Log-In --------------------")
    choice = int(input("""
        1- Create new project
        2- View all projects
        3- Edit project
        4- Delete project
        5- Search for a project
        6- Exit
        """))

    if choice == 1:
        create.create_project(user_id)
        
    elif choice == 2:
        view.view_project(user_id)
    elif choice == 3:
        update.Update(user_id)
    elif choice == 4:
        delete.Delete(user_id)
    elif choice == 6:
        exit()



