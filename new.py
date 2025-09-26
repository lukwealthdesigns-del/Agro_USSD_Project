import csv
from pathlib import Path

# --- Database Setup ---
database = Path("database")
if database.exists() == False:
    database.mkdir()
farmers_csv = database / "farmers.csv"
buyers_csv = database / "buyers.csv"
products_csv = database / "products.csv"  # For farmer's listed products

# Initialize CSV with headers if files do not exist
if farmers_csv.exists() == False:
    with open(farmers_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["FULL NAME", "PHONE NUMBER", "STATE", "CITY", "FARM SIZE", "PRIMARY CROPS", "PIN"])

if buyers_csv.exists() == False:
    with open(buyers_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["FULL NAME", "PHONE NUMBER", "STATE", "CITY", "PIN"])

if products_csv.exists() == False:  # Initialize products CSV
    with open(products_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["FARMER PHONE", "PRODUCT", "QUANTITY", "PRICE"])


# --- Farmer Dashboard Functions ---
def farmer_dashboard(farmer_phone):
    while True:
        print("\n--- Farmer Dashboard ---")
        print("1. Update Details")
        print("2. List Product to Sell")
        print("3. View Listed Products")
        print("4. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            update_farmer_details(farmer_phone)
        elif choice == '2':
            list_product_to_sell(farmer_phone)
        elif choice == '3':
            view_listed_products(farmer_phone)
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")


def update_farmer_details(farmer_phone):
    print("\n--- Update Farmer Details ---")
    farmers_data = []
    updated = False
    with open(farmers_csv, "r", newline="", encoding="utf-8") as f_read:
        reader = csv.DictReader(f_read)
        for row in reader:
            if row["PHONE NUMBER"] == farmer_phone:
                print(f"Current Details for {row['FULL NAME']}:")
                for key, value in row.items():
                    print(f"{key}: {value}")

                print("\nWhich detail would you like to update?")
                print("1. Full Name")
                print("2. Phone Number")
                print("3. State")
                print("4. City")
                print("5. Farm Size")
                print("6. Primary Crops")
                print("7. PIN")
                print("8. Cancel")
                update_choice = input("Enter your choice: ")

                if update_choice == '1':
                    row["FULL NAME"] = input("Enter new Full Name: ")
                elif update_choice == '2':
                    new_phone = input("Enter new Phone Number: ")
                    row["PHONE NUMBER"] = new_phone
                    farmer_phone = new_phone
                elif update_choice == '3':
                    row["STATE"] = input("Enter new State: ")
                elif update_choice == '4':
                    row["CITY"] = input("Enter new City: ")
                elif update_choice == '5':
                    row["FARM SIZE"] = input("Enter new Farm Size: ")
                elif update_choice == '6':
                    row["PRIMARY CROPS"] = input("Enter new Primary Crops: ")
                elif update_choice == '7':
                    new_pin = input("Enter new 4-digit PIN: ")
                    if len(new_pin) == 4 and new_pin.isdigit():
                        row["PIN"] = new_pin
                    else:
                        print("Invalid PIN. PIN not updated.")
                elif update_choice == '8':
                    print("Update cancelled.")
                    farmers_data.append(row)
                    continue
                else:
                    print("Invalid choice.")
                    farmers_data.append(row)
                    continue

                updated = True
                print("Details updated successfully!")
            farmers_data.append(row)

    if updated == True:
        with open(farmers_csv, "w", newline="", encoding="utf-8") as f_write:
            fieldnames = ["FULL NAME", "PHONE NUMBER", "STATE", "CITY", "FARM SIZE", "PRIMARY CROPS", "PIN"]
            writer = csv.DictWriter(f_write, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(farmers_data)
    else:
        print("Farmer not found or no updates made.")


def list_product_to_sell(farmer_phone):
    print("\n--- List New Product ---")
    product_name = input("Enter Product Name (e.g., Maize, Beans): ")
    while True:
        try:
            quantity = float(input("Enter Quantity (e.g., 50)in kg: "))
            break
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    while True:
        try:
            price = float(input("Enter Asking Price per unit (e.g., 1000 NGN): "))
            break
        except ValueError:
            print("Invalid price. Please enter a number.")

    with open(products_csv, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([farmer_phone, product_name, quantity, price])
    print("Product listed successfully!")


def view_listed_products(farmer_phone):
    print("\n--- Your Listed Products ---")
    found_products = False
    with open(products_csv, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["FARMER PHONE"] == farmer_phone:
                found_products = True
                print(f"Product: {row['PRODUCT']}, Quantity: {row['QUANTITY']}, Price: {row['PRICE']}")

    if found_products == False:
        print("You have no products listed yet.")



# --- Buyer Dashboard Functions ---
def buyer_dashboard(buyer_phone):
    while True:
        print("\n--- Buyer Dashboard ---")
        print("1. Update Details")
        print("2. View Listed Products")
        print("3. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            update_buyer_details(buyer_phone)
        elif choice == '2':
            view_listed_products(buyer_phone)
        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")


def update_buyer_details(buyer_phone):
    print("\n--- Update Buyer Details ---")
    buyers_data = []
    updated = False
    with open(buyers_csv, "r", newline="", encoding="utf-8") as f_read:
        reader = csv.DictReader(f_read)
        for row in reader:
            if row["PHONE NUMBER"] == buyer_phone:
                print(f"Current Details for {row['FULL NAME']}:")
                for key, value in row.items():
                    print(f"{key}: {value}")

                print("\nWhich detail would you like to update?")
                print("1. Full Name")
                print("2. Phone Number")
                print("3. State")
                print("4. City")
                print("5. PIN")
                print("6. Cancel")
                update_choice = input("Enter your choice: ")

                if update_choice == '1':
                    row["FULL NAME"] = input("Enter new Full Name: ")
                elif update_choice == '2':
                    new_phone = input("Enter new Phone Number: ")
                    row["PHONE NUMBER"] = new_phone
                    buyer_phone = new_phone
                elif update_choice == '3':
                    row["STATE"] = input("Enter new State: ")
                elif update_choice == '4':
                    row["CITY"] = input("Enter new City: ")
                elif update_choice == '5':
                    new_pin = input("Enter new 4-digit PIN: ")
                    if len(new_pin) == 4 and new_pin.isdigit():
                        row["PIN"] = new_pin
                    else:
                        print("Invalid PIN. PIN not updated.")
                elif update_choice == '6':
                    print("Update cancelled.")
                    buyers_data.append(row)
                    continue
                else:
                    print("Invalid choice.")
                    buyers_data.append(row)
                    continue

                updated = True
                print("Details updated successfully!")
            buyers_data.append(row)

    if updated == True:
        with open(buyers_csv, "w", newline="", encoding="utf-8") as f_write:
            fieldnames = ["FULL NAME", "PHONE NUMBER", "STATE", "CITY", "PIN"]
            writer = csv.DictWriter(f_write, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(buyers_data)
    else:
        print("Buyer not found or no updates made.")
    
def view_listed_products(buyer_phone):
    print("\n---  Listed Products ---")
    found_products = False
    with open(products_csv, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["FARMER PHONE"] == buyer_phone:
                found_products = True
                print(f"Product: {row['PRODUCT']}, Quantity: {row['QUANTITY']}, Price: {row['PRICE']}, {row['FARMER PHONE']}")

    if found_products == False:
        print("There are no products listed yet.")





# --- Main Loop ---
while True:
    option = input("Kindly Dial *620#: ")
    if option == "*620#":
        print("Welcome to Haven Agro Bank")
        menu = int(input("Are you a farmer or a buyer?\n1. Farmer\n2. Buyer\nChoose Option:  "))
        if menu == 1:
            menu_o = int(input("1. Register as a farmer  2. Login as a farmer\nChoose Option: "))

            if menu_o == 1:
                while True:
                    first_name = input("Enter Your First Name: ")
                    if first_name != "":
                        break
                    else:
                        print("Dear user, Your first name cannot be empty. Kindly input your first name and try again")

                while True:
                    surname = input("Enter Your Surname: ")
                    if surname != "":
                        break
                    else:
                        print("Dear user, Your surname cannot be empty. Kindly input your surname and try again")

                full_name = f"{surname} {first_name}"

                while True:
                    phonenumber = input("Enter Your Phone number (11 digits): ")
                    if len(phonenumber) == 11 and phonenumber.isdigit():
                        break
                    else:
                        print("Invalid phone number. Please enter an 11-digit number.")

                while True:
                    location1 = input("Enter your location (state): ").strip().title()
                    if location1 != "":
                        break
                    else:
                        print("Dear user, Your state cannot be empty. Kindly input your state and try again")

                while True:
                    location2 = input("Enter your location (city): ").strip().title()
                    if location2 != "":
                        break
                    else:
                        print("Dear user, Your city cannot be empty. Kindly input your city and try again")

                while True:
                    farmsize = input("Kindly enter your farm size in acres: ")
                    if farmsize != "":
                        break
                    else:
                        print("Dear user, Your farmsize cannot be empty. Kindly input your farmsize and try again")

                while True:
                    crops = input("Kindly enter your primary crops: ")
                    if crops != "":
                        break
                    else:
                        print("Dear user, Your primary crops cannot be empty. Kindly input your primary crops and try again")

                farmer_dictionary = {
                    "Full Name": full_name,
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
                        print("Please restart registration to edit details.")
                        continue
                    else:
                        print("Wrong input, Try again !!!")

                pin_set = False
                while pin_set == False:
                    pin = input("Enter Your 4 digit pin: ")
                    if len(pin) == 4 and pin.isdigit():
                        reenter_pin = input("Confirm your pin: ")
                        if reenter_pin == pin:
                            with open(farmers_csv, "a", newline="", encoding="utf-8") as f:
                                writer = csv.writer(f)
                                writer.writerow([full_name, phonenumber, location1, location2, farmsize, crops, pin])
                            print("Farmer registered successfully!\n")
                            pin_set = True
                        else:
                            print("PINs do not match. Please try again.")
                    else:
                        print("PIN must be 4 digits. Please try again.")

            elif menu_o == 2:
                while True:
                    phone = input("Enter Phone Number: ")
                    pin = input("Enter Your Pin: ")
                    logged_in_phone = ""
                    with open(farmers_csv, "r", newline="", encoding="utf-8") as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            if row["PHONE NUMBER"] == phone and row["PIN"] == pin:
                                print(f"Welcome back, {row['FULL NAME']}!")
                                logged_in_phone = row["PHONE NUMBER"]
                                break
                    if logged_in_phone != "":
                        farmer_dashboard(logged_in_phone)
                    else:
                        print("Invalid login details for farmer.\n")

        elif menu == 2:
            menu_1 = int(input("1. Register as a buyer  2. Login as a buyer\nChoose Option: "))
            if menu_1 == 1:
                while True:
                    print("Enter your details")
                    first_name = input("Kindly enter your first name: ").strip().title()
                    if first_name != "":
                        break
                    else:
                        print("Dear user, Your first name cannot be empty. Kindly input your first name and try again")

                while True:
                    last_name = input("Kindly enter your last name: ").strip().title()
                    if last_name != "":
                        break
                    else:
                        print("Dear user, Your last name cannot be empty. Kindly input your last name and try again")

                full_name = f"{first_name} {last_name}"

                while True:
                    phone_number = input("Enter your phone number (11 digits): ")
                    if len(phone_number) == 11 and phone_number.isdigit():
                        break
                    else:
                        print("Your phone number is invalid!!! Try again")

                while True:
                    location1 = input("Enter your location (state): ").strip().title()
                    if location1 != "":
                        break
                    else:
                        print("Dear user, Your state cannot be empty. Kindly input your state and try again")

                while True:
                    location2 = input("Enter your location (city): ").strip().title()
                    if location2 != "":
                        break
                    else:
                        print("Dear user, Your city cannot be empty. Kindly input your city and try again")

                buyer_dictionary = {
                    "Full Name": full_name,
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
                        print("Please restart registration to edit details.")
                        continue
                    else:
                        print("Wrong input, Try again !!!")

               
             
                    pin = input("Enter your 4 digit PIN: ")
                    if len(pin) == 4 and pin.isdigit():
                        confirm_pin = input("Kindly confirm your PIN: ")
                        if confirm_pin == pin:
                            with open(buyers_csv, "a", newline="", encoding="utf-8") as f:
                                writer = csv.writer(f)
                                writer.writerow([full_name, phone_number, location1, location2, pin])
                            print("Buyer registered successfully!\n")
                            
                        else:
                            print("PINs do not match. Please try again.")
                    else:
                        print("Your PIN is invalid!!! Try again")

            elif menu_1 == 2:
                while True:
                    phone = input("Enter Phone Number: ")
                    pin = input("Enter Your Pin: ")
                    logged_in_phone = ""
                    with open(buyers_csv, "r", newline="", encoding="utf-8") as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            if row["PHONE NUMBER"] == phone and row["PIN"] == pin:
                                print(f"Welcome back, {row['FULL NAME']}!")
                                logged_in_phone = row["PHONE NUMBER"]
                                break
                    if logged_in_phone != "":
                        buyer_dashboard(logged_in_phone)
                    else:
                        print("Invalid login details for buyer.\n")
        else:
            print("Invalid option. Please choose 1 for Farmer or 2 for Buyer.")

    else:
        print("Invalid code. Try again.")
