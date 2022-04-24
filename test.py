import unittest
from user import User
from credentials import Credentials

class Testuser(unittest.TestCase):

  def setUp(self):
    self.new_user = User("Martin", "Kago", "Python")

  def test_init(self):
    self.assertEqual(self.new_user.user_name,"Martin")
    self.assertEqual(self.new_user.password, "Python")

  def test_save_user(self):
    self.new_user.save_user()
    self.assertEqual(len(User.user_list),1)

  def test_delete_user(self):
    self.new_contact.save_contact()
    test_user = User("Test", "user", "0712121212", "martokhago@gmail.com")
    test_user.save_user()     

    self.new_user.delete_user()
    self.assertEqual(len(User.user_list),1)

if __name__ == "__main__":
  unittest.main()    
