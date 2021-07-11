
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
print("How many is :", rand_string.count("is"))
print("Where is :", rand_string.find("string"))
print("Where is :", rand_string.replace(" an", " a kind of "))

a_list_2 = rand_string.split()

for i in a_list_2:
    print(i)

orig_string = input("Convert to Acronym : ")
orig_string = orig_string.upper()
list_of_words = orig_string.split()
for word in list_of_words:
    print(word[0], end="")
print()

letter_z = "z"
print("Is z a letter or number :", letter_z.isalnum())
print("Is z a letter :", letter_z.isalpha())
print("Is z a letter :", letter_z.isdigit())
print("Is z a letter :", letter_z.islower())
print("Is z a letter :", letter_z.isupper())
print("Is z a letter :", letter_z.isspace())
