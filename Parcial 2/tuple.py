"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
print("\033c")
paises1=("Mexico","Italia","Honduras","Mexico")
for i in paises1:
   print(i)  
for i in range(0,len(paises1)):
   print(paises1[i]) 
i=0
while i< len(paises1):
  print(paises1[i])
  i+=1 
paises1=("Mexico","Italia","Honduras","Mexico")
varios=("Mexico",True,3,3.1416)
print(paises1)
paises1[1]="Brasil" #no se puede 
print(f"Los paises que NO clasificaron al mundial 2026 son: {paises1[1]} y {paises1[2]} ")
cuantos=paises1.count("Brasil")
print(cuantos)
posicion=paises1.index("Italia")
print(posicion)