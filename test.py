import unittest
import pyperclip
from user import User, Credential

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user behaviors.
    Args:
        unittest.TestCase: helps in creating test cases
    '''
    def SetUp(self):
        '''
        Function to create a user account before each test
        '''
        self.new_user = User('Jacinta', 'At\'ek\'a' 'pswd540')