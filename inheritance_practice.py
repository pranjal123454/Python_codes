#ques create a class c-2d vector and use it to create another class representing a 3d vector
# class c2dvec:
#     def __init__(self,i,j):
#         self.icap=i
#         self.jcap=j
#     def __str__(self):
#        return f"{self.icap}i+{self.jcap}j" 
# class c3dvec(c2dvec):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.kcap=k
#     def __str__(self):
#        return f"{self.icap}i+{self.jcap}j +{self.kcap}k"     

# v2d=c2dvec(1,3) 
# v3d=c3dvec(1,3,4)         
# print(v2d)
# print(v3d)


#ques create class employee and add property ko add
# class Employee:
#     salary=1000
#     increment=1.5
#     @property
#     def salaryAfterIncrement(self):
#      return self.salary * self.increment

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,sai):
#         self.increment=sai/self.salary
# e=Employee()
# print(e.salaryAfterIncrement)

# ques class of complex no and do multiply
class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,c):
        return Complex(self.real+c.real,self.imaginary +c.imaginary)

    def __mul__(self,c):
        mulReal=self.real*c.real - self.imaginary +c.imaginary
        mulImaginary=self.real*c.imaginary +self.imaginary*c.real
        return Complex(self.mulReal,self.mulImaginary)    

    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
     
c1=Complex(1,4)
c2=Complex(8,5)
print(c1+c2)
print(c1*c2)

   







