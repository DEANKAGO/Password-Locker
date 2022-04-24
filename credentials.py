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
    Credentials.accounts.remove(self)
  @classmethod

  def show_accounts(cls): 
    for account in cls.accounts:
      return cls.accounts 
  @classmethod

  def find_by_number(cls, number):
    for account in cls.accounts:
      if account.accountusername == number:
        return account      
