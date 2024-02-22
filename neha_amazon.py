#Input user name and password and check its validity--------------------------------------------------------------------------------------------------------

import re
import time

def registration():
    username = input("Enter your Username:")
    attempt = 1
    while attempt <= 3 :
        print("Attempt no: ", attempt)
        password = input ("Enter your Password:")
        cond = False
        if len(password)>6 and len(password)<20 and re.search(r'[!@#$%^&*()]', password):
            print("Passes 1st condition")
            for i in password:
                if i.isnumeric():
                    print("Numeric character present")
                    cond = True
            for i in password:
                if i.isupper():
                    print("Uppercase present")
                    cond = True
            for i in password:
                if i.islower():
                    print("Lowercase present")
                    cond = True
                    attempt = 4
                    return username, password
        else:
            print("CHECKING PASSWORD: ", attempt)
            attempt += 1
            return None,None

try:
    username, password = registration()
    if password:
        print("Your login is: ", password )
    else:
        print("Password check failed")
except:
    print("An exception occurred")




"""        if len(password)>6 and len(password)<20 and re.search(r'[!@#$%^&*()]',password) :
            if password.isnumeric() and password.isupper() and password.islower():
                print("Registration successful")
                attempt = 3
                return username, password
        else:
            print("Try again with a valid password")
            attempt +=1
    if attempt > 2 :
        print("Too many attempts")
        print("Wait for 5 seconds...")
        time.sleep(5)
        return None, None

#Input contact number of the user----------------------------------------------------------------------------------------------------------------------------

def cont_info():
    cont_no = input("Enter your Contact number: +49 " )
    if len(cont_no)!= 11 :
        print("Please enter 11 digit number")

#Input login function ----------------------------------------------------------------------------------------------------------------------------------------

def login():
    while attempt < 3 :
        login_username = input ("Enter your Username : ")
        login_password = input ("Enter your Password: " )
        if login_username == username and login_password == password :
            print("Welcome to the Amazon Expense Tracker!")
            return
        else :
            print("Invalid username or password")
            attempt += 1
            print("Wait for 5 seconds...")
            time.sleep(5)

username, password = registration()
if username and password:
    cont_info()
    login()
"""