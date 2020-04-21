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

        def test__init__(self):
            '''
            Test to if check the initialization/creation of user instances is properly done
            '''
            self.assertEqual(self.new_user.first_name, 'Jacinta')
            self.assertEqual(self.new_user.last-name, 'At\'ek\'a')
            self.assertEqual(self.new_user.password, 'pswd540')

            