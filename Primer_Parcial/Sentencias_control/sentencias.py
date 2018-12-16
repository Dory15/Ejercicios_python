# Estructura if

# If basico
a = 5
b = 10

if a < b :
    print("a es menor que b")


#If else
c = 13
d = 8

if c < d :
    print("c es menor que d")
else :
    print("d es mayor que c")


#If con else if

e = 8
f = 16

if e > f :
    print("e es mayor que f")
elif f > e :
    print("f es mayor que e")
else :
    print("Los dos numero son iguales")


# Ciclos while

# While basico
g = 0

while g < 11 :
    print("Este es el numero g: ", g)
    g += 1

# while en listas, lo mismo aplica para las tuplas

h = 0
i = ["Juanito", "Pedro", "Luis", "Francisco"]

while h < len(i):
    print("El nombre es: ", i[h])
    h += 1
    

# Ciclos for

# For basico con numero

for j in range(11):
    print("El numero es: ", j)

# For basico con intervalos

for k in range(10, 21):
    print("El numero es: ", k)

# For basico con intervalos e incremento definido

for l in range (30, 61, 3):
    print("El numero es: ", l)

# For en un string

for m in "Murcielago":
    print("La letra es: ", m)

# For en una lista

n = ["Manzana", "Uva", "Fresa"]

for o in n :
    print("La fruta es: ", o)
