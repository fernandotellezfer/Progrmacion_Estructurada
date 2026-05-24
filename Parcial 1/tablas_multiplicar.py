'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones



num_tabla= int (input("¿de que numero de tabla de multiplicar quieres?: "))
num=1

multi=num_tabla*num
print(f"{num}x 1: {num}")
num+=1
multi=num_tabla*num
print(f"{num}x 1: {num}")
num+=1
multi=num_tabla*num
print(f"{num}x 1: {num}")
num+=1
multi=num_tabla*num
print(f"{num}x 1: {num}")
num+=1
multi=num_tabla*num
print(f"{num}x 1: {num}")
num+=1
multi=num_tabla*num
print(f"{num}x 1: {num}")
num+=1
multi=num_tabla*num
print(f"{num}x 1: {num}")
num+=1
multi=num_tabla*num
print(f"{num}x 1: {num}")
num+=1
'''

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones


print=("\033c")
num_tabla= int (input("¿de que numero de tabla de multiplicar quieres?: "))
num=1
while num<=10:
  multi=num_tabla*num
  print(f"{num_tabla}x {num}= {multi}")
  num+=1
'''
print=("\033c")
def tabla(num_tabla,num):
  multi=num_tabla*num
  print(f"{num_tabla}x num= {multi}")
  n+=1
  return num
num_tabla= int (input("¿de que numero de tabla de multiplicar quieres?: "))
num=1
num= tabla(num_tabla,num)
num= tabla(num_tabla,num)
num= tabla(num_tabla,num)
num= tabla(num_tabla,num)
num= tabla(num_tabla,num)
num= tabla(num_tabla,num)
num= tabla(num_tabla,num)
num= tabla(num_tabla,num)
num= tabla(num_tabla,num)
num= tabla(num_tabla,num)

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones
'''
 print=("\033c")
 def tabla(num_tabla,num):
 num_tabla= int (input("¿de que numero de tabla de multiplicar quieres?: "))
 num=1

for n in range(1,11):
  mult= num_tabla*n
  print (f"{num tabla} x {n} = {mult}")