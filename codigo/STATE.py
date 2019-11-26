
from abc import ABC, abstractmethod

class Persona(Estados):
    @abstractmethod
    def at(self):
        pass
    
class Estados:
    def maneja(self):
        pass
        
class DefEstados(Estados):
    def Alegria(self):
        pass
    def Tristeza(self):
      pass
    def Felicidad(self):
        pass
    def Enojo(self):
        pass
    def Miedo(self):
        pass
    
    
