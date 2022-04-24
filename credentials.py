from requests import delete


class Credentials:
  accounts = []
  def __init__(self,accountname, accountusername, accountpassword):
    self.accountname = accountname
    self.accountusername = accountusername
    self.accountpassword = accountpassword

  def save_contact(self):
    Credentials.accounts.append(self)  

  def delete_account(self):
      