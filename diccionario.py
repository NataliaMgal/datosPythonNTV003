estudiante={
    'nombre': 'Natalia',
    'edad' : 19,
    'exFutbolista': True
}
#Imprimir/acceder a todas las llaves
#Atributos de mi diccionario
print(estudiante)
#necesito acceder a un ATRIBUTO o LLAVE del diccionario
print(estudiante['nombre'])
print(estudiante.get('edad'))

#Recorrer un diccionario y obtener sus valores
for valor in estudiante.values():
    print(valor)