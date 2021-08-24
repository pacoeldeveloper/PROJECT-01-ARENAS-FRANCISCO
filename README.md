# *Lifestore* Study case coding solution

## Run
python3 -m sales_analysis_system

## About the case
Recently, the virtual store *Lifestore* has noticed an inventory accumulation problem. In addition, it reported a decrement in the sales of the last trimester directly related to a search history diminishment of certain products.

## What was needed to be done?
To improve this situation, they asked us to develop a new strategy for product retirement in order to prevent another inventory accumulation problem.  This solution must satisfy 3 focal points:

1. Bestseller products and flopped products from a previous analysis of those categories with lower sales and least searches 
2. Reviews of products from a previous analysis of those categories with higher sales and more searches 
3. Product retirement based on the income data as well as on monthly sales.

## Case requirements
In order to fulfill the necessities of the fictional coorporation, the coding solution must meet the following requirements:

- Login-system → This login system must authenticate and register two different types of users: Normal user / Admin user. There was not any specification regarding the storage method for this information. Thus, a text file with the format: `#, user-type, username, password` will be used.
- Admin user → This user must be able to see:
    - A monthly report of the bestselling products (in specific, he/she must be able to see the 50 best selling products in a list format).
    - A monthly report of the most searched products (in specific, he/she must be able to see the 100 products with most searches in a list format).
    - A report based on category of the 50 products with lower sales and other with the 100 least searched products.
    - Two lists containing the 20 best reviewed and worst reviewed products, respectively. This evaluation is made using the devolution criteria.
    - Total income earnings alongside an estimated average of monthly sales. In addition, this sales analysis must include the total anual sales as well as the months with more sales of the year.
- Normal user → The behavior of the system for this user is not specified in the official organization documentation. Nevertheless, it is proposed to let this user search for a specific product or search products of a specific category.

## Contributing
Any Pull requests to the repository are welcome. For major changes, please open an issue first in order to discuss your changes. 

## License
[MIT](https://choosealicense.com/licenses/mit/)

