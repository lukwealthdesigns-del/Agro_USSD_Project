import csv
from pathlib import Path


# Creating Class for farmer
class Farmer:
    def __init__(self, full_name, phonenumber, location, farmsize, primary_crops, pin):
        self.full_name = full_name
        self.phonumber = phonenumber
        self.location = location
        farmsize = farmsize
        self.primary_crops = primary_crops
        self.pin = pin

# Creating empty dictionary for farmer
farmer_dictionary = {}

# Managing the file path
database = Path("database")
database.mkdir(exist_ok=True)
farmer_csv = database / "farmer.csv"
farmer_csv

# Writing in file path
with open(farmer_csv, "w", newline="", encoding="utf-8") as f:
    f.write("FULL NAME, PHONE NUMBER, STATE, CITY, FARM SIZE, PRIMARY CROPS, PIN")
    #f.write(farmer_dictionary)
    writer = csv.writer(f)
    writer.writerows(farmer_dictionary) # Write all rows at once
    




# Collecting Inputs for registration and log in
while True:
    option = input("Kindly Dial *620#: ")
    if option == "*620#":
        print("Welcome to Haven Agro Bank")
        menu = int(
            input("Are you a farmer or a buyer?\n1. Farmer\n2. Buyer\nChoose Option:  "))
        if menu == 1:
            menu_o = int(
                input("1. Register as a farmer  2. Login as a farmer\nChoose Option: "))

            if menu_o == 1:
                while True:
                    first_name = input("Enter Your First Name: ")
                    if first_name != "":
                        break
                    else:
                        print(
                            "Dear user, Your first name cannot be empty. Kindly input your first name and try again")
                while True:
                    surname = input("Enter Your Suranme: ")
                    if surname != "":
                        break
                    else:
                        print(
                            "Dear user, Your surname cannot be empty. Kindly input your surname and try again")
                    full_name = (surname, first_name)
                    farmer_dictionary["full name"] = full_name
                while True:
                    phonenumber = (input("Enter Your Phone number: "))
                    if len(phonenumber) == 11:
                        break
                    else:
                        print("R-enter phone number")
                        farmer_dictionary["phone number"] = phonenumber
                while True:
                    location1 = input(
                        "Enter your location (state): ").strip().title()
                    if location1 != "":
                        break
                    else:
                        print(
                            "Dear user, Your state cannot be empty. Kindly input your state and try again")
                    farmer_dictionary["State"] = location1
                while True:
                    location2 = input(
                        "Enter your location (city): ").strip().title()
                    if location2 != "":
                        break
                    else:
                        print(
                            "Dear user, Your city cannot be empty. Kindly input your city and try again")
                    farmer_dictionary["City"] = location2
                while True:
                    farmsize = input("kindly enter your farm size in acres: ")
                    if farmsize != "":
                        break
                    else:
                        print(
                            "Dear user, Your farmsize cannot be empty. Kindly input your farmsize and try again")
                    farmer_dictionary["Farm Size"] = farmsize
                while True:
                    pin = (input("Enter Your 4 digit pin: "))
                    if len(pin) == 4:
                        break
                    else:
                        print("Ensure 4 Digit Pin is correct: ")
                    farmer_dictionary["Pin"] = pin
                while True:
                    reenter_pin = (input("Confirm your pin: "))
                    if reenter_pin == pin:
                        break
                    else:
                        print("incorrect pin  verify your pin: ")
                # save_register_farmer(farmer_dictionary)

            elif menu_o == 2:
                phonenumber = int(input("Enter Phone Number: "))
                pin = int(input("Enter Your Pin: "))


            while True:

                confirm_details = int(input(f"Kindly Confirm your information\n{farmer_dictionary}\n1. Yes, Proceed \n2. No, Edit\nKindly choose: "))
                if confirm_details == 1:
                    print("Your information has been saved succefully")
                    break
                elif confirm_details == 2:
                    print("Try again !!!")
                else:
                    print("Wrong input, Try again !!!")

        elif menu == 2:
            menu_1 = int(
                input("1. Register as a buyer  2. Login as a buyer\nChoose Option: "))
            if menu_1 == 1:
                while True:
                    print("Enter your details")
                    first_name = input(
                        "Kindly enter your first name: ").strip().title()
                    if first_name != "":
                        break
                    else:
                        print(
                            "Dear user, Your first name cannot be empty. Kindly input your first name and try again")

                while True:
                    last_name = input(
                        "Kindly enter your last name: ").strip().title()
                    if last_name != "":
                        break
                    else:
                        print(
                            "Dear user, Your last name cannot be empty. Kindly input your last name and try again")

                while True:
                    phone_number = input("Enter your phone number: ")
                    if len(phone_number) == 11 and phone_number.isdigit():
                        break
                    else:
                        print("Your phone number is invalid!!! Try again")

                while True:
                    location1 = input(
                        "Enter your location (state): ").strip().title()
                    if location1 != "":
                        break
                    else:
                        print(
                            "Dear user, Your state cannot be empty. Kindly input your state and try again")

                while True:
                    location2 = input(
                        "Enter your location (city): ").strip().title()
                    if location2 != "":
                        break
                    else:
                        print(
                            "Dear user, Your city cannot be empty. Kindly input your city and try again")

                while True:
                    pin = input("Enter your 4 digit PIN: ")
                    if len(pin) == 4 and pin.isdigit():
                        break
                    else:
                        print("Your PIN is invalid!!! Try again")

                while True:
                    confirm_pin = input("Kindly confirm your PIN: ")
                    if confirm_pin == pin:
                        break
                    else:
                        print(
                            "You have entered a PIN different from the previous PIN. Please try again")

                buyer_dictionary = {
                    "First Name": first_name,
                    "Last Name": last_name,
                    "Phone Number": phone_number,
                    "State": location1,
                    "City": location2

                }
                dictionary = {}
                dictionary["name"] = location1
                while True:

                    confirm_details = int(input(
                        f"Kindly Confirm your information\n{dictionary}\n1. Yes, Proceed \n2. No, Edit\nKindly choose: "))
                    if confirm_details == 1:
                        print("Your information has been saved succefully")
                        break
                    elif confirm_details == 2:
                        print("Try again !!!")
                    else:
                        print("Wrong input, Try again !!!")

            elif menu_1 == 2:
                while True:
                    print("\nLOG IN\n")
                    phone = input("Kindly enter your phone number: ")
                    if phone == phone_number:
                        break
                    else:
                        print("Your phone number is invalid!!!")

                while True:
                    cpin = input("Kindly enter your PIN: ")
                    if cpin == confirm_pin:
                        break
                    else:
                        print("Your PIn is invalid!!!")

        else:
            print("Enter if you are a farmer or buyer")

    else:
        print("Try again")
