from ILS import ILS
from USD import USD
import os


def get_user_value():

    choice = input("Please choose an option(1/2)\n1. Dollars to Shekels\n2. Shekels to dollars\n")
    if choice == '1':
        # convert to shekel
        value_to_convert = float(input("please enter an amount to convert:"))
        usd = USD()
        print(usd.calculate(value_to_convert))
        # save results to list
    elif choice == '2':
        # convert to dollar
        value_to_convert = float(input("please enter an amount to convert:"))
        ils=ILS()
        print(ils.calculate(value_to_convert))
        # save results to list
    else:
        print("invalid choice please try again")


def main():
    while True:
        os.system('cls')
        print("Welcome to currency converter")
        get_user_value()
        start_over = input("do you want to start over (Y/N) ?")
        if start_over.upper() == "N":
            print("Thanks for using our currency converter")
            # print results
            # save results to file
            break
        elif start_over.upper() != "Y":
            print("invalid input - assuming YES")


main()
