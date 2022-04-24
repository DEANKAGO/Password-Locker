from psutil import users
from requests import delete


class User:
  userslist=[]
  def __init__(self, firstname, lastname, username,password):
    self.firstname = firstname
    self.lastname = lastname
    self.username = username
    self.password = password

  def save_user(self):
    User.userslist.append(self)

  def delete_user(self):
    User.userslist.remove(self)
  @classmethod

  def show_users(cls):
    return cls.userslist
  @classmethod

  def find_by_number(cls,number):
    for user in cls.userslist:
      if user.password == number:
        return user
  @classmethod

  def user_exist(cls,number):
    for user in cls.userslist:
      if user.username == number:
        return True
        return False            
