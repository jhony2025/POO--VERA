from abc import ABC, abstractmethod

class Animal(ABC):  #Creamos la clase y la bastraccion  # Clase abstracta
    @abstractmethod
    def sonido(self): #Creamos un metodo
        pass

class Leon(Animal): #Creamos otra clase
    def sonido(self):
        return "Rugido fuerte"

mi_leon = Leon() #Instanciamos
print(mi_leon.sonido())