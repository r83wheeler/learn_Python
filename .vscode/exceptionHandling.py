
'''
while True: 
    try:
        number = int(input("Please enter a number : "))
        break

    except ValueError:
        print("You didn't enter a number")
    except:
        print("An unknown error occurred")

print("Thank you for entering a number")
'''
###################################################################

secret_number = 7
while True:
    guess = int(input("Guess a number between 1 and 10 :"))
    if guess == secret_number:
        print("You guessed it")
        break

    
