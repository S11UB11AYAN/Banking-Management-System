import random
import os


def generate_random_paragraph():
    paragraphs = [
        "Welcome to Bank Management System. By using our services, you agree to comply with the terms and conditions outlined in this policy.",
        "Account Security: It is the responsibility of the account holder to maintain the confidentiality of their login credentials. Any unauthorized access or use of your account should be reported immediately to our customer support.",
        "Transactions: All financial transactions conducted through our banking system are subject to monitoring and verification. Bank reserves the right to investigate and take action against any suspicious or fraudulent activities.",
        "Privacy: We are committed to protecting your privacy. Personal information provided to us will be handled in accordance with our privacy policy, which can be reviewed on our official website.",
        "Service Availability: While we strive to provide uninterrupted services, Bank is not liable for any disruptions due to technical issues, maintenance, or unforeseen circumstances.",
        "Termination of Services: Bank reserves the right to terminate or suspend services to any account holder for violation of terms, fraudulent activities, or any other reasons deemed necessary.",
        "Changes to Terms: We may update or modify the terms and policies of our banking system. Account holders will be notified of any changes, and continued use of our services implies acceptance of the revised terms.",
        "Governing Law: This agreement is governed by and construed in accordance with the laws of the jurisdiction in which Bank operates.",
        "Contact: For any inquiries or concerns regarding our banking management system, please contact our customer support at support@xyzbank.com.",
    ]
    return "\n".join(random.sample(paragraphs, len(paragraphs)))


def generate_account_number():
    account_number = ''.join(str(random.randint(0, 9)) for _ in range(10))
    return account_number


def generate_6_digit_pin():
    return str(random.randint(100000, 999999))


