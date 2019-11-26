from abc import ABC,abstractmethod

class Comida:
    @abstractmethod
    def attack(self):
        pass

class China(Comida):
    def Arroz(self):
        pass
class Mexicana(Comida):
    def Tacos(self):
        pass
    
class Decoorador(Mexicana):
    def cebolla(self):
        pass
    def Cilantro(self):
      pass
    def Salsa(self):
        pass
   
