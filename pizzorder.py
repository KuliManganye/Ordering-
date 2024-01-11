# This code is to create a program that adds up the bill for ordering pizza according to the specifications the user inputs


print("Welcome to Python Pizza Deliveries")

"""PIZZA PRICES
Small Pizza = $15
Medium Pizza = $20
large Pizza = $25

TOPPINGS
Pepperoni for small pizza = $2
Pepperoni for medium and large pizaa = $3

Extra cheese for any size pizza = $1
"""

size = input("What size pizza do you want? S, M or L \n")
add_pepperoni = input("Do you want Pepperoni? Y or N \n")
add_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2

elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3

elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3

if add_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")
