from gettext import find
from random import randint
from secrets import choice
import string
from user import User
from credentials import Credentials


def create_user(firstname, lastname, username, userpassword):
    newuser = User(firstname, lastname, username, userpassword)
    return newuser


def save_user(user):
    user.save_user()


def delete_user(user):
    user.delete_user()


def find_user(number):
    return User.find_by_number(number)


def show_users():
    return User.show_users()


def create_account(accountname, acccountusername, accountpassword):
    newaccount = Credentials(accountname, acccountusername, accountpassword)
    return newaccount


def save_account(user):
    user.save_account()


def delete_account(user):
    user.delete_account()


def find_account(number):
    return Credentials.find_by_number(number)


def show_accounts():
    return Credentials.show_accounts()


def main():
    while True:
        print("Welcome to password Locker write SU or LG to start")
        print("SU or LG")
        option = input()
        if option == "SU":
            print("Create Account")
            print("Enter First Name")
            firstname = input()
            print("Enter Last Name")
            lastname = input()
            print("Set Username")
            username = input()
            print("Set Password")
            userpassword = input()
            save_user(create_user(firstname, lastname, username, userpassword))
            print("Account created successfully")
            print(
                f"Name:{firstname} {lastname} \nUsername: {username} \nPassword: {userpassword}")
            print("\nFill in your details to LogIn")
            print("\n \n")

        elif option == "LG":
            print("username")
            loginUsername = input()
            print("password")
            loginPassword = input()
            if find_user(loginPassword):
                print("\n")
                print("Log in successful")
                print("\n")
                print("You can create multiple accounts (AC) and also view them (VC)")
                print("AC or VC")
                choose = input()
                print("\n")
                accountusername = loginUsername
                if choose == "AC":
                    print("Add your Account")
                    accountusername = accountusername
                    print("Account Name")
                    accountname = input()
                    print("Account Username")
                    accountusername = input()
                    print("\n")
                    print("generate password (G) or create new password(C)")
                    decision = input()
                    if decision == "G":
                        characters = string.ascii_letters + string.digits
                        accountpassword = "".join(
                            choice(characters) for x in range(randint(6, 16)))
                        print(f"password: {accountpassword}")
                    elif decision == "C":
                        print("Enter Password")
                        accountpassword = input()
                    else:
                        print("Please put in valid information")
                    save_account(create_account(
                        accountname, accountusername, accountpassword))
                    print("\n")
                    print(
                        f"Account Name: {accountname} \nUsername: {accountusername}  \nPassword: {accountpassword}")
                    print("\n")
                elif choose == "VC":
                    if find_account(accountusername):
                        print("Here are your created accounts")
                        for user in show_accounts():
                            print(
                                f"Account: {user.accountname} \nUsername: {user.accountusername} \nPassword: {user.accountpassword} \n")
                    else:
                        print("Invalid Information!")
                else:
                    print("Try Again")
                    print("\n")
            else:
                print("Incorect Information Plese try again")
                print("\n")
        else:
            print("Please choose a valid option")
            print("\n")


if __name__ == '__main__':
    main()
