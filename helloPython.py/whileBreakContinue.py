import random

rand_num = random.randrange(1, 51)
i = 1
while i != rand_num:
    i += 1
print("The random value is : ", rand_num)

#######################################################

i = 1 
while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue
    if i == 15:
        break
    print("Odd :", i)
    i += 1

#######################################################

tree_height = input("How tall is the tree : ")
tree_height = int(tree_height)
spaces = tree_height -1
hashes = 1 
stump_spaces = tree_height -1
while tree_height != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")
    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1
for i in range(stump_spaces):
    print(" ", end="")
print("#")