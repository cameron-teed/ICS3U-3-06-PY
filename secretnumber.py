#!usr/bin/env python

# Created by: Cameron Teed
# Created On: September 2019
# this program gets you to guess my number

import random


def main():
    # this program gets you to guess my number

    # This gives me a rondom number
    very_secret = random.randint(1, 50+1)

    # This sets the variable sevret number to false
    secret_number = False

    # process
    if secret_number == very_secret:
        # output
        print("First try!")

    # process
    if secret_number == 0:
        # output
        print("")

    # because secret number is false, and not equal to a number it will run
    # this section
    while type(secret_number) is not int:

        try:

            secret_number = int(input("Try and guess my number: "))
        # say if there is an error
        except ValueError:
            print(" ")
            print('Please enter a number')

    while secret_number != very_secret:

        if secret_number == 0:
            print("")

        if secret_number <= -1:
            print(" ")
            print("go higher")

        while secret_number >= 1:
            if secret_number <= very_secret:
                print(" ")
                print("go higher")

            break

        if secret_number >= very_secret:
            print(" ")
            print("go lower")

        if secret_number != very_secret:
            print("you suck, try again")

        secret_number = False

        if type(secret_number) is not int:

            try:

                secret_number = int(input("Try and guess my number: "))

            except ValueError:
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print('Please enter a number')

        if secret_number == very_secret:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("you got it bud")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            pass


if __name__ == "__main__":
    main()
