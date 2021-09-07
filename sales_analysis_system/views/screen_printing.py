'''
Author: Francisco Arenas
Creation Date: August 25th, 2021
Last Modfication Date: September 7th, 2021

File with all art printing-related operations.
'''

def print_main_menu() -> None:
    print("""
 _________________________________________
/ Welcome to the Lifestore sales analysis \\
| system. Please, select an option to     |
| begin:                                  |
|                                         |
| 1. Login with your user/admin account   |
| 2. Create a new account                 |
\ 0. Exit                                 /
 ----------------------------------------
   \\
    \\
        .--.
       |o_o |
       |:_/ |
      //   \ \\
     (|     | )
    /'\_   _/`\\
    \___)=(___/ 
    """)

def print_admin_menu(username: str) -> None:
      print(f"""
      Welcome {username} 
 _________________________________________
/ Please, select an option to begin:      \\
| begin:                                  |
|                                         |
| 1. See searches/sales analysis          |
| 2. See reviews analysis                 |
| 3. See income analysis                  |
\ -1. Exit                                /
 ----------------------------------------
   \\
    \\
        .--.
       |o_o |
       |:_/ |
      //   \ \\
     (|     | )
    /'\_   _/`\\
    \___)=(___/ 
    """)

def print_user_menu(username: str) -> None:
      print(f"""
      Welcome {username} 
 _________________________________________
/ Please, select an option to begin:      \\
| begin:                                  |
|                                         |
| 1. Search a specific product            |
| 2. See all products from a specific     |
|    category                             |
| 3. See all products                     |
\ -1. Exit                                /
 ----------------------------------------
   \\
    \\
        .--.
       |o_o |
       |:_/ |
      //   \ \\
     (|     | )
    /'\_   _/`\\
    \___)=(___/ 
    """)

def print_goodbye() -> None:
  print("""
   ____                 _ _                
  / ___| ___   ___   __| | |__  _   _  ___ 
 | |  _ / _ \ / _ \ / _` | '_ \| | | |/ _ \\
 | |_| | (_) | (_) | (_| | |_) | |_| |  __/
  \____|\___/ \___/ \__,_|_.__/ \__, |\___|
                                |___/      
  """)