def add_numbers(num_1, num_2):
    return num_1 + num_2

print("5 + 4 =", add_numbers(5, 4))

###################################################

def change_name(name):
    name = "Mark"

name = "Tom"
change_name(name)
print(name)

###################################################

def change_name():
    return "Mark"

name = "Tom"
name = change_name()
print(name)

###################################################

def change_name():
    global gbl_name
    gbl_name = "Sammy"

gbl_name = "Sally"
change_name()
print(gbl_name)


