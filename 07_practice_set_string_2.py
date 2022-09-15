#letter template
# letter=''' Dear <|Name|>
# you are selected!.

# <|Date|>

# '''
# name=input("enter your Name\n")
# date=input("enter Date\n")
# letter=letter.replace('<|Name|>',name)
# letter=letter.replace('<|Date|>',date)
# print(letter)


#write a program to detect double space in the string
name="pranjal  chaubey"
print(name.find("  "))       # if double space exists then it will give index of the double soace if it not find then it will return -1.