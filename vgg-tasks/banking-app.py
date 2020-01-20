#  test data
account = {
    "test@gmail.com": {"firstname": "user", "password": "test123", "balance": 1000.0}
}
#Create a new account
def create_account():
    global firstname
    print("Welcome to Up4naija Bank,\nPlease input your details correctly")
    print("=========================================")
    email = input("Enter your email: ").lower()
    # check if account id already exists
    if ("@" in email) and ("." in email):
        if email in account.keys():
            print("This email already exists.")
            transaction()
        else:
            firstname = input("Enter your firstname: ").lower()
            password = input("Enter your password: ")
# set the balance to $0.0
            balance = 0.0
            account[email] = {"firstname": firstname, "password": password, "balance": balance}
            print("Mr."+ firstname +" Account successfully created, Proceed to make a transaction")
            print("=========================================")
            transaction()
    else:
        print("Email is not valid, Please try again")
        create_account()

def transaction():
#Authenticate users before they carry out transactions on the account
    print("Hello customer!")
    print("                          ")
    email = input("Please verify your email: ").lower()
# check if user exists or not
    if email not in account.keys():
        print("Sorry Account does not exist, Please Create an account now. ")
        create_account()
    else:
        print("Hello "+ firstname )
        password = input("Please enter your password: ")
# check if supplied password matches with the saved password to authenticate user
        if password == account[email]["password"]:
            print(firstname + " you have been authenticated")
            print("=========================================")
# user is authenticated and is shown services available
            print("Please select a transaction type")
            services = input("Press 1: Check Account balance\nPress 2: Withdraw Funds\nPress 3: Desopit Funds\nPress 4: Transfer Funds ")
            print("                                         ")
            if services == "1":
                check_balance(email)

            elif services == "2":
                deposit(email)

            elif services == "3":
                withdraw(email)

            elif services == "4":
                transfer(email)

            else:
                print("This input is not valid, please try again")

        else:
            print("Wrong Password, User not Authorized")
            create_account()


def check_balance(email):
    # query data structure to get current user balance
    balance = account[email]["balance"]
    print("Your balance is ", balance)
    print("===============================")
    print("Thank you for banking with us, " + firstname +".")
    continue_banking = input("Would you like to perform another transaction, Y/N: ").lower()
    if continue_banking == "y":
        transaction()
    elif continue_banking == "n":
        print("Thank you for banking with us, " + firstname +".")
        quit()
    else:
        print("Invalid input")
        print("===============================")
        print(continue_banking)

#Transfer funds
def transfer(email):
    recipient = input("Please enter the beneficiary's email: ").lower()
    if recipient not in account.keys():
        print("Beneficiary account does not exist, Please try again")
        transfer(email)
    transfer_amount = input("Please enter the amount to transfer: ")
    while True:
        try:
            actual_amount = float(transfer_amount)
            if actual_amount > 0.0:
                break
            else:
                print("Invalid amount, please enter figures only")
                transfer_amount = input("Please enter the amount to transfer")
        except ValueError:
            print("Invalid amount, please enter figures only")
            transfer_amount = input("Please enter the amount to transfer")
    current_balance = account[email]["balance"]
    # check if there is sufficient balance for the transaction
    if current_balance < actual_amount:
        print("Insufficient funds, your current balance is", current_balance)
        print("Would you make a DEPOSIT now? Yes or No")
        option = input()
        if option.lower() == "yes":
            deposit(email)
        elif option.lower() == "no":
            print("===============================")
            print("Thank you for banking with us")
            quit()
        else:
            print("Invalid selection")
    else:
        account[email]["balance"] = current_balance - actual_amount
        new_balance = account[email]["balance"]
        recipient_balance = account[recipient]["balance"]
        account[recipient]["balance"] = recipient_balance + actual_amount
        print("You have transferred", actual_amount, "to", recipient, "Your new balance is ", new_balance)
        print("===============================")
        print("Thank you for accounting with us")
        print("===============================")
        continue_banking = input("Would you like to perform another transaction, Y/N: ").lower()
    if continue_banking == "y":
        transaction()
    elif continue_banking == "n":
        print("Thank you for banking with Us.")
        quit()
    else:
        print("Invalid input")
        print("===============================")
        print(continue_banking)

def deposit(email):
    #Deposit funds
    amount = input("Please Enter an amount you want to deposit: ")
    while True:
        try:
            actual_amount = float(amount)
            if actual_amount > 0.0:
                break
            else:
                print("Invalid amount, please enter figures only")
                amount = input("Please Enter an amount you want to deposit")
        except ValueError:
            print("Invalid amount, please enter figures only")
            amount = input("Please Enter an amount you want to deposit")
    current_balance = account[email]["balance"]
    account[email]["balance"] = current_balance + actual_amount
    new_balance = account[email]["balance"]
    print("You have deposited ", actual_amount, "Your new balance is ", new_balance)
    print("===============================")
    print("Thank you for banking with us")
    continue_banking = input("Would you like to perform another transaction, Y/N: ").lower()
    if continue_banking == "y":
        transaction()
    elif continue_banking == "n":
        print("Thank you for banking with Us.")
        quit()
    else:
        print("Invalid input")
        print("===============================")
        print(continue_banking)

#Withdraw funds
def withdraw(email):
    withdrawal_amount = input("Please enter an amount to withdraw: ")
    # check if there is sufficient balance for the transaction
    while True:
        try:
            valid_withdrawal_amount = float(withdrawal_amount)
            if valid_withdrawal_amount > 0.0:
                break
            else:
                print("Invalid amount, please fund your account.")
                withdrawal_amount = input("Please enter an amount to withdraw")
        except ValueError:
            print("Invalid amount, please enter figures only")
            withdrawal_amount = input("Please enter an amount to withdraw")
    current_balance = account[email]["balance"]
    if current_balance < valid_withdrawal_amount:
        print("Insufficient funds, your current balance is", current_balance)
        deposit_now = input("Would you make a DEPOSIT now? Y or N: ")
        if deposit_now.lower() == "y":
            deposit(email)
        elif deposit_now.lower() == "n":
            print("===============================")
            print("Thank you for banking with us")
            quit()
        else:
            print("Invalid selection")
    else:
        new_balance  = current_balance - valid_withdrawal_amount
        print("You have withdrawn", withdrawal_amount, "Your new balance is ", new_balance)
        print("===============================")
        print("Thank you for banking with us")
        continue_banking = input("Would you like to perform another transaction, Y/N: ").lower()
    if continue_banking == "y":
        transaction()
    elif continue_banking == "n":
        print("Thank you for banking with Us.")
        quit()
    else:
        print("Invalid input")
        print("===============================")
        print(continue_banking)
Bank = input("Press 1: Create Account \nPress 2: Transaction \nPress q to quit ")
while True:
    if Bank == "1" or Bank == "2" or Bank == "q":
        break
    else:
        print("Invalid selection")
        Bank = input("Press 1: Create Account \nPress 2: Transaction \nPress q to quit ")
if Bank == "1":
    create_account()
elif Bank == "2":
    transaction()
elif Bank == "q":
    print("Thank you, Goodbye!!!")
    quit()
