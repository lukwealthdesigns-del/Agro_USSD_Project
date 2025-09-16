import csv
from pathlib import Path

# --- Database Setup ---
database = Path("database")
if database.exists() is False:   # instead of if not database.exists()
    database.mkdir()
farmers_csv = database / "farmers.csv"
buyers_csv = database / "buyers.csv"

# Initialize CSV with headers if files do not exist
if farmers_csv.exists() is False:
    with open(farmers_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["FULL NAME", "PHONE NUMBER", "STATE", "CITY", "FARM SIZE", "PRIMARY CROPS", "PIN"])
if buyers_csv.exists() is False:
    with open(buyers_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["FULL NAME", "PHONE NUMBER", "STATE", "CITY", "PIN"])
# --- Main Loop ---
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
                
                while True:
                    phonenumber = (input("Enter Your Phone number: "))
                    if len(phonenumber) == 11:
                        break
                    else:
                        print("R-enter phone number")
                        
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
                    farmsize = input("kindly enter your farm size in acres: ")
                    if farmsize != "":
                        break
                    else:
                        print(
                            "Dear user, Your farmsize cannot be empty. Kindly input your farmsize and try again")
                while True:
                    crops = input("kindly enter your primary crops: ")
                    if farmsize != "":
                        break
                    else:
                        print(
                            "Dear user, Your primary cannot be empty. Kindly input your primary crops and try again")
                farmer_dictionary = {
                    "First Name": first_name,
                    "Last Name": surname,
                    "Phone Number": phonenumber,
                    "State": location1,
                    "City": location2,
                    "Crops": crops,
                    "Farm Size": farmsize

                }
                while True:

                    confirm_details = int(input(
                        f"Kindly Confirm your information\n{farmer_dictionary}\n1. Yes, Proceed \n2. No, Edit\nKindly choose: "))
                    if confirm_details == 1:

                        break
                    elif confirm_details == 2:
                        print("Try again !!!")
                    else:
                        print("Wrong input, Try again !!!")
                while True:
                    pin = (input("Enter Your 4 digit pin: "))
                    if len(pin) == 4:
                        break
                    else:
                        print("Ensure 4 Digit Pin is correct: ")
                    
        
                reenter_pin = (input("Confirm your pin: "))
                if reenter_pin == pin:
                    with open(farmers_csv, "a", newline="", encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerow([surname, phonenumber, location1, location2, farmsize, crops, pin])
                    print("Farmer registered successfully!\n")
                else:
                    print("incorrect pin  verify your pin: ")
                
            # Farmer Login
            elif menu_o == 2:
                phone = input("Enter Phone Number: ")
                pin = input("Enter Your Pin: ")
                logged_in = ""   # empty string
                with open(farmers_csv, "r", newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row["PHONE NUMBER"] == phone and row["PIN"] == pin:
                            print(f"Welcome back, {row['FULL NAME']}!")
                            logged_in = row["FULL NAME"]
                            break
                if logged_in == "":
                    print("Invalid login details for farmer.\n")
        # ---------------- Buyer Menu ----------------
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
                full_name = (first_name, last_name)
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
                buyer_dictionary = {
                    "First Name": first_name,
                    "Last Name": last_name,
                    "Phone Number": phone_number,
                    "State": location1,
                    "City": location2,
                    
                }
                while True:

                    confirm_details = int(input(
                        f"Kindly Confirm your information\n{buyer_dictionary}\n1. Yes, Proceed \n2. No, Edit\nKindly choose: "))
                    if confirm_details == 1:

                        break
                    elif confirm_details == 2:
                        print("Try again !!!")
                    else:
                        print("Wrong input, Try again !!!")

                while True:
                    pin = input("Enter your 4 digit PIN: ")
                    if len(pin) == 4 and pin.isdigit():
                        break
                    else:
                        print("Your PIN is invalid!!! Try again")

                while True:
                    confirm_pin = input("Kindly confirm your PIN: ")
                    if confirm_pin == pin:
                        with open(buyers_csv, "a", newline="", encoding="utf-8") as f:
                            writer = csv.writer(f)
                            writer.writerow([full_name, phone_number, location1, location2, pin])
                        print("Buyer registered successfully!\n")
                    else:
                        print(
                            "You have entered a PIN different from the previous PIN. Please try again")

                
              
              
            # Buyer Login
            elif menu_1 == 2:
                phone = input("Enter Phone Number: ")
                pin = input("Enter Your Pin: ")
                logged_in = ""   # empty string
                with open(buyers_csv, "r", newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row["PHONE NUMBER"] == phone and row["PIN"] == pin:
                            print(f"Welcome back, {row['FULL NAME']}!")
                            logged_in = row["FULL NAME"]
                            break
                if logged_in == "":
                    print("Invalid login details for buyer.\n")
        else:
                print("Enter if you are a farmer or buyer")

    else:
            print("Try again")