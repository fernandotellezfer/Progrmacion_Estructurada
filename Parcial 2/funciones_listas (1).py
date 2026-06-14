"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.


Funciones más comunes en las listas
"""
print("\033c")
paises=["Mexico", "Canada", "EUA","Mexico","Brasil"]

numeros=[23,45,8,24]

varios=["Hola", 3.1416, 33, True]

vacia=[]
#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacia)

print(paises[1])
for numero in numeros:
   print(numero)


    
for vario in varios:
    print(vario)
#Recorrer la lista 
#1er forma 
for pais in paises:
    print(pais)

# #2do forma 
for i in range(0,len(paises),1):
    print(paises[i])



#ordenar elementos de una lista
paises=["Mexico", "Canada", "EUA","Mexico","Brasil"]
paises.sort()

for pais in paises:
    print(pais)
#dar la vuelta a una lista
paises.reverse()
for pais in paises:
    print(pais)

print("\033c")
paises=["Mexico", "Canada", "EUA","Mexico","Brasil"]

#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Colombia")
print(paises)
paises.insert(8,"Australia")
print(paises)


#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(4) ##pop es una funcion remueve un elemento 
print(paises)
#2da forma 
paises.remove("EUA")
print(paises)
paises.pop(4)
print(paises)

#Buscar un elemento dentro de la lista
resp="Brasil" in paises
print(resp)

if "Brasil" in paises:
    print("la respuesta es TRUE")
else:     print("la respuesta es TRUE")
#Contar el numeros de veces que aparece un elemento dentro de una lista

numeros=[23,45,8,24,100,200,0,-1,-10,23,24,8,23,50]
print(numeros)


numeros.sort()
print(numeros)
num=int(input("Ingresa un numero: "))
cuantos=numeros.count(num)
print(f"El numero de veces que aparece el {num} es: {cuantos}")

#Conocer la posicion o indice en el que se encuentra un elemento de la lista
posicion=numeros.index(23)
print(f"La posicion del numero es posicion: {posicion}")


#Unir el contenido de una lista dentro de otra lista
numeros=[23,45,8,24,100,200,0,-1,-10,23,24,8,23,50]
print(numeros)
numeros2=[500,1000]
print(numeros2)
numeros.extend(numeros2)
#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente

numeros.sort()
numeros.reverse()
print(numeros)



