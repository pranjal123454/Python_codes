#the perfect guess
import random
randNo=random.randint(1,100)
guesses=0
userGuess=None  #user guess hmesA define 
while(userGuess!=0):
    userGuess=int(input("Enter a number"))
    guesses+=1
    if(userGuess==randNo):
        print("Congo you guess right!")
        print(f"you guessd the number in {guesses}") 
        break
    else:
        if(userGuess>randNo):
         print("you guessed wrong!ENter a smaller no")
        else:
            print("you guessed wrong !Enter a larger number")        
           
with open("hiscore.txt","r") as f:
    hiscore=int(f.read())
if(guesses<hiscore):
    print("YOu have just broken the hi score")    
    with open("hiscore.txt","w") as f:
        f.write(guesses)