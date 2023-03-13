from EUR import EUR
from ILS import ILS
from Result import Result
from USD import USD
import os

lst = []


def get_amount():
    while True:
        try:
            value_to_convert = float(input("please enter an amount to convert:"))
            return value_to_convert
        except:
            print("invalid input")


def get_yes_no(text):
    while True:
        rc = input(text + "(Y/N) ?").upper()
        if rc == "Y" or rc == "N":
            return rc
        print("Invalid Input - Please try again.")


def get_user_choice():

    choice = input("Please choose an option(1/2/3)\n1. Dollars to Shekels\n2. Shekels to dollars\n3. ILS to EUR\nprint here:")
    if choice == '1':
        # convert to shekel
        value_to_convert = get_amount()
        usd = USD()
        new_value = usd.calculate(value_to_convert)
        print(new_value)
        # save results to list
        result = Result(new_value, "USD to ILS")
        lst.append(result)

    elif choice == '2':
        # convert to dollar
        value_to_convert = get_amount()
        ils = ILS()
        new_value = ils.calculate(value_to_convert)
        print(new_value)
        # save results to list
        result = Result(new_value, "ILS to USD")
        lst.append(result)
    elif choice == "3":
        value_to_convert = get_amount()
        eur = EUR()
        new_value = eur.calculate(value_to_convert)
        print(new_value)
        result = Result(new_value, "ILS to EUR")
        lst.append(result)
    else:
        print("invalid choice please try again")


def main():
    print("Welcome to currency converter")
    while True:
        os.system('cls')
        get_user_choice()
        start_over = get_yes_no("do you want to start over")
        if start_over == "N":
            print("Thanks for using our currency converter")
            file1 = open("results.txt", "a")
            for result in lst:
                text = result.to_string()
                print(text)
                file1.write(text+"\n")
            file1.close()
            break


main()
