import login
import os
def Delete(id):
    print('_____________________Delete Project___________________')
    delete_input=input('Enter the name of you want to delete it ')
    file=open("project_file.txt",'r')
    lines=file.readlines()
    file.close()
    data=[]
    for line in lines:
        line=line.split(':')
        if not(line[1]==delete_input and line[0]==id):
            line=':'.join(line)
            data.append(line)
        else:
            print('project is deleted ')
 
    
    file=open("project_file.txt",'w')
    file.writelines(data)
    file.close()

    print (" Press '1' to Delete userAgian??")
    print (" Press '2' to go back to main menu")
    choice = input()
    if choice == "1":
        Delete(id)
    elif choice == "2":
        os.system("clear")
        login.login_menu(id)

