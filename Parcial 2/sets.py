print("\033c")
"""
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.

"""
set1={"Python", "SLQ","Estructurado","SQL"}
print(set1)
for i in set1:
  print(i)
set2={"Hola", True,33, 33.1416}
print(set2)
set2_respaldo=set2.copy()
print(set2_respaldo)
set3={""}
print(set3)
set3.add("HOLA")
print(set3)
set3.add("3")
print(set3)
set3.add(10.0)
print(set3)
set3.add(3)
print(set3)
set3.pop()
set3.pop()
print(set3)
set3.clear()
print(set3)
set3.add("3")
lista=[10,9.5,8.5,3.4]
"""
ejemplo Crear un programa que solicite los email de los alumnos de 
la UTD almacenar en una lista y posteriormente mostrar en pantalla los 
email sin duplicados
"""
#Solucion 1
set_emails={""}
lista_emails=[]
opc="S"
while opc=="S":
  lista_emails.append(input("Ingresa el email: ").lower().strip())
  set_emails.add(input("Ingresa el email: ").lower().strip())
  opc=input("Deseas agregar otro (S/N)?: ").upper().upper().strip()
print(lista_emails)
print(set_emails)
set_emails=set(lista_emails)
print(set_emails)
lista_emails=list(set_emails)
print(lista_emails)
#Solucion 2
opc=True
while opc:
  lista_emails.insert(1,input("Ingresa el email: ").lower().strip())
  set_emails.add(input("Ingresa el email: ").lower().strip())
  opc=input("Deseas agregar otro (S/N)?: ").upper().strip()
  if opc=="N":
    opc=False
set_emails=set(lista_emails)
lista_emails=list(set_emails)
print(lista_emails)

  



