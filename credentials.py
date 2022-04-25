from requests import delete


class Credentials:
    """
    class for new credentials
    """

    accounts = []

    def __init__(self, accountname, accountusername, accountpassword):
        """
        method for defining properties
        """
        self.accountname = accountname
        self.accountusername = accountusername
        self.accountpassword = accountpassword

    def save_account(self):
        """
        method that saves new user information
        """
        Credentials.accounts.append(self)

    def delete_account(self):
        """
        method that deletes a user account
        """
        Credentials.accounts.remove(self)

    @classmethod
    def show_accounts(cls):
        """
        method that shows accounts
        """
        for account in cls.accounts:
            return cls.accounts

    @classmethod
    def find_by_number(cls, number):
        """
        method that returns a user
        """
        for account in cls.accounts:
            if account.accountusername == number:
                return account
