#!/usr/bin/env python3

# Created By: Tony G

# Date: 2025-03-18

# Asks for user input and tells user if number is correct or not


def main():
    print("Greetings! Please input a number")
    user_input = input("Please enter a number: ")

    number = float(user_input)
    if number == 5:
        print("Congratulations! Correct!")
    else:
        print("Incorrect, try again :(")


if __name__ == "__main__":
    main()
