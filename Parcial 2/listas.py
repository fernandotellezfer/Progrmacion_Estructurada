import os
os.system("cls")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[10,34,25,45]


lista="["
for i in numeros:
    lista+=f"{i}, "
print(f"{lista}]")

lista="["
for i in range(0,len(numeros)):
    lista+=f"{numeros[i]}, "
print(f"{lista}]")

lista="["
c=0
while c<len(numeros):
        lista+=f"{numeros[c]}, "
        c+=1
print(f"{lista.strip()}]")       


opc="SI"
while opc =="SI":
    numero=int(input("Dame un numero: "))
    numeros.append(numero)
    opc=input("Deseas agregar otro: SI/NO ").upper().strip()


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=["UTD","segundo","TI","MTI"]
palabra=input("Dame una palabra a buscar ").strip()
if palabra in palabras:
    print("Encontre la palabra en la lista :)")
else:
    print("No se encontro la palabra en la lista :(")

#2DA FORMA
encotro=False
for i in palabras:
    if i ==palabra:
        encotro=True
if encotro:
    print("Encontre la palabra en la lista :)")
else:
    print("No se encontro la palabra en la lista :(")

#3er FORMA
encotro=False
for i in range(0,len(palabras)):
    if palabras[i] ==palabra:
        encotro=True
if encotro:
    print("Encontre la palabra en la lista :)")
else:
    print("No se encontro la palabra en la lista :(")
#4ta FORMA
encotro=False
con=0
while con<len(palabra):
        if palabras[con] ==palabra:
            encotro=True
if encotro:
    print("Encontre la palabra en la lista :)")
else:
    print("No se encontro la palabra en la lista :(")


#Ejemplo 3 Añadir elementos a la lista
lista=[]
#version 1
true=True
while true:
    dato=input("Dame un valor para la lista: ").upper().strip()
    lista.append(dato)
    true=input("deseas añadir mas elementos a la lista? (SI/NO) ").lower().strip()
    if true=="no":
        true=False

#version 2
true="si"
while true=="si":
    dato=input("Dame un valor para la lista: ").upper().strip()
    lista.append(dato)
    true=input("deseas añadir mas elementos a la lista? (SI/NO) ").lower().strip()

print(lista)


#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda=[
        ["Carlos","6181234567"],
        ["Alberto","6182344567"],
        ["Martin","6181231223"]
        ]
print(agenda)

for i in agenda:
    print(i)
    
for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])
        
lista=""
for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c]}, "
    lista+="\n"
    print(lista)