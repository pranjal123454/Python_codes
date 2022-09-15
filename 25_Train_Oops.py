class Train:
    def __init__(self,name,fare,seats):
        self.name= name
        self.fare= fare
        self.seats= seats
    def getstatus(self):
        print(f" THe name of the Train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
    def fareinfo(self):
        print(f"the fare of {self.name} is {self.fare}")
intercity=Train("Intercity Express:1342",90,30)
intercity.getstatus()    
intercity.fareinfo()    
