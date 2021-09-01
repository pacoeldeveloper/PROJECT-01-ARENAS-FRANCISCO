'''
Author: Francisco Arenas
Creation Date: August 25th, 2021
Last Modfication Date: August 25th, 2021

File with all account-related operations.
'''

import pkg_resources
import os

PATH = pkg_resources.resource_filename(__name__, 
    os.path.join(os.pardir, 'resources', 'login_information.txt'))

def get_user_data() -> list:
    with open(PATH, 'r') as file:
        users_data = [line.replace('\n', '').split(', ', 4)[1:4] for line in file]
        usernames = [data_list[0] for data_list in users_data]
    return users_data, usernames

def create_account() -> bool:    
    try:
        _, registered_usernames = get_user_data()
        default_usertype = 0    # 0 = No admin user; 1 = Admin user
        new_user_id = len(registered_usernames) + 1
        new_username = input("You're about to create you new account. Type your username: ")

        while new_username in registered_usernames:
            new_username = input("Sorry, that username is already in use. Type another one:  ")
        
        new_password = input("Type your password: ")
        entered_type = input("Are you an admin user? [Y/N]: ")

        if entered_type.lower() == 'y':
            default_usertype = 1
            
        with open(PATH, 'a') as file:
            file.writelines(
                str(new_user_id) + ', ' + new_username + ', ' +
                new_password + ', ' + str(default_usertype) + ', ' + '\n'
            )
            return True

    except (FileNotFoundError, KeyboardInterrupt):
        print("\nError while creating your account, try again later.")
        return False

def verify_login(given_username: str, given_password: str) -> int:
    registered_users, registered_usernames = get_user_data()
    valid_tries = 0
    
    if given_username not in registered_usernames:
        return no_account_found()
    else:
        index = registered_usernames.index(given_username)
        registered_password = registered_users[index][1] 
        
        while valid_tries < 6 and given_password != registered_password:  
            given_password = input("You introduced a wrong password. Try again: ")
            valid_tries += 1
    
        if given_password != registered_password:
            return no_account_found()
        else:
            return int(registered_users[index][2])
                
def no_account_found() -> int:
    what_to_do = input("Sorry, it seems like you do not have an account. Want to create one? [Y/N] ")      
    print(what_to_do.lower())
    if what_to_do.lower() == 'y':
        return 2
    else: 
        return 3

def verify_account_creation(is_created: bool) -> None:
    if is_created:
        print("To continue, type 1 or exit with 0: ")
    else:
        print("To use the system create an account. Type 2 to do so or exit with 0:")