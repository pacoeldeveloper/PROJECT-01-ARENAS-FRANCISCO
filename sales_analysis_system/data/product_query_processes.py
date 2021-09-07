'''
Author: Francisco Arenas
Creation Date: September 7th, 2021
Last Modfication Date: September 7th, 2021

File with all the needed functions to show the user the 
requested information.
'''

from sales_analysis_system.data.lifestore_file import *

def show_specified_product(given_product: str) -> None:
    product_names =  list((product[1] for product in lifestore_products))

    if given_product not in product_names:
        print("Sorry, the product you are looking for is not available right now")
    else: 
        product_ID = product_names.index(given_product)
        print(f"""
        Product: {lifestore_products[product_ID][1]},
        Price: {lifestore_products[product_ID][2]},
        Category: {lifestore_products[product_ID][3]},
        Current stock: {lifestore_products[product_ID][4]}
        """)

def show_category_products(category: str) -> None: 
    for product in lifestore_products:
        if lifestore_products[(product[0] - 1)][3] == category:    
            print(f"""
            Product: {lifestore_products[(product[0] - 1)][1]},
            Price: {lifestore_products[(product[0] - 1)][2]},
            Category: {lifestore_products[(product[0] - 1)][3]},
            Current stock: {lifestore_products[(product[0] - 1)][4]}
            """)

def show_products() -> None:
    print_products(lifestore_products)

def print_products(given_list) -> None:
    for product in given_list:
        print(f"""
        Product: {lifestore_products[(product[0] - 1)][1]},
        Price: {lifestore_products[(product[0] - 1)][2]},
        Category: {lifestore_products[(product[0] - 1)][3]},
        Current stock: {lifestore_products[(product[0] - 1)][4]}
        """)