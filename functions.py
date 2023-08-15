import random
import sqlite3


charactersDatabase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z', "!", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z', '?', '.', '>', '<', ',', ':', ';', '[', ']', '}', '{', '}', '-', '_', '=', '+', '*', '/', '!', '@', '#', '$', '%', '^&', '*']


#CREATING DATABASE
connection = sqlite3.connect('passwordDatabase')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS password (service TEXT, password TEXT)""")
connection.commit()


def starter_function(): # STARTS THE SCRIPT
    selection = input("A. Create password or B. Check already existing password? C. Clear Database\n").lower()
    if selection == "a":
        password = generate_password(20)
        print(password)
        save_password(password)
    
    elif selection == "b":
        service = input("What is the service?\n").lower()
        try:
            cursor.execute("""SELECT * FROM password WHERE service = '{}' """.format(service))
            result = cursor.fetchone()
            print(f"Password saved for {service} is {result[1]}")
        except TypeError:
            print("No passwords saved for selected service.")
    
    elif selection == "c":
        cursor.execute("""DROP table password""")
        connection.commit()
        cursor.execute("""CREATE TABLE IF NOT EXISTS password (service TEXT, password TEXT)""")
        connection.commit()
        print("Passwords erased.")
    
    else:
        starter_function()


def generate_password(passwordLenght: int): # GENERATES THE PASSWORD
    amountOfCharacters = int(passwordLenght)
    generatedPassword = []
    while len(generatedPassword) < amountOfCharacters:
        generatedPassword.append(charactersDatabase[random.randint(0, (len(charactersDatabase)-1))])
    
    outcome = ""
    for character in generatedPassword:
        outcome = outcome + str(character)
    return outcome


def save_password(passwordToBeSaved): # SAVES THE PASSWORD
    selection = input("Want to save the password in the database?\ny/n\n").lower()
    
    if selection == "y":
        service = input("What services is using this passowrd?\n").lower()
        cursor.execute("""INSERT INTO password VALUES('{}', '{}')""".format(service, passwordToBeSaved))
        connection.commit()
        print(f"Password sucessfully saved for {service}")
    
    elif selection == "n":
        print("Password not saved")
    
    else:
        save_password(passwordToBeSaved)
