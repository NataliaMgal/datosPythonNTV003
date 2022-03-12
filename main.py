#Lista de datos
#una variable debe ser de nombre completo, especifico
#un arreglo debe tener un nombre en plural
#un arreglo debe guardar datos del mismo tipo

ciudades = ['Medellin','Cali','Bogota','Santa marta','Cartagena']
print(ciudades)

#Esculcando la lista (recorrer/buscar/explorar)
#los auxiliares del forech son variables locales, en este ejemplo es edison:
#el auxiliar de todo foreach deberia ser en singular del nombre del arreglo

for ciudad in ciudades:
    ciudad= "Medellin"
print(ciudad)

#lista #2 (arreglo)
numeros = [1,2,3,4,5]
suma = 0

for numero in numeros:
    suma+=numero
    print(f"La suma es:{suma}")

