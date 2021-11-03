# Jaime S
# 11/2/2021
# Team Members: Jaime S & Noah M.
# Simple Draft
import random
number = random.randint(1, 10)

player_name = input("What's your name?")
number_of_guesses = 0
print(player_name + ' I am guessing a number between 1 and 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is low')
        print('Please guess higher')
    if guess > number:
        print('Your guess is high')
        print('Please guess lower')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))