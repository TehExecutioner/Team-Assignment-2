# Jaime S
# 11/2/2021
# Team Members: Jaime S & Noah M.
# This is a program that will take a number input and guess a randomly generated number
# (player will have the option to guess higher or lower)
def guessing_game():
    import random
    play_again = "y"                               # will process user's "yes" input
    while play_again == "y":
        number = random.randrange(1, 10)              # the number chosen has to be between this range
        guess = int(input("Guess a number between 1-10: "))
        if guess != number:                          # guess must be higher than answer
            if guess < number:
                print("Please guess higher")
            else:                                     # guess must be lower than answer
                print("Please guess lower")
            guess = int(input())
            if guess == number:                       # guess is correct
                print("You guessed it!")
            else:                                     # guess is wrong
                print("Better luck next time")
        else:                                         # guess is correct for first try
            print("First try, well done!")

        play_again = input("Play Again? [y/n]: ")  # will ask user to play again
    n = quit()                                        # will quit the game

guessing_game()


