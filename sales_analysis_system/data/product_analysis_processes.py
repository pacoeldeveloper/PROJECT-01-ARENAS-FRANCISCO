'''
Author: Francisco Arenas
Creation Date: August 30th, 2021
Last Modfication Date: September 1st, 2021

File with all the needed functions to obtain the required
analysis.
'''

from datetime import datetime
from sales_analysis_system.data.lifestore_file import *
from typing import List
import calendar

def show_sales_searches_analysis() -> None:
    _, worst_sold_products, best_sold_products = get_top_worst_products(1, lifestore_sales)
    _, least_searched_products, most_searched_products = get_top_worst_products(1, lifestore_searches)
    print("Best sold products (NOTE! The list was clean to present the most relevant data):")
    print_products(get_cleaner_lists(best_sold_products), "Times it was bought")
    print("Worst sold products:")
    print_products(worst_sold_products, "Times it was bought")
    print("Most searched products:")
    print_products(most_searched_products, "Times it was searched")
    print("Least searched products:")
    print_products(least_searched_products, "Times it was searched")

def show_reviews_analysis() -> None:
    best_reviewed_products, worst_reviewed_products = get_top_worst_reviews()
    _, _, worst_sold_products = get_top_worst_products(1, lifestore_sales)
    worst_sold_products_id = sorted(list((product[0] for product in worst_sold_products)))
    
    print("Best reviewed products:")
    print_products(best_reviewed_products, "Times it was refunded")
    print("Worst reviewed products:")
    print_products(worst_reviewed_products, "Times it was refunded")

    # Clean the the reviews to obtain the elements with most info
    cleaner_worst = get_cleaner_lists(worst_reviewed_products)

    print('Nonetheless, the only products that were refunded are:')
    print_products(cleaner_worst, "Times it was refunded")
    print('From this list, the following products were within the worst sold products list:')
    print_products(get_worst_reviwed_in_worst_sold_products(cleaner_worst, 
                                                            worst_sold_products_id), "Times it was refunded")
 
def show_income() -> None:
    average, worst_months, best_months = get_monthly_sales()
    print(f'The total income aquired is: ${get_total_income()}')
    print(f'With the current sales data, the company is making, in average, approximately {average} sales per month ')
    print('Each year, the company had the following total number of sales:')
    print_time(get_anual_income(), 'Year', 'Sales within that year')
    print('Furthermore, historically, we have that the months with the best sales are:')
    print_time(dict(best_months), 'Month', 'Sales within that month')
    print('While the months with the worst sales are:')
    print_time(dict(worst_months), 'Month', 'Sales within that month')
    
def get_top_worst_products(product_attribute_index, list_to_search) -> List:
    product_list = dict.fromkeys((product[0] for product in lifestore_products), 0)
    
    for attribute in list_to_search:
        product_id = attribute[product_attribute_index]
        product_list[product_id] += 1

    # dictionary is now a tuple-formed list by sorting its values
    product_list = sorted(product_list.items(), key=lambda x:x[1], reverse=True)
    worst_elements = product_list[(len(product_list) // 2):]
    top_elements = product_list[:(len(product_list) // 2)]

    return product_list, worst_elements, top_elements

def get_top_worst_reviews() -> List:
    refunded_products = dict.fromkeys((product[0] for product in lifestore_products), 0)
    for sale in lifestore_sales:
        # we take for granted that index 4 and 1 are refund and product id respectively
        if(sale[4] == 1):
            refunded_products[sale[1]] += 1
    
    refunded_products = sorted(refunded_products.items(), key=lambda x:x[1], reverse=True)

    # The following lists contain our top 20 best/worst reviews
    best_reviewed_products = refunded_products[(len(refunded_products) - 20):]
    worst_reviewed_products = refunded_products[:20]

    return best_reviewed_products, worst_reviewed_products

def get_cleaner_lists(given__list) -> List:
    cleaner_list = []
    for element in given__list:
        if element[1] >= 1:
            cleaner_list.append(element)
    
    return cleaner_list

def get_worst_reviwed_in_worst_sold_products(refunded_products, products_id) -> List:
    worst_worst_products = []
    for product in refunded_products:
        if product[0] in products_id:
            worst_worst_products.append(product)
    
    return worst_worst_products

def get_total_income() -> int:
    products_sold, _, _ = get_top_worst_products(1, lifestore_sales)
    total_income = 0
    for product in products_sold:
        # index 0 and 1 in product is the product ID and the times it was sold, respectively
        total_income += (product[1] * lifestore_products[(product[0]) - 1][2])
    
    return total_income

def get_monthly_sales(): 
    sales_per_month = get_sales_per_month()

    average_sales_per_month = 0
    for month in sales_per_month:
        average_sales_per_month += sales_per_month[month]
    
    average_sales_per_month //= len(sales_per_month)
    
    best_months_in_sales = []
    worst_months_in_sales = []

    for month in sales_per_month:
        if sales_per_month[month] < average_sales_per_month:
            worst_months_in_sales.append((calendar.month_name[month], sales_per_month[month]))
        else:
            best_months_in_sales.append((calendar.month_name[month], sales_per_month[month]))

    return average_sales_per_month, worst_months_in_sales, best_months_in_sales
    
def get_sales_per_month() -> List:
    dates_in_string = list((date[3] for date in lifestore_sales))
    formatted_dates = []
    for date in dates_in_string:
        formatted_dates.append((datetime.strptime(date, '%d/%m/%Y')).month)

    sales_per_month = dict.fromkeys(sorted(formatted_dates), 0)
    for product in lifestore_sales:
        month_it_was_bought = (datetime.strptime(product[3], '%d/%m/%Y')).month
        sales_per_month[month_it_was_bought] += 1

    return sales_per_month

def get_anual_income() -> List:
    dates_in_string = list((date[3] for date in lifestore_sales))
    formatted_dates = []
    for date in dates_in_string:
        formatted_dates.append((datetime.strptime(date, '%d/%m/%Y')).year)
    
    sales_per_year = dict.fromkeys(sorted(formatted_dates), 0)
    for product in lifestore_sales:
        year_it_was_bought = (datetime.strptime(product[3], '%d/%m/%Y')).year
        sales_per_year[year_it_was_bought] += 1

    return sales_per_year

def print_products(given_list, analyzed_attribute) -> None:
    for product in given_list:
        print(f"""
        Product: {lifestore_products[(product[0] - 1)][1]},
        Price: {lifestore_products[(product[0] - 1)][2]},
        Category: {lifestore_products[(product[0] - 1)][3]},
        Current stock: {lifestore_products[(product[0] - 1)][4]},
        {analyzed_attribute}: {product[1]}
        """)

def print_time(given_dict, time_attribute, sale_attribute) -> None:
    for date, sales in given_dict.items():
        print(f'''
        {time_attribute}: {date},
        {sale_attribute}: {sales}
        ''')