#creando tuplas en python
estudiantes = ("Natalia", "Leidy")
print(estudiantes)

#estudiantes.append("martha") ERROR no se puede
#print(estudiantes)

#Recorriendo una tupla
for estudiante in estudiantes:
    print(estudiante)

#convertir dupla en lista (para modificarla, cambiarla)
listaEstudiantes = list(estudiantes)
print(listaEstudiantes) 
listaEstudiantes.append('Estudiante nuevo')
newTupla = tuple(listaEstudiantes)
print(newTupla)