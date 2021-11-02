# November 2, 2021
# Team: Jamie, Noah
# Objective: create a guessing game, that allows user to guess between 1-10.

def guessing_game():
    import random
    playagain = "y"
    while playagain == "y":
        Target= random.randrange(1,10)
        guess= int(input("Guess a number between 1-10: "))
        if guess !=Target: # guess must be higher than answer
            if guess < Target:
                print("please guess higher")
            else: # guess must be lower than answer
                print("please guess lower")
            guess = int(input())
            if guess == Target: # guess is correct
                print("You Win")
            else: # guess is wrong
                print("better luck next time")
        else: # guess is right the first time
            print("first try, hacker")

        playagain = input("Play Again? [y/n]: ")
    n = quit()

guessing_game()