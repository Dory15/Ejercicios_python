# Variables en python
numero_entero = 5
numero_flotante = 5.8
numero_flotante_elevado = 5.6e4 # 5.6 elevado a la 4
numero_complejo = 1j

letra = 'A' # Como tal el tipo de dato char en python no existe pero se simula
cadena = "Hola"

lista = [ 'Hola', 5, 5.268, 5.8e6, 1j ] # Listas en python son arreglos
tupla = ( 'Hola', 5, 5.268, 5.8e6, 1j ) # Las tuplas son listas pero no se pueden cambiar sus valores
set = {'Uno', 'Dos', 'Tres'} # Los set son listas desindexadas y desordenadas

diccionario = {'nombre': 'Carlitos', 'edad': 18, 'escuela': 'Cecyt #9'} # Los diccionarios en python son objectos json

print(" El diccionario es: {} \n Los sets son: {} \n".format(diccionario, set));
print(" La lista es: {} \n La tupla es: {} \n".format(lista, tupla))
print(" Tipo de numero entero: {} \n Tipo de numero flotante: {} \n Tipo de numero flotante elevado: {} \n Tipo de numero complejo: {} \n Tipo de dato de letra: {} \n Tipo de dato de cadena: {} \n".format(type(numero_entero), type(numero_flotante), type(numero_flotante_elevado), type(numero_complejo), type(letra), type(cadena)))
print(" Numero entero: {} \n Numero flotante: {} \n Numero flotante elevado {} \n Numero complejo: {} \n Letra: {} \n Cadena: {}".format(numero_entero, numero_flotante, numero_flotante_elevado, numero_complejo, letra, cadena))
