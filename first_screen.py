from EUR import EUR
from ILS import ILS
from USD import USD
import os
print("Welcome to currency converter")
lst=[]
def get_user_value():

    global value_to_convert
    choice = input("Please choose an option(1/2/3)\n1. Dollars to Shekels\n2. Shekels to dollars\n3. ILS to EUR\nprint here:")
    if choice == '1':
        # convert to shekel
        try:
         value_to_convert = float(input("please enter an amount to convert:"))
        except:
            print("invalid character")
        usd = USD()
        print(usd.calculate(value_to_convert))
        lst.append(usd.calculate(value_to_convert))
        lst.append("USD to ILS")
        # save results to list
    elif choice == '2':
        # convert to dollar
        try:
            value_to_convert = float(input("please enter an amount to convert:"))
        except:
            print("invalid character")
        ils=ILS()
        print(ils.calculate(value_to_convert))
        # save results to list
        lst.append(ils.calculate(value_to_convert))
        lst.append("ILS to USD")
    elif choice =="3":
        try:
            value_to_convert = float(input("please enter an amount to convert:"))
        except:
            print("invalid character")
        eur=EUR()
        print(eur.calculate(value_to_convert))
        lst.append(eur.calculate(value_to_convert))
        lst.append("ILS to EUR")
        #all the try excpet saving the code from crash



    else:
        print("invalid choice please try again")


def main():
    global i
    while True:
        os.system('cls')

        get_user_value()
        start_over = input("do you want to start over (Y/N) ?")
        if start_over.upper() == "N":
            print("Thanks for using our currency converter")
            print(lst)
            file1 = open("results.txt", "a")
            file1.write(str(lst))
            file1.close()

            break
        elif start_over.upper() != "Y":
            print("invalid input ")
            get_user_value()

        elif start_over.upper() == "Y":
            get_user_value()

            file1 = open("results.txt","a")
            file1.write(str(lst))
            file1.close()




main()