def read_specific_line(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if 1 <= line_number <= len(lines):
                specific_line = lines[line_number - 1]
                return specific_line
            else:
                return f"Line number {line_number} is out of range for the file."
    except FileNotFoundError:
        return f"The file {file_path} does not exist."


def write_to_specific_line(file_path, line_number, new_content):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        if 1 <= line_number <= len(lines):
            lines[line_number - 1] = new_content + '\n'
            with open(file_path, 'w') as file:
                file.writelines(lines)
        else:
            print(f"Line number {line_number} is out of range for the file.")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def extract_digits_from_line(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if line_number <= len(lines):
            line = lines[line_number - 1]
            digits = ''.join(filter(str.isdigit, line))
            return digits
        else:
            return "Line number out of range."


def print_box(message):
    border = '*' * (len(message) + 4)
    print(border)
    print(f'* {message} *')
    print(border)


def read_entire_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        return f"The file {file_path} does not exist."
    except Exception as e:
        return f"An error occurred: {e}"


balanceSbi = '0'
balanceAb = '0'
balanceUb = '0'

print("==========================================")
print("        BANKING MANAGEMENT SYSTEM")
print("==========================================")
choice_bank = int(input(
    "Which bank do you want to select:- \n 1. State Bank Of India\n 2. Axis Bank\n 3. Union Bank\n 4. Exit\n Please enter your choice: "))

while choice_bank != 4:
    if choice_bank == 1:
        print("==========================================")
        print("     WELCOME TO STATE BANK OF INDIA")
        print("==========================================")
        print("******************************************")
        print("*         1.Create Account               *\n*         2.Login                        *\n*         3.Terms & Conditions           *")
        print("******************************************")
        choice_option = int(input("Please enter your choice : "))
        if choice_option == 3:
            random_paragraph = generate_random_paragraph()
            print(random_paragraph)
        elif choice_option == 1:
            name = input("Please enter your full name: ")
            day = input("Enter the day of birth (e.g., 01): ")
            month = input("Enter the month of birth (e.g., 05): ")
            year = input("Enter the year of birth (e.g., 1990): ")
            age = (input("Please enter your age: "))
            phone = (input("please enter your mobile number: "))
            address = input("Please enter your current address: ")
            random_account_number = generate_account_number()
            copy_accountnumber = random_account_number
            pin = generate_6_digit_pin()
            copy_pin = pin
            date_of_birth = f"{year}-{month}-{day}"
            f = open(name+"sbi"+'.txt', 'w')
            f.write("Name: "+name+'\n')
            f.write("Date of Birth: " + date_of_birth+'\n')
            f.write("Age: "+age+'\n')
            f.write("Mobile Number: "+phone+'\n')
            f.write("Address: "+address+'\n')
            f.write("Account Number: "+random_account_number+'\n')
            f.write("Generated PIN: " + pin+'\n')
            f.write("Bank balance: "+balanceSbi)
            f.close()
            print("Your account has been successfully created!!!")
            file_path = name+"sbi"+".txt"
            line_number = 6
            result = read_specific_line(file_path, line_number)
            print(result)
            file_path = name+"sbi"+".txt"
            line_number = 7
            result_pin = read_specific_line(file_path, line_number)
            print(result_pin)
        elif choice_option == 2:
            login_name = input("Please enter your full name: ")
            login_accountNumber = input("Please enter your account number: ")
            file_path = login_name+"sbi"+".txt"
            line_number = 6
            result = read_specific_line(file_path, line_number)
            result_account_number = result.strip().split(": ")[1]
            if result_account_number == str(login_accountNumber):
                print("******************************************")
                print("*         1.View Balance                 *\n*         2.Withdraw Money               *\n*         3.Deposit Money                *\n*         4.Edit Account Details         *\n*         5.Change Pin                   *\n*         6.Transfer                     *\n*         7.View Profile                 *\n*         0.Exit                         *")
                print("******************************************")
                choice_login_option = 6
                while choice_login_option != 0:
                    choice_login_option = int(
                        input("Please enter your choice : "))
                    if choice_login_option == 1:
                        name = input("Please enter your name: ")
                        file_path = name+"sbi"+".txt"
                        line_number = 8
                        balanceSbi = extract_digits_from_line(
                            file_path, line_number)
                        print("Your current balance is: ", balanceSbi)
                        print()
                    elif choice_login_option == 2:
                        userTypedPin = input("Please enter the pin number: ")
                        if userTypedPin == copy_pin:
                            withdraw_name = input("Please enter your name: ")
                            amount_withdraw = int(
                                input("Please enter the amount you want to withdraw: "))
                            balanceSbi = int(balanceSbi)-amount_withdraw
                            print("Your current balance is ", balanceSbi)
                            balanceSbi = str(balanceSbi)
                            file_path = withdraw_name+"sbi"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+balanceSbi
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)

                            print()
                    elif choice_login_option == 3:
                        deposit_name = input("Please enter your name: ")
                        amount_deposit = int(
                            input("Please enter the amount you want to deposit: "))
                        balanceSbi = int(balanceSbi)+amount_deposit
                        print("Your current balance is ", balanceSbi)
                        balanceSbi = str(balanceSbi)
                        copy_balance = balanceSbi
                        file_path = deposit_name+"sbi"+".txt"
                        line_number_to_modify = 8
                        new_content_for_line = "Bank balance: "+balanceSbi
                        write_to_specific_line(
                            file_path, line_number_to_modify, new_content_for_line)
                        print()
                    elif choice_login_option == 4:
                        previous_name = input(
                            "Please enter your full name which is already registered: ")
                        day = input("Enter the day of birth (e.g., 01): ")
                        month = input("Enter the month of birth (e.g., 05): ")
                        year = input("Enter the year of birth (e.g., 1990): ")
                        age = (input("Please enter your age: "))
                        phone = (input("please enter your mobile number: "))
                        address = input("Please enter your current address: ")
                        name = input("Please enter your full name: ")
                        random_account_number = generate_account_number()
                        date_of_birth = f"{year}-{month}-{day}"
                        f = open(previous_name+"sbi"+'.txt', 'w')
                        os.rename(previous_name+"sbi" +
                                  '.txt', name+"sbi"+".txt")
                        f.write("Name: "+name+'\n')
                        f.write("Date of Birth: " + date_of_birth+'\n')
                        f.write("Age: "+age+'\n')
                        f.write("Mobile Number: "+phone+'\n')
                        f.write("Adrress: "+address+'\n')
                        f.write("Account Number: "+copy_accountnumber+'\n')
                        f.write("Generated PIN:" + copy_pin+'\n')
                        f.write("Bank balance: "+balanceSbi)
                        f.close()
                        print("Your account has been successfully updated!!!")
                        print()
                    elif choice_login_option == 5:
                        pin_name = input("Please enter your name: ")
                        change_pin = input(
                            "Please enter the current pin number: ")
                        if change_pin == copy_pin:
                            pin = generate_6_digit_pin()
                            copy_pin = pin
                            print("Your new pin number is: ", copy_pin)
                            print()
                            file_path = name+"sbi"+".txt"
                            line_number_to_modify = 7
                            new_content_for_line = "Generated PIN:" + copy_pin+'\n'
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                    elif choice_login_option == 6:
                        name = input("Please enter your full name: ")
                        transfer_name = input(
                            "Please enter the name of the user to whom you want to transfer: ")
                        print_box("TRANSFER DETAILS")
                        print(f"Sender: {name}")
                        print(f"Recipient: {transfer_name}")
                        print("1. State Bank of India\n2. Axis Bank\n3. Union Bank")
                        transfer_choice = int(
                            input("Please choose the bank to which you want to transfer: "))
                        if transfer_choice == 1:
                            transfer_money = int(
                                input("Please enter the amount you want to transfer: "))
                            file_path = name+"sbi"+".txt"
                            line_number = 8
                            copy_balance = extract_digits_from_line(
                                file_path, line_number)
                            copy_balance = int(copy_balance)-transfer_money
                            print_box(
                                f"Amount of Rs.{transfer_money} transferred successfully!!!")
                            print(
                                f"{name}'s current balance is Rs.{copy_balance}")
                            print()
                            copy_balance = str(copy_balance)
                            file_path = name+"sbi"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+copy_balance
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                            print()
                            file_path = transfer_name+"sbi"+".txt"
                            line_number = 8
                            balance_transfer = extract_digits_from_line(
                                file_path, line_number)
                            balance_transfer = int(
                                balance_transfer)+transfer_money
                            balance_transfer = str(balance_transfer)
                            file_path = transfer_name+"sbi"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+balance_transfer
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                        elif transfer_choice == 2:
                            transfer_money = int(
                                input("Please enter the amount you want to transfer: "))
                            file_path = name+"sbi"+".txt"
                            line_number = 8
                            copy_balance = extract_digits_from_line(
                                file_path, line_number)
                            copy_balance = int(copy_balance)-transfer_money
                            print_box(
                                f"Amount of Rs.{transfer_money} transferred successfully!!!")
                            print(
                                f"{name}'s current balance is Rs.{copy_balance}")
                            print()
                            file_path = name+"sbi"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+copy_balance
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                            print()
                            file_path = transfer_name+"ab"+".txt"
                            line_number = 8
                            balance_transfer = extract_digits_from_line(
                                file_path, line_number)
                            balance_transfer = int(
                                balance_transfer)+transfer_money
                            balance_transfer = str(balance_transfer)
                            file_path = transfer_name+"ab"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+balance_transfer
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                        elif transfer_choice == 3:
                            transfer_money = int(
                                input("Please enter the amount you want to transfer: "))
                            file_path = name+"sbi"+".txt"
                            line_number = 8
                            copy_balance = extract_digits_from_line(
                                file_path, line_number)
                            copy_balance = int(copy_balance)-transfer_money
                            print_box(
                                f"Amount of Rs.{transfer_money} transferred successfully!!!")
                            print(
                                f"{name}'s current balance is Rs.{copy_balance}")
                            print()
                            copy_balance = str(copy_balance)
                            file_path = name+"sbi"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+copy_balance
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                            print()
                            file_path = transfer_name+"ub"+".txt"
                            line_number = 8
                            balance_transfer = extract_digits_from_line(
                                file_path, line_number)
                            balance_transfer = int(
                                balance_transfer)+transfer_money
                            balance_transfer = str(balance_transfer)
                            file_path = transfer_name+"ub"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+balance_transfer
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                        elif choice_login_option == 7:
                            name = input("Please enter your name: ")
                            file_path = name+"sbi"+".txt"
                            file_contents = read_entire_file(file_path)
                            if file_contents:
                                print_box("Account Details:")
                                print(file_contents)
            else:
                print("You've entered wrong account number, please try again!!!!")
    elif choice_bank == 2:
        print("==========================================")
        print("       WELCOME TO AXIS BANK")
        print("==========================================")
        print("******************************************")
        print("*         1.Create Account               *\n*         2.Login                        *\n*         3.Terms & Conditions           *")
        print("******************************************")
        choice_option = int(input("Please enter your choice : "))
        if choice_option == 3:
            random_paragraph = generate_random_paragraph()
            print(random_paragraph)
        elif choice_option == 1:
            name = input("Please enter your full name: ")
            day = input("Enter the day of birth (e.g., 01): ")
            month = input("Enter the month of birth (e.g., 05): ")
            year = input("Enter the year of birth (e.g., 1990): ")
            age = (input("Please enter your age: "))
            phone = (input("please enter your mobile number: "))
            address = input("Please enter your current address: ")
            random_account_number = generate_account_number()
            copy_accountnumber = random_account_number
            pin = generate_6_digit_pin()
            copy_pin = pin
            date_of_birth = f"{year}-{month}-{day}"
            f = open(name + "ab" + '.txt', 'w')
            f.write("Name: " + name + '\n')
            f.write("Date of Birth: " + date_of_birth + '\n')
            f.write("Age: " + age + '\n')
            f.write("Mobile Number: " + phone + '\n')
            f.write("Adrress: " + address + '\n')
            f.write("Account Number: " + random_account_number + '\n')
            f.write("Generated PIN: " + pin + '\n')
            f.write("Bank balance: " + balanceAb)
            f.close()
            print("Your account has been successfully created!!!")
            file_path = name + "ab" + ".txt"
            line_number = 6
            result = read_specific_line(file_path, line_number)
            print(result)
            file_path = name + "ab" + ".txt"
            line_number = 7
            result_pin = read_specific_line(file_path, line_number)
            print(result_pin)
        elif choice_option == 2:
            login_name = input("Please enter your full name: ")
            login_accountNumber = input("Please enter your account number: ")
            file_path = login_name + "ab" + ".txt"
            line_number = 6
            result = read_specific_line(file_path, line_number)
            result_account_number = result.strip().split(": ")[1]
            if result_account_number == str(login_accountNumber):
                print("******************************************")
                print("*         1.View Balance                 *\n*         2.Withdraw Money               *\n*         3.Deposit Money                *\n*         4.Edit Account Details         *\n*         5.Change Pin                   *\n*         6.Transfer                     *\n*         7.View Profile                 *\n*         0.Exit                         *")
                print("******************************************")
                choice_login_option = 6
                while choice_login_option != 0:
                    choice_login_option = int(
                        input("Please enter your choice : "))
                    if choice_login_option == 1:
                        name = input("Please enter your name: ")
                        file_path = name + "ab" + ".txt"
                        line_number = 8
                        balanceAb = extract_digits_from_line(
                            file_path, line_number)
                        print("Your current balance is: ", balanceAb)
                        print()
                    elif choice_login_option == 2:
                        userTypedPin = input(
                            "Please enter the pin number: ")
                        if userTypedPin == copy_pin:
                            withdraw_name = input(
                                "Please enter your name: ")
                            amount_withdraw = int(
                                input("Please enter the amount you want to withdraw: "))
                            balanceAb = int(balanceAb) - amount_withdraw
                            print("Your current balance is ", balanceAb)
                            balanceAb = str(balanceAb)
                            file_path = withdraw_name + "ab" + ".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: " + balanceAb
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                            print()
                    elif choice_login_option == 3:
                        deposit_name = input("Please enter your name: ")
                        amount_deposit = int(
                            input("Please enter the amount you want to deposit: "))
                        balanceAb = int(balanceAb) + amount_deposit
                        print("Your current balance is ", balanceAb)
                        balanceAb = str(balanceAb)
                        copy_balance = balanceAb
                        file_path = deposit_name + "ab" + ".txt"
                        line_number_to_modify = 8
                        new_content_for_line = "Bank balance: " + balanceAb
                        write_to_specific_line(
                            file_path, line_number_to_modify, new_content_for_line)
                        print()
                    elif choice_login_option == 4:
                        previous_name = input(
                            "Please enter your full name which is already registered: ")
                        day = input("Enter the day of birth (e.g., 01): ")
                        month = input("Enter the month of birth (e.g., 05): ")
                        year = input("Enter the year of birth (e.g., 1990): ")
                        age = (input("Please enter your age: "))
                        phone = (input("please enter your mobile number: "))
                        address = input(
                            "Please enter your current address: ")
                        name = input("Please enter your full name: ")
                        random_account_number = generate_account_number()
                        date_of_birth = f"{year}-{month}-{day}"
                        f = open(previous_name + "ab" + '.txt', 'w')
                        os.rename(previous_name + "ab" +
                                  '.txt', name + "ab" + ".txt")
                        f.write("Name: " + name + '\n')
                        f.write("Date of Birth: " + date_of_birth + '\n')
                        f.write("Age: " + age + '\n')
                        f.write("Mobile Number: " + phone + '\n')
                        f.write("Adrress: " + address + '\n')
                        f.write("Account Number: " +
                                copy_accountnumber + '\n')
                        f.write("Generated PIN:" + copy_pin + '\n')
                        f.write("Bank balance: " + balanceAb)
                        f.close()
                        print("Your account has been successfully updated!!!")
                        print()
                    elif choice_login_option == 5:
                        pin_name = input("Please enter your name: ")
                        change_pin = input(
                            "Please enter the current pin number: ")
                        if change_pin == copy_pin:
                            pin = generate_6_digit_pin()
                            copy_pin = pin
                            print("Your new pin number is: ", copy_pin)
                            print()
                            file_path = name + "ab" + ".txt"
                            line_number_to_modify = 7
                            new_content_for_line = "Generated PIN:" + copy_pin + '\n'
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                    elif choice_login_option == 6:
                        name = input("Please enter your full name: ")
                        transfer_name = input(
                            "Please enter the name of the user to whom you want to transfer: ")
                        print_box("TRANSFER DETAILS")
                        print(
                            f"Sender: {name}")
                        print(
                            f"Recipient: {transfer_name}")
                        print(
                            "1. State Bank of India\n2. Axis Bank\n3. Union Bank")
                        transfer_choice = int(
                            input("Please choose the bank to which you want to transfer: "))
                        if transfer_choice == 1:
                            transfer_money = int(
                                input("Please enter the amount you want to transfer: "))
                            file_path = name + "ab" + ".txt"
                            line_number = 8
                            copy_balance = extract_digits_from_line(
                                file_path, line_number)
                            copy_balance = int(copy_balance) - transfer_money
                            print_box(
                                f"Amount of Rs.{transfer_money} transferred successfully!!!")
                            print(
                                f"{name}'s current balance is Rs.{copy_balance}")
                            print()
                            copy_balance = str(copy_balance)
                            file_path = name + "ab" + ".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: " + copy_balance
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                            print()
                            file_path = transfer_name + "sbi" + ".txt"
                            line_number = 8
                            balance_transfer = extract_digits_from_line(
                                file_path, line_number)
                            balance_transfer = int(
                                balance_transfer) + transfer_money
                            balance_transfer = str(balance_transfer)
                            file_path = transfer_name + "sbi" + ".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: " + balance_transfer
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                        elif transfer_choice == 2:
                            transfer_money = int(
                                input("Please enter the amount you want to transfer: "))
                            file_path = name + "ab" + ".txt"
                            line_number = 8
                            copy_balance = extract_digits_from_line(
                                file_path, line_number)
                            copy_balance = int(copy_balance) - transfer_money
                            print_box(
                                f"Amount of Rs.{transfer_money} transferred successfully!!!")
                            print(
                                f"{name}'s current balance is Rs.{copy_balance}")
                            print()
                            file_path = name + "ab" + ".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: " + copy_balance
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                            print()
                            file_path = transfer_name + "ab" + ".txt"
                            line_number = 8
                            balance_transfer = extract_digits_from_line(
                                file_path, line_number)
                            balance_transfer = int(
                                balance_transfer) + transfer_money
                            balance_transfer = str(balance_transfer)
                            file_path = transfer_name + "ab" + ".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: " + balance_transfer
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                        elif transfer_choice == 3:
                            transfer_money = int(
                                input("Please enter the amount you want to transfer: "))
                            file_path = name + "ab" + ".txt"
                            line_number = 8
                            copy_balance = extract_digits_from_line(
                                file_path, line_number)
                            copy_balance = int(copy_balance) - transfer_money
                            print_box(
                                f"Amount of Rs.{transfer_money} transferred successfully!!!")
                            print(
                                f"{name}'s current balance is Rs.{copy_balance}")
                            print()
                            copy_balance = str(copy_balance)
                            file_path = name + "ab" + ".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: " + copy_balance
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                            print()
                            file_path = transfer_name + "ub" + ".txt"
                            line_number = 8
                            balance_transfer = extract_digits_from_line(
                                file_path, line_number)
                            balance_transfer = int(
                                balance_transfer) + transfer_money
                            balance_transfer = str(balance_transfer)
                            file_path = transfer_name + "ub" + ".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: " + balance_transfer
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                    elif choice_login_option == 7:
                        name = input("Please enter your name: ")
                        file_path = name+"ab"+".txt"
                        file_contents = read_entire_file(file_path)
                        if file_contents:
                            print_box("Account Details:")
                            print(file_contents)
            else:
                print("You've entered wrong account number, please try again!!!!")
    elif choice_bank == 3:
        print("==========================================")
        print("        WELCOME TO UNION BANK")
        print("==========================================")
        print("******************************************")
        print("*         1.Create Account               *\n*         2.Login                        *\n*         3.Terms & Conditions           *")
        print("******************************************")
        choice_option = int(input("Please enter your choice : "))
        if choice_option == 3:
            random_paragraph = generate_random_paragraph()
            print(random_paragraph)
        elif choice_option == 1:
            name = input("Please enter your full name: ")
            day = input("Enter the day of birth (e.g., 01): ")
            month = input("Enter the month of birth (e.g., 05): ")
            year = input("Enter the year of birth (e.g., 1990): ")
            age = (input("Please enter your age: "))
            phone = (input("please enter your mobile number: "))
            address = input("Please enter your current address: ")
            random_account_number = generate_account_number()
            copy_accountnumber = random_account_number
            pin = generate_6_digit_pin()
            copy_pin = pin
            date_of_birth = f"{year}-{month}-{day}"
            f = open(name+"ub"+'.txt', 'w')
            f.write("Name: "+name+'\n')
            f.write("Date of Birth: " + date_of_birth+'\n')
            f.write("Age: "+age+'\n')
            f.write("Mobile Number: "+phone+'\n')
            f.write("Adrress: "+address+'\n')
            f.write("Account Number: "+random_account_number+'\n')
            f.write("Generated PIN: " + pin+'\n')
            f.write("Bank balance: "+balanceUb)
            f.close()
            print("Your account has been successfully created!!!")
            file_path = name+"ub"+".txt"
            line_number = 6
            result = read_specific_line(file_path, line_number)
            print(result)
            file_path = name+"ub"+".txt"
            line_number = 7
            result_pin = read_specific_line(file_path, line_number)
            print(result_pin)
        elif choice_option == 2:
            login_name = input("Please enter your full name: ")
            login_accountNumber = input("Please enter your account number: ")
            file_path = login_name+"ub"+".txt"
            line_number = 6
            result = read_specific_line(file_path, line_number)
            result_account_number = result.strip().split(": ")[1]
            if result_account_number == str(login_accountNumber):
                print("******************************************")
                print("*         1.View Balance                 *\n*         2.Withdraw Money               *\n*         3.Deposit Money                *\n*         4.Edit Account Details         *\n*         5.Change Pin                   *\n*         6.Transfer                     *\n*         7.View Profile                 *\n*         0.Exit                         *")
                print("******************************************")
                choice_login_option = 6
                while choice_login_option != 0:
                    choice_login_option = int(
                        input("Please enter your choice : "))
                    if choice_login_option == 1:
                        name = input("Please enter your name: ")
                        file_path = name+"ub"+".txt"
                        line_number = 8
                        balanceUb = extract_digits_from_line(
                            file_path, line_number)
                        print("Your current balance is: ", balanceUb)
                        print()
                    elif choice_login_option == 2:
                        userTypedPin = input("Please enter the pin number: ")
                        if userTypedPin == copy_pin:
                            withdraw_name = input("Please enter your name: ")
                            amount_withdraw = int(
                                input("Please enter the amount you want to withdraw: "))
                            balanceUb = int(balanceUb)-amount_withdraw
                            print("Your current balance is ", balanceUb)
                            balanceUb = str(balanceUb)
                            file_path = withdraw_name+"ub"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+balanceUb
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)

                            print()
                    elif choice_login_option == 3:
                        deposit_name = input("Please enter your name: ")
                        amount_deposit = int(
                            input("Please enter the amount you want to deposit: "))
                        balanceUb = int(balanceUb)+amount_deposit
                        print("Your current balance is ", balanceUb)
                        balanceUb = str(balanceUb)
                        copy_balance = balanceUb
                        file_path = deposit_name+"ub"+".txt"
                        line_number_to_modify = 8
                        new_content_for_line = "Bank balance: "+balanceUb
                        write_to_specific_line(
                            file_path, line_number_to_modify, new_content_for_line)
                        print()
                    elif choice_login_option == 4:
                        previous_name = input(
                            "Please enter your full name which is already registered: ")
                        day = input("Enter the day of birth (e.g., 01): ")
                        month = input("Enter the month of birth (e.g., 05): ")
                        year = input("Enter the year of birth (e.g., 1990): ")
                        age = (input("Please enter your age: "))
                        phone = (input("please enter your mobile number: "))
                        address = input("Please enter your current address: ")
                        name = input("Please enter your full name: ")
                        random_account_number = generate_account_number()
                        date_of_birth = f"{year}-{month}-{day}"
                        f = open(previous_name+"ub"+'.txt', 'w')
                        os.rename(previous_name+"ub" +
                                  '.txt', name+"ub"+".txt")
                        f.write("Name: "+name+'\n')
                        f.write("Date of Birth: " + date_of_birth+'\n')
                        f.write("Age: "+age+'\n')
                        f.write("Mobile Number: "+phone+'\n')
                        f.write("Adrress: "+address+'\n')
                        f.write("Account Number: "+copy_accountnumber+'\n')
                        f.write("Generated PIN:" + copy_pin+'\n')
                        f.write("Bank balance: "+balanceUb)
                        f.close()
                        print("Your account has been successfully updated!!!")
                        print()
                    elif choice_login_option == 5:
                        pin_name = input("Please enter your name: ")
                        change_pin = input(
                            "Please enter the current pin number: ")
                        if change_pin == copy_pin:
                            pin = generate_6_digit_pin()
                            copy_pin = pin
                            print("Your new pin number is: ", copy_pin)
                            print()
                            file_path = name+"ub"+".txt"
                            line_number_to_modify = 7
                            new_content_for_line = "Generated PIN:" + copy_pin+'\n'
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                    elif choice_login_option == 6:
                        name = input("Please enter your full name: ")
                        transfer_name = input(
                            "Please enter the name of the user to whom you want to transfer: ")
                        print_box("TRANSFER DETAILS")
                        print(f"Sender: {name}")
                        print(f"Recipient: {transfer_name}")
                        print("1. State Bank of India\n2. Axis Bank\n3. Union Bank")
                        transfer_choice = int(
                            input("Please choose the bank to which you want to transfer: "))
                        if transfer_choice == 1:
                            transfer_money = int(
                                input("Please enter the amount you want to transfer: "))
                            file_path = name+"ub"+".txt"
                            line_number = 8
                            copy_balance = extract_digits_from_line(
                                file_path, line_number)
                            copy_balance = int(copy_balance)-transfer_money
                            print_box(
                                f"Amount of Rs.{transfer_money} transferred successfully!!!")
                            print(
                                f"{name}'s current balance is Rs.{copy_balance}")
                            print()
                            copy_balance = str(copy_balance)
                            file_path = name+"ub"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+copy_balance
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                            print()
                            file_path = transfer_name+"sbi"+".txt"
                            line_number = 8
                            balance_transfer = extract_digits_from_line(
                                file_path, line_number)
                            balance_transfer = int(
                                balance_transfer)+transfer_money
                            balance_transfer = str(balance_transfer)
                            file_path = transfer_name+"sbi"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+balance_transfer
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                        elif transfer_choice == 2:
                            transfer_money = int(
                                input("Please enter the amount you want to transfer: "))
                            file_path = name+"ub"+".txt"
                            line_number = 8
                            copy_balance = extract_digits_from_line(
                                file_path, line_number)
                            copy_balance = int(copy_balance)-transfer_money
                            print_box(
                                f"Amount of Rs.{transfer_money} transferred successfully!!!")
                            print(
                                f"{name}'s current balance is Rs.{copy_balance}")
                            print()
                            file_path = name+"ub"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+copy_balance
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                            print()
                            file_path = transfer_name+"ab"+".txt"
                            line_number = 8
                            balance_transfer = extract_digits_from_line(
                                file_path, line_number)
                            balance_transfer = int(
                                balance_transfer)+transfer_money
                            balance_transfer = str(balance_transfer)
                            file_path = transfer_name+"ab"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+balance_transfer
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                        elif transfer_choice == 3:
                            transfer_money = int(
                                input("Please enter the amount you want to transfer: "))
                            file_path = name+"ub"+".txt"
                            line_number = 8
                            copy_balance = extract_digits_from_line(
                                file_path, line_number)
                            copy_balance = int(copy_balance)-transfer_money
                            print_box(
                                f"Amount of Rs.{transfer_money} transferred successfully!!!")
                            print(
                                f"{name}'s current balance is Rs.{copy_balance}")
                            print()
                            copy_balance = str(copy_balance)
                            file_path = name+"ub"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+copy_balance
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                            print()
                            file_path = transfer_name+"ub"+".txt"
                            line_number = 8
                            balance_transfer = extract_digits_from_line(
                                file_path, line_number)
                            balance_transfer = int(
                                balance_transfer)+transfer_money
                            balance_transfer = str(balance_transfer)
                            file_path = transfer_name+"ub"+".txt"
                            line_number_to_modify = 8
                            new_content_for_line = "Bank balance: "+balance_transfer
                            write_to_specific_line(
                                file_path, line_number_to_modify, new_content_for_line)
                    elif choice_login_option == 7:
                        name = input("Please enter your name: ")
                        file_path = name+"ub"+".txt"
                        file_contents = read_entire_file(file_path)
                        if file_contents:
                            print_box("Account Details:")
                            print(file_contents)
            else:
                print("You've entered wrong account number, please try again!!!!")
        else:
            print("Invalid choice. Please enter a valid option.")
