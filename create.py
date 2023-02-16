import os  
import re
import login
def create_project(id): 
    # print(f'email is {x}')
    os.system("clear")
    print('create')
    projectTitle = input("Enter Project Ttile ")
    while projectTitle == "" or projectTitle.isdigit() == True:
        projectTitle = input("Please Enter Ttile of project Again:")   
###########################project details###################################
    projectDetails = input("Enter Project Detail ")
    while projectDetails == "" or projectDetails.isdigit() == True or len(projectDetails) < 10:
        projectDetails = input("please Enter Detail of Project Agian: ")
#############################total target#################################
    TotalTarget = input("Enter Project TotalTarget  :) ")
    while TotalTarget == "" or TotalTarget.isalpha()==True :
        TotalTarget = input("please Enter TotalTarget Agian:) ")
##############################startdate of project################################
    StartDate = input("Enter Start Date in this format => (d/m/yyyy): ")
    while StartDate == "" or not re.match(r"([0-2]\d|3[01])/(0\d|1[0-2])/([12]\d{3})", StartDate):
        StartDate = input("Enter Start Date in this format => (d/m/yyyy) ")
##############################EndDate of project####################################
    EndDate = input("Enter End Date in this format =>(d/m/yyyy): ")
    while EndDate == "" or not re.match(r"([0-2]\d|3[01])/(0\d|1[0-2])/([12]\d{3})", EndDate):
        EndDate = input("Enter End Date in this format (d/m/yyyy) ")
##############################file Create and write#####################################
#   i want list here 
    os.system("touch project_file.txt") 
    f = open("project_file.txt" , "a")
    f.write(f'{id}:{projectTitle}:{projectDetails}:{TotalTarget}:{StartDate}:{EndDate}\n')
    f.close()
    os.system("clear")
    print("---------------------- Success adding project ------------------------ ")
    

    print (" Press '1' create again?")
    print (" Press '2' go back to main menu")
    choice = input()
    if choice == "1":
        create_project(id)
    elif choice == "2":
        os.system("clear")
        login.login_menu(id)