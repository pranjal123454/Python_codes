# class Number:
#     def sum(self):
#         return self.a +self.b 
# num =Number()
# num.a=12
# num.b=43
# s=num.sum()
# print(s)
class Railway:
    formType="railwayForm"
    def printData(self):
        print(f"Name is:{self.name}")
        print(f"Train is:{self.train}")
harry=Railway()
harry.name="Harry"
harry.train="Kafiyat Express"

harry.printData()