
#snake water gun game
import random 
def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
      if you=='w':
        return False
      elif you=='g':
        return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True    
    elif comp ==  'g':
        if you=='s':
            return False
        elif you=="w":
            return True             

print("Comp TUrn:Snake(s) Water(w) or Gun(g) ")
randNo=random.randint(1,3) 

if randNo==1:
    com='s'
elif randNo==2:
    comp='w'  
elif randNo==3:
    comp='g'       
you=input("your TUrn:Snake(s) Water(w) or Gun(g) ")

a=game(comp,you)
if a==None:
    print("Tie")
elif a:
    print('you win!')
else:
    print("you Loose")        


