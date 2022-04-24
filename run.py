from user import User
from credentials import Credentials

def create_user(firstname,lastname, username, userpassword):
  newuser = User(firstname,lastname,username, userpassword)
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
               