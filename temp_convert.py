#!/usr/bin/env python3

# Created by Paterry Baptichon
# Created on 2022-05-10
# This program can convert degrees celsius to fahrenheit


def fahrenheit():
    # this function can convert degrees celsius to fahrenheit

    print("This program can convert degrees celsius to fahrenheit.")
    print("\n", end="")

    # input of the user
    temperature_string = input("Enter a temperature(℃): ")
    print("\n", end="")

    try:
        temperature_integer = int(temperature_string)

        # process and calculation of celsius to fahrenheit
        fahrenheit = (9/5)*temperature_integer + 32
 
        # display what the celsius value is in fahrenheit
        print("{0}°C is equal to {1}°F"
              .format(temperature_integer, fahrenheit))
        # if user enters invalid input then display " this is not an integer"
    except Exception:
        print("This is not an integer")


def main():
    # this function just calls other functions

    # call functions
    fahrenheit()


if __name__ == "__main__":
    main()

