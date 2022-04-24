from psutil import users
from requests import delete


class User:
  userslist=[]
  def __init__(self, firstname, lastname, username,password):
    self.firstname = firstname
    self.lastname = lastname
    self.username = username
    self.password = password

  # def save_user(self):
  #   User.userslist.append(self)

  # def delete_user(self):
  #   User.userslist.remove(self)
  # @classmethod

  # def show_users(cls)  
