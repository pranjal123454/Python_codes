


#inheritance example 1
# class Employee:
#     company="Microsoft"
#     def getPersonaldetails(self,name,phno,address):
#         self.name=name
#         self.address=address
#         self.phno=phno
#         print(f"THe name of the EMployee is{self.name} and addressis :{self.address} and phno is:{self.phno}")
# class Programmer(Employee):
#     def printAge(self):
#         print("Age")
# harry=Employee()
# harry.getPersonaldetails("HaRRY","8287118690","ghaziabad")
# pranjal=Programmer()
# pranjal.getPersonaldetails("pranjal","8287118690","ghaziabad")

#multiple inheritance
class Employee:
    company="visaa"
class Freelancer:
    company="fiverr"  
    level=2 
class Programmer(Employee,Freelancer):
    name="Rohit"
p= Programmer()
print(p.company)   #nearest parent ka method run krta hn   
print(p.level)
