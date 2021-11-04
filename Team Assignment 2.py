def guessing_game():
    import random
    playagain = "y"
    while playagain == "y":
        target = random.randrange(1, 10)
        guess = int(input("Guess a number between 1-10: "))
        if guess != target:  # guess must be higher than answer
            if guess < target:
                print("please guess higher")
            else:  # guess must be lower than answer
                print("please guess lower")
            guess = int(input())
            if guess == target:  # guess is correct
                print("You Win")
            else:  # guess is wrong
                print("better luck next time")
        else:  # guess is right the first time
            print("first try, hacker")

        playagain = input("Play Again? [y/n]: ")
    n = quit()


guessing_game()
