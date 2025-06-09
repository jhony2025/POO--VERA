class Ave: #Creamos la clase Ave
    def volar(self): #Añadimos un metodo de volar
        return "Esta ave vuela alto" #Retornamos un mensaje

class Pinguino: #Creamos otra clase
    def volar(self): #Añadimos un metodo
        return "Los pingüinos no pueden volar"

def describir_vuelo(ave): #Creamos una funcion
    print(ave.volar())

describir_vuelo(Ave())
describir_vuelo(Pinguino())