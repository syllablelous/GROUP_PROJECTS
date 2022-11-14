# ***   PASSWORD GENERATOR PROGRAM  ***
# The goal of this program is to generate or create passwords that the user can use for their security-related needs. The user is given options
# to choose from in relation to how they want their password to be prepared according to their preferences as offered by the program.
# FINALS Group Project by Russel Jerome G. Rapi, John Kerwin Briñas, and Chrisnald Bartolome of INF224

import random

print("Welcome to the PASSWORD GENERATOR PROGRAM\n")

# LIST OF CHARACTERS
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '@' , '#' , '$', '%', '^', '&', '*', '<', '>', '?', '+', '=']

# DETERMINES THE LENGTH OF THE PASSWORD
length = int(input("How many characters would you like for your password to have? "))

if(length < 16):
    while(length < 16):
        print("For security reasons, it is recommended that you create a password with at least 16 or more characters.\n")
        length = int(input("How many characters would you like for your password to have? "))


# USER PROMPT
print("Do you want a basic password, secure password, or a modified password of your choosing? \n")
choice = str(input("Choose from the options: (BASIC/SECURE/MODIFIED) ")).upper()

password = ""

# BASIC PASSWORD
def basicPassword(length, password, lowercase):
    print("You have chosen: BASIC PASSWORD")
    for i in range(length):
        password = password + random.choice(lowercase)
    print("Your brand new password is:", password, "\n")
    print("We hope you enjoy your new password!\n")


# SECURE PASSWORD
def securePassword(length, password, lowercase, uppercase, numbers, special):
    print("You have chosen: SECURE PASSWORD")
    for i in range(length):
        count = random.choice([0, 1, 2, 3])
    
        if (count == 1):
            password = password + random.choice(uppercase)
        elif (count == 2):
            password = password + random.choice(numbers)
        elif (count == 3):
            password = password + random.choice(special)
        else:
            password = password + random.choice(lowercase)

    print("Your brand new password is:", password, "\n")
    print("We hope you enjoy your new password!\n")


# MODIFIED PASSWORD
def modifiedPassword(length, password, numbers, uppercase, special, lowercase):
    print("You have chosen: MODIFIED PASSWORD\n")
    include_num = str(input("Do you want the password to have numbers? (Y/N) ")).upper()
    include_up = str(input("Do you want the password to include uppercase letters? (Y/N) ")).upper()
    include_spec = str(input("Do you want the password to have special characters? (Y/N) ")).upper()

    count = 0

    for i in range(length):
            
        if(include_num == "N" and include_up == "N" and include_spec == "N"):
            password = password + random.choice(lowercase)
        elif(include_num == "Y" and include_up == "N" and include_spec == "N"):
            count = random.choice([0, 1])
            if (count == 1):
                password = password + random.choice(numbers)
            else:
                password = password + random.choice(lowercase)
        elif(include_num == "Y" and include_up == "Y" and include_spec == "N"):
            count = random.choice([0, 1, 2])
            if (count == 1):
                password = password + random.choice(numbers)
            elif (count == 2):
                password = password + random.choice(uppercase)
            else:
                password = password + random.choice(lowercase)
        elif(include_num == "Y" and include_up == "Y" and include_spec == "Y"):
            count = random.choice([0, 1, 2, 3])
            if (count == 1):
                password = password + random.choice(numbers)
            elif (count == 2):
                password = password + random.choice(uppercase)
            elif (count == 3):
                password = password + random.choice(special)
            else:
                password = password + random.choice(lowercase)
        elif(include_num == "N" and include_up == "Y" and include_spec == "N"):
            count = random.choice([0, 1])
            if (count == 1):
                password = password + random.choice(uppercase)
            else:
                password = password + random.choice(lowercase)
        elif(include_num == "N" and include_up == "Y" and include_spec == "Y"):
            count = random.choice([0, 1, 2])
            if (count == 1):
                password = password + random.choice(uppercase)
            elif (count == 2):
                password = password + random.choice(special)
            else:
                password = password + random.choice(lowercase)
        elif(include_num == "N" and include_up == "N" and include_spec == "Y"):
            count = random.choice([0, 1])
            if (count == 1):
                password = password + random.choice(special)
            else:
                password = password + random.choice(lowercase)
        elif(include_num == "Y" and include_up == "N" and include_spec == "Y"):
            count = random.choice([0, 1, 2])
            if (count == 1):
                password = password + random.choice(numbers)
            elif (count == 2):
                password = password + random.choice(special)
            else:
                password = password + random.choice(lowercase)
        # if the user inputs different characters instead of the noted options, it runs the secured option
        else:
            count = random.choice([0, 1, 2, 3])
            if (count == 1):
                password = password + random.choice(numbers)
            elif (count == 2):
                password = password + random.choice(uppercase)
            elif (count == 3):
                password = password + random.choice(special)
            else:
                password = password + random.choice(lowercase)
        
    print("Your brand new password is:", password, "\n")
    print("We hope you enjoy your new password!\n")

# CHOICES FOR PASSWORD GENERATOR
if(choice == "BASIC"):
    basicPassword(length, password, lowercase)
elif(choice == "SECURE"):
    securePassword(length, password, lowercase, uppercase, numbers, special)
elif(choice == "MODIFIED"):
    modifiedPassword(length, password, numbers, uppercase, special, lowercase)
else:
    print("ERROR: That is not available in our options! Try again.")

# END OF PROGRAM
