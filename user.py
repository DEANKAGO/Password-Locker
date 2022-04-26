from psutil import users
from requests import delete



class User:
  """
  a class for creating new users
  """
  userslist=[]
  def __init__(self, firstname, lastname, username,password):
    """
    method for defining properties
    """
    self.firstname = firstname
    self.lastname = lastname
    self.username = username
    self.password = password

  def save_user(self, user):
    """
    method for saving user information
    """
    User.userslist.append(user)

  def delete_user(self):
    """
    method for deleting a user
    """
    User.userslist.remove(self)
  @classmethod
  def show_users(cls):
    """
    method that shows userlist information"""
    return cls.userslist
  @classmethod
  def find_by_number(cls,number):
    for user in cls.userslist:
      if user.password == number:
        return user
  @classmethod
  def user_exist(cls,number):
    for user in cls.userslist:
      if user.userslist == number:
        return True
        return False            
