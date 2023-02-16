# from registeration import register
# from login import loginfun
import registeration
import login
def main_menu():
     while True:
        print("-------- Main Menu ----------")
        choice = int(input("""
        1: Register
        2- LogIn
        3- Exit
        """))
        if choice == 1:
            registeration.register()
        
        elif choice == 2:
            login.get_user()
            

        elif choice == 3:
            exit()
        else:
            print("Invalid choice")
print("######## CROWD FUNDING ############")

main_menu()

