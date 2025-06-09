class CuentaBancaria:  #Creamos la clase
    def __init__(self, saldo): #Llamaos al cosntructor e inicializamos saldo
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad): #Creamos el metodo
        self.__saldo += cantidad #Sumamos

    def obtener_saldo(self): #Creamos otro metodo del saldo disponible
        return f"Saldo disponible: {self.__saldo}"

mi_cuenta = CuentaBancaria(1000)
mi_cuenta.depositar(500)
print(mi_cuenta.obtener_saldo()) #Imprimimos

