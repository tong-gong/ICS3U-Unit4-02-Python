#!/usr/bin/env python3

# Created by Tong Gong
# Created time December 2020
# This is a while loop program.


def main():
    # This is the function to run while loop.

    factorial = 1
    # Input
    user_input_number = input("Enter a positive integer:")
    print("")

    # Process & output
    try:
        user_input_number = int(user_input_number)
        if user_input_number > 0:
            while_number = user_input_number
            while while_number > 0:
                factorial = while_number * factorial
                while_number = while_number - 1
            else:
                print("factorial of {0} is {1}".format(user_input_number, factorial))
        elif while_number < 0:
            print("Sorry, you did not enter a positive integer!")
    except Exception:
        print("You are not type in an integer!")



if __name__ == "__main__":
    main()
