#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: November 2019
# This program rounds numbers with user input


def rounding(deci, deci_place):
    # This function rounds the user's number

    # Process
    rounded = (deci * (10 ** deci_place) + 0.5)
    rounded = int(rounded)
    rounded = rounded / (10 ** deci_place)

    return rounded


def main():
    # This function gets user's input and shows rounded input
    rounding_num = []

    print("Welcome to rounding calculator.")
    print("")
    # Process
    user_deci = input("Enter a decimal: ")
    try:
        user_deci = float(user_deci)
        user_deci_place = input("Enter desired decimal places to round to: ")
        try:
            user_deci_place = int(user_deci_place)
            rounding_num.append(user_deci)
            rounded_num = rounding(user_deci, user_deci_place)
            print("")
            print("Rounded number: ", rounded_num)
        except Exception:
            print("Wrong input. Try again.")
    except Exception:
        print("Wrong input. Try again.")


if __name__ == "__main__":
    main()
