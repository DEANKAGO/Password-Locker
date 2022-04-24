import unittest
from user import User
from credentials import Credentials

class Testuser(unittest.TestCase):

  def setUp(self):
    self.new_user = User("Martin", "Kago", "Python")

  def test_init(self):
    self.assertEqual()  