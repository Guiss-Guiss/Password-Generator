import string
import random
import time

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()-=_+?;:<>,.[]{}/`~")


def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    current_time = int(time.time())
    random.seed(current_time)
    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)
    option = input("Do you want to generate another password? (y/n): ")
    if option == "y":
        generate_password()
    elif option == "n":
        print("Program ended")
        quit()
    else:
        print("Invalid input, please input y or n")
        quit()

option = input("Do you want to generate a password? (y/n): ")

if option == "y":
    generate_password()

elif option == "n":
    print("Program ended")
    quit()
else:
    print("Invalid input, please input y or n")
    quit()
