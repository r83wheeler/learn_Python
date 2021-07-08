""""
samp_string = "This is a very important string"

print("Length :", len(samp_string))

print(samp_string[0])
print(samp_string[-1])
print(samp_string[0:4])
print(samp_string[8:])
print("Every Other", samp_string[0:-1:2])
print("Reverse", samp_string[::-1])

print("Green" + "Eggs")
print("Hello " * 5)
num_string = str(4)

for char in samp_string:
    print(char)

for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])
"""

# unicode a - z 97 -122, A - Z 65 - 90

print("A =", ord("A"))
print("65 =", chr(65))

norm_string = input("Enter a string to hide in uppercase : ")
secret_string = ""
for char in norm_string:
    secret_string += str(ord(char) - 23)
print("Secret Message :", secret_string)
norm_string = ""
for i in range(0, len(secret_string)-1,2):
    char_code = secret_string[i] + secret_string[i+1]
    norm_string += chr(int(char_code) + 23)
print("Original Message :", norm_string)