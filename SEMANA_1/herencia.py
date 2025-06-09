class Vehiculo:  #Definimos la clase
    def __init__(self, marca):  #Llamamos al constructor
        self.marca = marca

    def obtener_info(self): #Creamos un metodo
        return f"Vehículo marca {self.marca}" #Retornamos un mensaje

class Auto(Vehiculo):  # Hereda de Vehículo
    def obtener_info(self):
        return f"Auto marca {self.marca}, tiene cuatro ruedas"

mi_auto = Auto("Toyota") #Vamos a instancia la clase Vehiculo
print(mi_auto.obtener_info())