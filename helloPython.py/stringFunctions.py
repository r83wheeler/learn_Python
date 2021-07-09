
# How to delete whitespace

rand_string = "          this is an important string        "

rand_string = rand_string.lstrip()
rand_string = rand_string.rstrip()

# You can also use .strip() to get rid of both left and right whitespaces

print(rand_string)

print(rand_string.capitalize())
print(rand_string.lower())

a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

a_list_2 = rand_string.split()

for i in a_list_2:
    print(i)
