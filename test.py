import unittest
from user import User
from credentials import Credentials


class Testuser(unittest.TestCase):
    """
    it defines how a user class behaves
    Args: unitest.Testcase: helps in creating test cases 
    """

    def setUp(self):
        """
        method that runs before each test case
        """
        self.new_user = User("Martin", "Muchai", "Kago", "python3")

    def test_init(self):
        """
        tests if an objest has been initialized properly
        """
        self.assertEqual(self.new_user.username, "Kago")
        self.assertEqual(self.new_user.password, "python3")

    def test_save_user(self):
        """
        tests if user is saved in user list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.userslist), 2)

    def test_delete_user(self):
        """
        tests if a user can be deleted
        """
        self.new_user.save_user()
        test_user = User("Martin", "Muchai", "Kago", "python3")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.userslist), 1)


if __name__ == "__main__":
    unittest.main()
