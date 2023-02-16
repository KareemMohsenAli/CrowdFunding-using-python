import os 
import login
# def view_project(id):
#     print('------------- viewing all project data ------------------')
#     os.system('cat project_file.txt')




def view_project(id):
    f = open("project_file.txt", 'r')
    lines = f.readlines()
    f.close()

    print("-------------- User Projects ----------------")
    counter = 1
    for line in lines:
        line = line.split(":")
        if line[0] == id:
            print(f"Project :  {counter}")
            print(f"Project Title: {line[1]}")
            print(f"Project Description: {line[2]}")
            print(f"Total Target: {line[3]}")
            print(f"Start Date: {line[4]}")
            print(f"End Date: {line[5]}")
            print("____________________________________________________________")
            counter += 1

          
    print (" Press '1' to go back to main menue")
    print (" Press '2' to exit from application!!")
    choice = input()
    if choice == "1":
        os.system("clear")
        login.login_menu(id)
    elif choice == "2":
        exit()


