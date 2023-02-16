# def Update():
#     print('update')
import login
import os
import re
def Update(user_id):
    print("--------------- Edit Project --------------------")

    ###################Validation####################

    ###################Project_title####################
    def validate_project_title(userInput):
        projectTitle = userInput
        while projectTitle == "" or projectTitle.isdigit() == True:
            projectTitle = input("Please Enter correct New Ttile of project Again: ")
        return projectTitle
    ###################Project_title#################### 
    ###################Details##########################
    def validate_details(userInput):
        projectDetails = userInput
        while projectDetails == "" or projectDetails.isdigit() == True or len(projectDetails) < 10:
            projectDetails = input("please Enter correct Detail of Project Agian: ")
        return projectDetails
    ###################Details##########################
    ###################Total_Target####################
    def validate_total_target(userInput):
        TotalTarget = userInput
        while TotalTarget == "" or TotalTarget.isalpha()==True :
            TotalTarget = input("please Enter correct TotalTarget of project Agian: ")
        return TotalTarget
    ###################Total_Target####################
    ###################Start_Time####################
    def validate_start_time(userInput):
        StartDate = userInput
        while StartDate == "" or not re.match(r"([0-2]\d|3[01])/(0\d|1[0-2])/([12]\d{3})", StartDate):
            StartDate = input("please Enter Start Date Again  in this format => (d/m/yyyy): ")
        return StartDate
    ###################Start_Time####################
    ###################End_Time#####################
    def validate_end_time(userInput):
        EndDate = userInput
        while EndDate == "" or not re.match(r"([0-2]\d|3[01])/(0\d|1[0-2])/([12]\d{3})", EndDate):
            EndDate = input("please Enter End Date agian in this format => (d/m/yyyy):  ")
        return EndDate
    ###################End_Time#####################

    ###################Validation####################     

    ####################start from here#############################
    project_title = input("Project Title: ")
    project = {"User": user_id,
                "Title": validate_project_title(input("Enter New Ttile of project: ")),
               "Details": validate_details(input("Enter New Project Details: ")),
               "Total_Target": validate_total_target(input("Enter New Total Target: ")),
               "Start_Time": validate_start_time(input("Enter New Start Time (dd/mm/yy): ")),
               "End_Time":validate_end_time(input("Enter New End Time (dd/mm/yy): "))
               }

    f = open("project_file.txt", 'r')
    lines = f.readlines()
    f.close()

    new_lines = []
    for line in lines:
        line = line.split(":")
        if line[1] == project_title and line[0] == user_id:
            line[1] = project["Title"]
            line[2] = project["Details"]
            line[3] = project["Total_Target"]
            line[4] = project["Start_Time"]
            line[5] = project["End_Time"]+'\n'
            line = ":".join(line)
            new_lines.append(line)
        else:
            line = ":".join(line)
            new_lines.append(line)

    f = open("project_file.txt", 'w')
    f.writelines(new_lines)
    f.close()
    print("Project Saved!")

    print (" Press '1' update again?")
    print (" Press '2' go back to main menu")
    choice = input()
    if choice == "1":
        Update(user_id)
    elif choice == "2":
        os.system("clear")
        login.login_menu(user_id )


    