from random import randint

print("This is an interactive guessing game!You have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")

def fun(r):
    i = 0
    while (True):
        print("What's your guess between 1 and 99?")
        a = input(">> ")
        try:
            if int(a) not in range(1, 100):
                print("The value is out of range!")
            elif int(a) > r:
                print("Too high!")
            elif int(a) < r:
                print("Too low!")
            elif int(a) == r:
                print("Congratulations, you've got it!")
                print("You won in {} attempts!".format(i))
                r = randint(1, 100)
                i = 0
        except:
            if (a == "exit"):
                print("Goodbye!")
                break
            print("That's not a number.")
        i += 1

fun(randint(1, 100))
