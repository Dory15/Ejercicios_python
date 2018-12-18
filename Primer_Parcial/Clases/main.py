from Recibir import Recibir
from Mostrar import Mostrar

def main():
    recibir = Recibir()

    nombre = recibir.recibirNombre()
    edad = recibir.recibirEdad()
    boleta = recibir.recibirBoleta()

    mostrar = Mostrar(nombre, edad, boleta)

    mostrar.mostrarBoleta()
    mostrar.mostrarNombre()
    mostrar.mostrarEdad()


if __name__ == '__main__':
    main()
