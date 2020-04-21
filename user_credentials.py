#!/usr/bin/env python3

import random
import string
import pyperclip

class user:
    '''
    class that generates instances of user
    '''

    #First test

    users_list = []# Empty list where users will be saved

    def _init_(self, first_name, last_name, password):
        '''
        _init_method that helps us define properties of our objects
        
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password


        def save_user(self):

            '''
            save_user method saves user objects into user_list
            '''

            user.user_list.append(self)


            @classmethod
            def check_user(cls, first_name, password):
                '''
                Method that checks the name and the password entered match entries in the user list.
                '''

                current_user = ''
                for user in User.users_list:
                    if(user.first_name == first_name and user.password == password):
                        current_user = user.first_name
                return current_user 


       class Credentials:
           '''
           Class that generates instances of account credentials, generate passwords and save informaton
           '''

           self.user_name = user_name
           self.site_name = site_name
           self.account_name = account_name
           self.password = password


        def save_credential(self):
            '''
            save_credentials method that saves credential objects in the credentials_list
            '''

            Credentials.credentials_list.append(self)


            