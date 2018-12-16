# Funciones en python

#Funcion sencilla
def hello_world():
    print("¡Hola Mundo!")

hello_world()


#Funcion con Parametro

def imprimirNombre(nombre):
    print("¡Hola {}!".format(nombre))

imprimirNombre("Paco")


#Funcion con Parametro por default

def imprimirEdad(edad = 18):
    print("Tu edad es ", edad)

imprimirEdad()
imprimirEdad(15)


#Funcion con retorno de valor

def multiplicacion(a = 0, b = 0):
    return a * b

print("El resultado de la suma es: ", multiplicacion(16,4))

# Funcion que retorna mas de un valor

def division(a = 1, b = 1):
    # Parseamos el resultado para que se vea más claro el ejemplo
    return (int) (a / b), a % b

resultado, residuo = division(22, 7)
print("El resultado es: {} y el residuo es: {}".format(resultado, residuo))

# Funciones anonimas o lambda

resta = lambda a = 0, b = 0 : a - b

print("El resultado es: ", resta(20, 10))
