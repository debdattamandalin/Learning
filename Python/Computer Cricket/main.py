import random
import time

time.sleep(1)
print("Hello player, welcome to computer cricket! \n")

name = input("Before we begin, what is your name player? \n")

print("Hello!", name, "nice to meet you! \n")

while True:
    htp = input("Do you want to know how to play this game? (Yes/No) \n")

    if htp.lower() == "yes":
        print("Cool! \n")
        break
    elif htp.lower() == "no":
        print("You pressed no \n")
        break
    else:
        print("Wrong Input, Please Try Again With (Yes/No). \n")

print("Worked! \n")