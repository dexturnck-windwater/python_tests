
import turtle




# =========================
# Question 7 — Car Dealership System
# =========================

"""
A car dealership stores car information
inside a list of dictionaries.

Tasks:
1. Use a loop to check every car inside cars_list

2. If the car type and country match
   the user's input:
   - print the brand
   - print the color
   - print the price
   - print the stock
   - print the amount sold
"""

cars_list = [
    {
        "id": 1,
        "brand": "Toyota",
        "color": "Red",
        "price": 30000,
        "type": "oil",
        "country": "Japan",
        "stock": 5,
        "sold": 2
    },
    {
        "id": 2,
        "brand": "Tesla",
        "color": "Black",
        "price": 50000,
        "type": "electric",
        "country": "USA",
        "stock": 3,
        "sold": 1
    },
    {
        "id": 3,
        "brand": "Hyundai",
        "color": "White",
        "price": 28000,
        "type": "oil",
        "country": "Korea",
        "stock": 7,
        "sold": 4
    }
]

user_type = input("Enter car type: ")
user_country = input("Enter country: ")

for x in range(0,3):
    if user_type==cars_list[x]["type"] and user_country==cars_list[x]["country"]:
        print(cars_list[x]["brand"])
        print(cars_list[x]["color"])
        print(cars_list[x]["price"])
        print(cars_list[x]["stock"])
        print(cars_list[x]["sold"])


# write your code here


"""
Example 1

Input:
oil
Japan

Output:
Brand: Toyota
Color: Red
Price: 30000
Stock: 5
Sold: 2
"""


"""
Example 2

Input:
electric
USA

Output:
Brand: Tesla
Color: Black
Price: 50000
Stock: 3
Sold: 1
"""


"""
Theory Questions

1. Why is a list used instead of one dictionary only?
    it is a dictionary

2. What is the difference between:

cars_list[0]

and

cars_list[0]["brand"]
# cars_list[0] prints dictionary
# cars_list[0]["brand"] prints out the variable in the dictionary

3. Why is a loop useful in this program?
    #to print the dictionary
4. What will happen if this code is used?

print(cars_list["brand"])
    #it will print waht is the brand
Explain your answer.
"""