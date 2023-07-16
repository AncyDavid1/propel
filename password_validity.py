import re

def check_password(password):
    if len(password) < 6 or len(password) > 12:
        print("password should be min 6 and max 12")

    if not re.search("[a-z]", password):
        print("password should contain atleadt one lower case")

    if not re.search("[0-9]", password):
        print("password should contain atleast one number")

    if not re.search("[A-Z]", password):
        print("password should contain atleadt one upper case")

    if not re.search("[$#@]", password):
        print("password should contain atleadt one special character")
    else:
        print("valid password")
my_pwd = input("Enter the password: ")
check_password(my_pwd)
