# 1er utilizar los modulos 

import modulos

modulos.borrarPantalla()
##modulos.funcion1()
n="Daniel"
a="Carreon"

nombres,apellidos=modulos.funcion4(n,a)
print(f"El nombre completo es: {nombres} {apellidos}")


#2da formar de utilizar modulos
from modulos import borrarPantalla, funcion3, funcion4
borrarPantalla()
n="Daniel"
a="Carreon"
funcion3(n,a)
nombres,apellidos=funcion4(n,a)
print(f"El nombre completo es: {nombres} {apellidos}")
