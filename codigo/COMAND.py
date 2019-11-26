'''
Created on 22 nov. 2019

@author: USUARIO
'''

from abc import ABC, abstractmethod

class Archivo:
    @abstractmethod
    def attack(self):
        pass
    
class Comandos(Archivo):
    def ejecutar(self):
        pass
        
class DefComandos(Comandos):
    def Guardar(self):
        pass
    def Abrir(self):
      pass
    def Cerrar(self):
        pass
    
    
class ArchivoReceptor(DefComandos):
    def ejecutar(self):
        pass

        
