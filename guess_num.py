import random
target=random.randint(0,100)
while True:
    userchoice=input("Guess the target or Quit-(Q):")
    if(userchoice == "Q"):
         print("...GAME OVER...")
         break
    userchoice=int(userchoice)
    if(userchoice==target):
            print("Sucess: Correct Guess")
            print("..Well Played..")
            break
    elif(userchoice < target):
            print("The num you entered is smaller to target .Take a bigger guess")
    else:
            print("The num you entered is bigger to target .Take a smaller guess")
