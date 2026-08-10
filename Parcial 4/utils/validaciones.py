import re
#la funcion principal de esta libreria es buscar, comparar, validar y manipular patrones de texto dentro de cadenas de caracteres
def validar_nombre(nombre):
    return re.match(r"^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$", nombre)
#verifica que una cadena de texto contenga unicamente letras (mayusculas, minusculas y la letra ñ) y espacios

def validar_numero(valor):
    return re.match(r"^\d+(\.\d+)?$", valor)
# verifica que la entrada sea estrictamente un numero, permitiendo tanto numeros enteros como numeros decimales (con punto)