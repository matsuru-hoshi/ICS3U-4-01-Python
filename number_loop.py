#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Oct 2019
# This is program loop number adder


def main():
    # funciton calculates the number added up to number

    # variable
    answer = 0
    repeater = 0

    # Welcome statement
    print("Welcome, I will add up numbers up to the number that you tell me.")
    print("Ex. 1 + 2 + 3 + 4 = 13")
    input("\nPress Enter to continue.")

    # input
    number = int(input("What is your number: "))

    # process
    while repeater <= number:
        answer = answer + repeater
        repeater = repeater + 1

    print("The answer is " + str(answer) + ".")


if __name__ == "__main__":
    main()
