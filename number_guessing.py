#!/usr/bin/env python

import random


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def read_int(prompt):
    numstr = input("{}: ".format(prompt))
    while not represents_int(numstr):
        print("{} is not an integer!".format(numstr))
        numstr = input("{}: ".format(prompt))
    return int(numstr)


def read_ints():
    start = read_int("Enter a starting digit")
    stop = read_int("Enter a bigger number than start")
    return (start, stop)

print("Welcome to my number guesser!")

(start, stop) = read_ints()
while start >= stop:
    print("Start number {} must be smaller than end number {}".format(start, stop))
    (start, stop) = read_ints()

RANDOM_NUMBER = random.randint(start, stop)
# print("Random number: {}".format(RANDOM_NUMBER))

guess = 1
user_guess = read_int("Enter a guess")
while user_guess != RANDOM_NUMBER:
    guess += 1
    if user_guess < RANDOM_NUMBER:
        user_guess = read_int("Wrong. Try a bigger number next time\nEnter a guess")
    else:
        user_guess = read_int("Wrong. Try a smaller number next time\nEnter a guess")

if guess == 1:
    print("Congratulations! You've found the correct number in " + str(guess) + " guess :)\n")
else:
    print("Congratulations! You've found the correct number in " + str(guess) + " guesses :)\n")

    # add a method to play agin without restarting
    # text = Do you want to play again?
