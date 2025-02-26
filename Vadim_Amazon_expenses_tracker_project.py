# Task 1
# The program should accept username and password
# from the terminal for registration

# Username = input("Please enter your Username: ")
# Password = input("Please enter your Password: ")


# # Task 2

# # if len(Password) >= 6 and len(Password) <= 20:
# #     print("Password Ok")
# # elif len(Password) < 6:
# #     print("Passwort too short")
# # elif len(Password) > 20:
# #     print("Password too long")

# def Password_check(Password):
#     if len(Password) < 6:
#         print("Passwort too short, length should be at least 6")
        
#     if len(Password) > 20:
#         print("Password too long length should be not be greater than 20")

#     if any(char.isdigit() for char in Password):
#         pass
#     else:
#         print('Password should have at least one numeral')
#         exit()
#     if any(char.isupper() for char in Password):
#         pass
#     else:
#         print('Password should have at least one uppercase letter')
#         exit()
#     if any(char.islower() for char in Password):
#         pass
#     else:
#         print('Password should have at least one uppercase letter')
#         exit()
#     if any(char in Special_Symbol for char in Password):
#         pass
#     else:
#         print('Password should have at least one of the special symbols e.g. $@#')
#         exit()

# # Task 3   
# Tel = input("Please enter your phone number: ")
# Phone = list(Tel)
# def Phone_check(Phone):
#     if len(Tel) < 14:
#         print("It should be a valid german mobile number")
#     if len(Tel) > 14:
#         print("It should be a valid german mobile number")

#     if Phone[0] == "+":
#         pass
#     elif Phone[1] == "4":
#         pass
#     elif Phone[2] == "9":
#         pass
#     else:
#         print("It should be a valid german mobile number")

# # Task 4
# print('Great, you have successfully created your account, now login please.')

# count = 0
# x = 5
# Uname = input("Please enter your Username: ")
# Pword = input("Please enter your Password: ")

# def Login(count, Username, Password):
#     while count < 6:
#         if Uname == Username and Pword == Password:
#             print("The login was successful")
#             break
#         else:
#             print("Invalid Username or Password, try again")
#             count = count + 1
#     print("You have used all the attempts, pleas wait for 5 seconds and try again")
#     time.sleep ( x )

#     Username = input("Please enter your Username: ")
#     Password = input("Please enter your Password: ")
#     if Username == "Vadim" and Password == "1234567":
#         print("The login was successful")
#     else:
#         print("Invalid Username or Password, register again")
#         exit()

# # Task 5

# print('Welcome to the Amazon Expense Tracker!')

# # Task 6
# Password_check(Password)
# Phone_check()
# Login()

# Creat functions: to chek the Password, to check the phone number, to regestrate, and to login...

import time
Special_Symbol=['!','$', '@', '#', '%','?',',','.','+','-','*','/','~','<','>','°','^']
User = {'Anna':{"Password":'Anna2025Anna!',"Phone number":'+4918186503828'},}

def check_Password(password_variable):
    if len(password_variable) >= 6:
        if len(password_variable) <= 20:
            if any(char.isdigit() for char in password_variable):
                if any(char.isupper() for char in password_variable):
                    if any(char.islower() for char in password_variable):
                        if any(char in Special_Symbol for char in password_variable):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def check_Phone(phone_variable):
    if len(phone_variable) == 14:
        if phone_variable[0] == "+":
            if phone_variable[1] == "4":
                if phone_variable[2] == "9":
                    return True             
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def register(name_variable,password_variable,phone_variable):
    if check_Password(password_variable) == True:
        if check_Phone(phone_variable) == True:
            User[name_variable] = {"Password":password_variable,"Phone number":phone_variable}
            return print('Registration successful.')
        else:
            return print('REGISTRATION-ERROR' "\n"
                         'your phone number MUST be:' 
                         '- a valid german mobile number' "\n"
                         '- it must starts with the Country Code' "\n"
                         '- it must has the correct length'
                         'Please try again with a valid phone number.')
            exit()
    else:
        return print('REGISTRATION-ERROR your Password MUST be:' "\n"
                     '- Between 6 an 20 characters long' "\n"
                     '- Should have at least one number' "\n"
                     '- Should have at least one uppercase and one lowercase character' "\n"
                     '- Should have at least one special symbol' "\n"
                     'Please try again with a valid password.')
        exit()

def login(name_variable,password_variable):
    if name_variable in User.keys():
       if password_variable == User[name_variable]["Password"]:
           print('Login successful')
           return True
       else:
           print('Password does not match')
           return False
    else:
        print('Username does not exist')
        return False

# From here on login/regester procedure

print("Welcome to expense tracker")
print("1. Login")
print("2. Register")
option = input("Enter an option:")
count = 0
x = 5

if option == "1":
    while count <= 2:
        username = input("Please enter your Username: ")
        password = input("Please enter your Password: ")
        if login(username,password) == True:
            print('\n')
            print('--> Welcome to the Amazon Expense Tracker!')
            break
        else:
            count = count + 1
    else:
        print("You have used all the attempts to login, pleas wait for 5 seconds and try again")
        time.sleep ( x )            
        username = input("Please enter your Username: ")
        password = input("Please enter your Password: ")
        if login(username,password) == True:
            pass
        else:
            print("Please register again")
            exit()

elif option == "2":
    print('Welcome to procedure of regester! Please choose a username, a password and enter your phone number' '\n'
          'But notice, the requirements for the password are:' '\n'
          '- It should has at least one number.' '\n'
          '- It should has at least one uppercase and one lowercase character.' '\n'
          '- It should has at least one special symbol, e.g. ! $ @ # % ? , . + - * / ~ < > ° ^' '\n'
          '- It should be between 6 to 20 characters long.' '\n'
          'It is as well important that your phone number is a valid german mobile number. So consider the country code as well.')
    print('\n')
    
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    phone_number = input("Please enter your phone number: ")
    
    register(username, password, phone_number)

else:
    exit()