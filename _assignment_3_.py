class Dog:
    def __init__(self,name,age,colour):
        self.name = name
        self.age = age
        self.colour = colour
    def description(self):
        print(f" Name of dog given is : {self.name} \n Age of Dog given is : {self.age}")
    def get_info(self):
        print( f" Colour of Dog given is : {self.colour}")
class JackRussellTerrier(Dog):
    def __init__(self):
        super().__init__(name,age,colour)
    def family(self):
        print(" Yes JackRusellTerrier is a Family Dog")
    def breed(self):
        print("JackRusellTerrier is from Reverend John Russell")
class bulldog(Dog):
    def __init__(self):
        super().__init__(name,age,colour)
    def size(self):
        print("Yes Bull dogs are small size")
    def life(self):
        print("Bull Dogs can live 8-10 Years")
name = input("Enter Name of the Dog : ")
age = int(input("Enter Age of the Dog : "))
colour = input("Enter colour of the Dog : ")


 
Dog_obj = Dog(name,age,colour)          

Dog_obj.description()                                         #For Description

Dog_obj.get_info()                                            #For Get_Info

JackRussellTerrier_obj = JackRussellTerrier()                 #For JackRussellTerrier
#JackRussellTerrier_obj.description()
#JackRussellTerrier_obj.get_info()
JackRussellTerrier_obj.family()
JackRussellTerrier_obj.breed()


bulldog_obj = bulldog()                                        #For Bull Dog
#bulldog_obj.description()
#ulldog_obj.get_info()
bulldog_obj.size()
bulldog_obj.life()