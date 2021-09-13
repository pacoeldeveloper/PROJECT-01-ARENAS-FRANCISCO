'''
Author: Francisco Arenas
Creation Date: September 7th, 2021
Last Modfication Date: September 7th, 2021

File with all the needed functions to show the user the 
requested information.
'''

from sales_analysis_system.data.lifestore_file import *

def show_specified_product(given_product: str) -> None:
    product_names =  list(((str(product[1])).split(", ")[0] for product in lifestore_products))

    if given_product not in product_names:
        print("Sorry, the product you are looking for is not available right now")
    else: 
        product_ID = product_names.index(given_product)
        print(f"""
        Product: {(str(lifestore_products[product_ID][1])).split(", ")[0]}
        Price: ${lifestore_products[product_ID][2]}
        Category: {lifestore_products[product_ID][3]}
        Current stock: {lifestore_products[product_ID][4]}
        """)

def show_category_products(category: str) -> None: 
    product_count = 1
    for product in lifestore_products:
        
        if lifestore_products[(product[0] - 1)][3] == category:    
            print("--------------------------------------------------------------------")
            print(f"""{product_count}
            Product: {(str(lifestore_products[(product[0] - 1)][1])).split(", ")[0]}
            Price: ${lifestore_products[(product[0] - 1)][2]}
            Current stock: {lifestore_products[(product[0] - 1)][4]}
            """)

            product_count += 1

def show_products() -> None:
    product_count = 1
    for product in lifestore_products:
        if product_count > 1 and product_count < (len(lifestore_products) + 1): 
            print("-----------------------------------------------------------------------")

        print(f"""{product_count}
        Product: {(str(lifestore_products[(product[0] - 1)][1])).split(", ")[0]}
        Price: ${lifestore_products[(product[0] - 1)][2]}
        Category: {lifestore_products[(product[0] - 1)][3]}
        Current stock: {lifestore_products[(product[0] - 1)][4]}""")
        
        product_count += 1