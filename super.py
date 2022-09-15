#super method is used to access the methods of a super class in a derived class



#class attribute



class Employee:
    company="Camel"
    salary=100
    location="delhi"
    
    # def chagesalary(self,sal):
    #     self.salary=sal
    @classmethod
    def chagesalary(cls,sal):
        cls.salary=sal

e=Employee()
       
e.chagesalary(344)
print(e.salary) 
print(Employee.salary) #chng honme ke bd bhi salary same hn means we need class method 
#after use of class method chng ni hoga
