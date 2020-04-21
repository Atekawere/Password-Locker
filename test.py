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

        def test_save_user(self):
            '''
            Test to check if the new users info is saved into the users list
            '''
            self.new_user.save_user()
            self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases for the credentials class behaviors.
    Args:
        unittest.TestCase: helps in creating test cases
    '''
        def test_check_user(self):
            '''
            Function to test whether the login in function check_user works as expected
            '''
            self.new_user = User('Jacinta', 'At\'ek\'a', 'pswd540')
            self.new_user.save_user()
            user2 = User('Mary', 'At\'ek\'a', 'pswd540')
            user2.save_user()

            for user in User.users_list:
                if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		    return current_user

            self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

            def setUp(self):
                '''
                Function to create an account's credentials before each test
                '''
                self.new_credential = Credential('Jacinta', 'Facebook', 'pswd540')

            def test__init__(self): 
                '''
                Test to if check the initialization/creation of credential instances is properly done
                ''' 
                self.assertEqual(self.new_credential.user_name, 'Jacinta')
                self.assertEqual(self.new_credential.site_name, 'Facebook')
                self.assertEqual(self.new_credential.account_name, 'Jacintaatek')
                self.assertEqual(self.new_credential.password, 'pswd540')

            def test_save_credentials(self):
                '''
                Test to check if the new credential info is saved into the credentials list
                '''
                self.new_credential.save_credentials()
                twitter = credential('Mary','Twitter','Jacintaatek','pswd540')
                twitter.save_credentials()
                self.assertEqual(len(Credential.credentials_list),2)

            def tearDown(self):
                
