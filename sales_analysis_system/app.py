'''
Author: Francisco Arenas
Creation Date: August 24th, 2021
Last Modfication Date: August 2th, 2021

Main file for the Lifestore case study. For more information, 
consult the README.md file in my github account: @farenasencis
'''

from sales_analysis_system.data.account_processes import *
from sales_analysis_system.views.screen_printing import *
from sales_analysis_system.data.lifestore_file import *

def admin_screen(username: str):
    print("admin")

def normal_user_screen(username: str):
    print("normal")

def main_screen() -> None:
    print_main_menu()
    selected_option = int(input("Answer [0, 1, 2]: "))

    while selected_option != 0:
        
        if selected_option == 1:
            typed_username = (input("Type your username: "))
            typed_password = (input("Type your password: "))
            is_valid_account = verify_login(typed_username, typed_password)

            if is_valid_account != 2 and is_valid_account != 3:         # 2 = did want; 3 = did not want to create account
                next_screen = {
                    0 : normal_user_screen(typed_username),
                    1 : admin_screen(typed_username)
                }
                next_screen.get(is_valid_account)
                break
            elif is_valid_account == 2:
                verify_account_creation(create_account())
                selected_option = int(input(""))
            else: 
                break

        elif selected_option == 2:
            verify_account_creation(create_account())
            selected_option = int(input(""))
        
        else: 
            print("You typed an invalid option!")
            selected_option = int(input("Select [0, 1, 2]: "))

def run():
    main_screen()
    #print_goodbye()
    
