import create
import update
import delete
import view
def login_menu():
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
        createProject.create_project(user_mail)
    elif choice == 2:
        viewProjects.view_all_projects()
    elif choice == 3:
        editProject.edit_project(user_mail)
    elif choice == 4:
        deleteProject.delete_project(user_mail)
    elif choice == 6:
        exit()
