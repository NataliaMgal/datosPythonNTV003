#El append agrega un elemento a la lista 
multiplo=[]

tamaño = int(input("Ingrese el tamaño del arreglo: "))
for i in range(tamaño):
    multiplo.append((i+1) * 7) 

print(multiplo)