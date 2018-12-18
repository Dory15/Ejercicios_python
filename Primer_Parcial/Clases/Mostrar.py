
# Hacemos en un archivo nuestra clase para imprimir en consola los datos
class Mostrar:
    # Iniciamos el constructor con los datos aunque se podría hacer sin el
    def __init__ (self, nombre, edad, boleta):
        self.nombre = nombre
        self.edad = edad
        self.boleta = boleta

    def mostrarNombre(self):
        print("Tu nombre es: ", self.nombre)

    def mostrarEdad(self):
        print("Tu edad es: ", self.edad)

    def mostrarBoleta(self):
        print("Tu boleta es: ", self.boleta)

    #El parametro self es para variables de la misma clase es un objecto
