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

###########################################################################################

# 1. exponentiation and root extraction
# 2. multiplication and division
# 3. addition and subtraction

print("2 + (3 * 4) = ", (2 + (3 * 4)))
print("(2 + 3) * 4 = ", ((2 + 3) * 4))
print("2 + 3 * 4 = ", (2 + 3 * 4))

