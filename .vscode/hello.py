import sys 
import math

###############################################################################
"""
print("degrees(1.5708) = ", math.degrees(1.5708))

print("log(1000, 10)=", math.log(1000, 10))
"""
################################################################################

"""def tip_amount(tip_percentage, total):
    return total * tip_percentage


def buy_produce(num_of_tomatoes, num_of_bananas, num_of_potatoes):
    total_price = num_of_tomatoes * 2.00 + num_of_bananas * 1.50 + num_of_potatoes * 3.00
    print("Welcome to Dev Branch Groceries")
    print("Today you bought: ")
    print(str(num_of_tomatoes) + "tomatoes")
    print(str(num_of_bananas) + "bananas")
    print(str(num_of_potatoes) + "potatoes")
    print("Your total is: $" + str(total_price))
    tips = tip_amount(0.15, total_price)
    print("Please tip me $" + str(tips))
    tips_more = tip_amount(0.5, total_price)
    print("If you're feeling rich, give me $" + str(tips_more))"""

################################################################################
""""
drink = input("Pick One (Coke or Pepsi) : ")
if drink == "Coke":
    print("Here is your Coke")
elif drink == "Pepsi":
    print("Here is your Pepsi")
else:
    print("Here is your Water")
"""
################################################################################
"""
num_1, operator, num_2 = input("Enter Calculation: ").split()
num_1 = int(num_1)
num_2 = int(num_2)

if operator == "+":
    print("{} + {} = {}".format(num_1, num_2, num_1 + num_2))
"""
################################################################################   
"""
age = int(input("Enter Age : "))  
if age < 5:
    print("Too Young for School")
elif age == 5:
    print("Go to Kindergarten")
elif (age >= 6) and (age <= 17):
    grade = age - 5
    print("Go to Grade {}".format(grade))
else: 
    print("Go to College")
"""
###############################################################################

# Ternary Operator
# condition_true if condition else condition_false 
"""
age = int(input("What is your age? "))
can_vote = True if age >= 18 else False
print("You can vote :", can_vote)
"""
###############################################################################

# For and Range

for i in [2, 4, 6, 8, 10]:
    print("i =", i)

for i in range(2, 5):
    print("i=", i)

i = 6
print("Is 6 Even :", ((i % 2) == 0))

# Print out all of the odd values in the range 

for i in range(1, 21): 
    if (i % 2) != 0:
        print("i =", i)

# This program will: 

# 1. Have the user enter their investment amount and expected interest

# 2. Each year their investment will increase by their investment + their investment * the interest rate

# 3. Print out their earnings after a 10 year period

money = input("How much to invest :")
interest_rate = input("interest Rate : ")

money = float(money)
interest_rate = float(interest_rate) * .01

for i in range(10):
    money = money + (money * interest_rate)
print("Investment after 10 years : ${:.2f}".format(money))

