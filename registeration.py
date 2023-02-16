import os
import re
import time
# import mainmenue
def register():
    os.system("clear")
    print("Welcome to the Registration System")

    firstName=input("enter your First Name ")
    while firstName=='' or firstName.isdigit()==True or len(firstName)<5:
            firstName=input("Please enter a valid first name: ")

############################################################################################
    lastName=input("Last Name ")
    while lastName=='' or lastName.isdigit()==True or len(lastName)<5:
            lastName=input("Please enter a valid last name:")
#############################################################################################
    email=input("Email ")
    while email == '' or not re.match(r'[^@]+@[^@]+\.[^@]+', email):
       email= input('Please enter a valid email: ')
#############################################################################################        
    password=input("Password ")
    while password=='' or len(password)<8:
        password=input("Please enter a valid password: ")
##############################################################################################
    confirmPassword=input("Confirm Password: ")
    while confirmPassword=='' or password!=confirmPassword:
        confirmPassword=input("Passwords do not match: ")
##############################################################################################
    mobilephone=input("enter phone number: ")
    while mobilephone=='' or mobilephone.isalpha()==True or not re.match(r'^01[0125][0-9]{8}$', mobilephone):
            mobilephone=input("Please enter a valid phone number: ")
###############################################################################################
    id =round(time.time()) 
    os.system("touch userFile.txt") 
    f = open("userFile.txt" , "a")
    f.write(f'{id}:{firstName}:{lastName}:{email}:{password}:{mobilephone}\n')
    f.close()
    print("Success adding.. ")
# mainmenue.main_menu()
# register()
        



