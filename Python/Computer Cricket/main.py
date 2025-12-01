import random
import time

time.sleep(1)

print("Hello Player, Welcome To Computer Cricket! \n")

name = input("Before We Begin, What Is Your Name Player? \n")

print("Hello!", name, "Nice To Meet You! \n")

while True:
    dyk = input("Do You Know How To Play This Game? (Yes/No) \n")

    if dyk.lower() == "yes":

        print("Good Then We Can Begin! \n")
        break

    elif dyk.lower() == "no":

        while True:
            htp = input("Would You Like To Know How To Play This Game? (Yes/No)\n")

            if htp.lower() == "yes":
                print("How To Play")
                break
            elif htp.lower() == "no":
                print("Okay Then Let's Begin Without The How To Play!")
                break
            else:
                print("Wrong Input Please Try Again! \n")

        break

    else:
        print("Wrong Input, Please Try Again! \n")

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
        print("Wrong Input, Please Try Again. \n")

if tossh == toss:
    print("You won the toss!")
else:
    print("I won the toss")

if tossh == toss:
    print()
else:
    print()



print("Worked! \n")