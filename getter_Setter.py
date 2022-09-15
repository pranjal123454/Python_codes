class Employee:
    company="Bharat Gas"
    salary=4566
    salarybonus=500
    totalSalary=6100

    @property       # this is called getter also ab total salary proprty ki trh pratit ho
    def totalSalary(self):
        return self.salary+self.salarybonus

e=Employee()     
print(e.totalSalary)   
