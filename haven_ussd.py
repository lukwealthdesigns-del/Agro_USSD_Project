
from pathlib import Path
import csv
# --- Database Setup ---
database = Path("database")
if database.exists() is False:   
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
        menu = int(input("Are you a farmer or a buyer?\n1. Farmer\n2. Buyer\nChoose Option: "))
        # ---------------- Farmer Menu ----------------
        if menu == 1:
            menu_o = int(input("1. Register as a farmer  2. Login as a farmer\nChoose Option: "))
            # Farmer Registration
            if menu_o == 1:
                first_name = input("Enter Your First Name: ").strip().title()
                surname = input("Enter Your Surname: ").strip().title()
                full_name = f"{surname} {first_name}"
                phone = input("Enter Your Phone number (11 digits): ")
                state = input("Enter your location (state): ").strip().title()
                city = input("Enter your location (city): ").strip().title()
                farm_size = input("Kindly enter your farm size in acres: ")
                crops = input("Enter your primary crops: ").strip().title()
                pin = input("Enter Your 4 digit pin: ")
                re_pin = input("Confirm your pin: ")
                if pin == re_pin:
                    with open(farmers_csv, "a", newline="", encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerow([full_name, phone, state, city, farm_size, crops, pin])
                    print("Farmer registered successfully!\n")
                else:
                    print("PINs do not match.\n")
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
            menu_1 = int(input("1. Register as a buyer  2. Login as a buyer\nChoose Option: "))
            # Buyer Registration
            if menu_1 == 1:
                first_name = input("Enter Your First Name: ").strip().title()
                last_name = input("Enter Your Last Name: ").strip().title()
                full_name = f"{first_name} {last_name}"
                phone = input("Enter Your Phone number (11 digits): ")
                state = input("Enter your location (state): ").strip().title()
                city = input("Enter your location (city): ").strip().title()
                pin = input("Enter Your 4 digit pin: ")
                re_pin = input("Confirm your pin: ")
                if pin == re_pin:
                    with open(buyers_csv, "a", newline="", encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerow([full_name, phone, state, city, pin])
                    print("white_tick: Buyer registered successfully!\n")
                else:
                    print("PINs do not match.\n")
            # Buyer Login
            elif menu_1 == 2:
                phone = input("Enter Phone Number: ")
                pin = input("Enter Your Pin: ")
                logged_in = ""   # empty string
                with open(buyers_csv, "r", newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row["PHONE NUMBER"] == phone and row["PIN"] == pin:
                            print(f":white_tick: Welcome back, {row['FULL NAME']}!")
                            logged_in = row["FULL NAME"]
                            break
                if logged_in == "":
                    print("Invalid login details for buyer.\n")
        else:
            print("Invalid option, choose 1 or 2.\n")
    else:
        print("Wrong code. Try again.\n")