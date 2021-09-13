'''
Author: Francisco Arenas
Creation Date: August 24th, 2021
Last Modfication Date: September 7th, 2021

Main file for the Lifestore case study. For more information, 
consult the README.md file in my github account: @farenasencis
'''

from sales_analysis_system.data.product_analysis_processes import show_income, show_reviews_analysis, show_sales_searches_analysis
from sales_analysis_system.data.product_query_processes import show_specified_product, show_category_products, show_products
from sales_analysis_system.data.account_processes import *
from sales_analysis_system.views.screen_printing import *
from sales_analysis_system.data.lifestore_file import *

def admin_screen(username: str):
    print_admin_menu(username)
    selected_option = int(input("Answer [-1, 1, 2, 3]: "))

    while selected_option > 0:
        
        if selected_option == 1:
            show_sales_searches_analysis()
            selected_option = int(input("\nSelect [-1, 1, 2, 3]: "))

        elif selected_option == 2:
            show_reviews_analysis()
            selected_option = int(input("\nSelect [-1, 1, 2, 3]: "))
        
        elif selected_option == 3:
            show_income()
            selected_option = int(input("\nSelect [-1, 1, 2, 3]: "))
        
        else: 
            print("You typed an invalid option!")
            selected_option = int(input("\nSelect [-1, 1, 2, 3]: "))


def normal_user_screen(username: str):
    print_user_menu(username)
    selected_option = int(input("Answer [-1, 1, 2, 3]: "))

    while selected_option > 0:
        
        if selected_option == 1:
            product_name = input("Write the product's name (use until the ',' from the lifestore_products list): ")
            show_specified_product(product_name)
            selected_option = int(input("\nSelect [-1, 1, 2, 3]: "))

        elif selected_option == 2:
            category = input("Write the category you would like to see: ")
            show_category_products(category)
            selected_option = int(input("\nSelect [-1, 1, 2, 3]: "))
        
        elif selected_option == 3:
            show_products()
            selected_option = int(input("\nSelect [-1, 1, 2, 3]: "))
        
        else: 
            print("You typed an invalid option!")
            selected_option = int(input("\nSelect [-1, 1, 2, 3]: "))

def main_screen() -> None:
    print_main_menu()
    selected_option = int(input("Answer [0, 1, 2]: "))

    while selected_option != 0:
        
        if selected_option == 1:
            typed_username = (input("Type your username: "))
            typed_password = (input("Type your password: "))
            is_valid_account = verify_login(typed_username, typed_password)

            if is_valid_account != 2 and is_valid_account != 3:         # 2 = did want; 3 = did not want to create account
                if is_valid_account == 0:
                    normal_user_screen(typed_username),
                else:
                    admin_screen(typed_username)
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
    print_goodbye()