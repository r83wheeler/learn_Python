

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