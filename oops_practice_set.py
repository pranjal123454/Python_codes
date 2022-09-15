#create a class programmer for storing information of few programmers working at microsoft
# class Programmer:
#     company="microsoft"
#     def __init__(self,name,role):
#         self.name=name
#         self.role=role
#     def getinfo(self):
#         print(self.name,self.role)

# harry=Programmer("hARRY","SDE")
# ALKA=Programmer("aLKA","Analyist")
# harry.getinfo()
# ALKA.getinfo()
#write a class calculator capable of finding square,cube,and squareroot
# class Calculator:
#     def __init__(self,num):
#         self.number=num
#     def square(self):
#         print(f"The value of{self.number} square is {self.number **2}")
#     def squareRoot():
#         pass
# a=Calculator(3)    
# a.square()
# create a class with class attribute a create an object from it and set a directly using object a=0 Does this change the class attribute?

# class  Sample:
#     a="harry"
# obj=   Sample()
# obj.a="Vikky"  #yh instance attribute hn yh hng ni hoga yh alg class alg
# Sample.a="Vikky" #aese chng ho jaega
# print(Sample.a)
# print(obj.a)
#ques greet with static method

from turtle import st


class Greeting:
    @staticmethod
    def greet():
     print("good morning")

a=Greeting()
a.greet()     