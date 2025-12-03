#Imports

import random
import time

#Player Introduction

print("Hello Player, Welcome To Computer Cricket! \n")

name = input("Before We Begin, What Is Your Name Player? \n")

print("Hello!", name, "Nice To Meet You! \n")

#Do You Know And How To Play The Game

while True:
    dyk = input("Do You Know How To Play This Game? (Yes/No) \n")

    if dyk.lower() == "yes":
        print("Good Then We Can Begin! \n")
        break
    elif dyk.lower() == "no":

        while True:
            htp = input("Would You Like To Know How To Play This Game? (Yes/No) \n")
            if htp.lower() == "yes":
                print("How To Play")
                break
            elif htp.lower() == "no":
                print("Okay Then Let's Begin Without The How To Play!")
                break
            else:
                print("Invalid Input, Please Try Again! \n")
        break

    else:
        print("Invalid Input, Please Try Again! \n")

#Toss

toss = random.randint(1,2)

while True:
    tossh = input("Heads or Tails? (Head/Tail) \n")

    if tossh.lower() == "head":
        tossh = 1
        break
    elif htp.lower() == "tail":
        tossh = 2
        break
    else:
        print("Invalid Input, Please Try Again! \n")

if tossh == toss:

    print("You Won The Toss! \n")

    while True:
        bob = input("Do You Want To Chose Batting Or Balling? (Bat/Ball) \n")

        if bob.lower() == "bat":
            print("User Chose Batting \n")
            bob = 1
            break
        elif bob.lower() == "ball":
            print("User Chose Balling \n")
            bob = 2
            break
        else:
            print("Invalid Input, Please Try Again! \n")

else:
    print("I Won The Toss \n")

bob = random.randint(1,2)

if bob == 1:
    print("I Am Choosing To Bat \n")
else:
    print("I Am Choosing To Ball \n")

ball = int(input("Computer Threw The Ball, Your Attack? (Chose A Number Between 1 to 6) \n"))

while True:
    ball = int(input("Computer Threw The Ball, Your Attack? (Chose A Number Between 1 to 6) \n"))
    balln = random.randint(1,6)
    if ball == 1 or 2 or 3 or 4 or 5 or 6:
        if ball == balln:
            print("Out!")
            scoreh = scoreh + 1
            break
        else:
            print("Your Scored", ball,"\n")
            scoreh = ball + scoreh
    else:
        print("Invalid Input")



while True:
    cv = random.randint(1,6)
    hv = input("")


print("Worked! \n")