import os

# para leer o escribir en el fichero necesitamos un descriptor de fichero, que es el puntero a una posición del archivo.
# para realizar estas acciones es necesario importar la libreria os (sistema operativo).

ruta = 'C:\\Users\\pablo\\OneDrive\\Escritorio\\archivo.txt'

#####################################
with open(ruta, 'r') as reader:
    for line in reader:
        print(line)
# esto sirve para lectura
#####################################
#####################################
with open(ruta, 'r') as reader:
    reader.seek(8)
    for line in reader:
        print(line)
# esto sirve para lectura empezando desde un caracter determinado
#####################################
file = open(ruta, "w")

file.write("Hola\n")
file.write("Vale  caracolis.\n")

file.close()
# esto sirve para escritura borrando todo el contenido anterior
####################################
#####################################
file = open(ruta, "a")

file.write("Hello\n")
file.write("Okey snail.\n")

file.close()
# esto sirve para escritura sin borrar lo anterior.
####################################
file = open(ruta, 'r')
print(file.readline(3))
file.close()
# file.write("Holoooooa")
# file.write("\nLinea 40567")
# file.close()
