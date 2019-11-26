from abc import ABC, abstractmethod

class Carro(Llanta):
    @abstractmethod
    def attack(self):
        pass

class Llanta():
    def rodar(self):
        pass
class Camara(Llanta):
    def inflar(self):
        pass
class Rin(Llanta):
    def adornar(self):
        pass
class Virlos(Llanta):
    def sujetar(self):
        pass
