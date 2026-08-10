import re
from .funciones import borrarPantalla, insertarSocio, buscarSocios, eliminarSocio, consultarSocios, actualizarSocio, vaciarSocio
from utils.exportar import exportarExcelsocios

def menuSocios():
    
    activo = True
    while activo == True: # Mientras activo sea True se repite el menu
        borrarPantalla()
        print("\n--- MENÚ DE SOCIOS ---")
        print("1. Agregar socio")
        print("2. Consultar socios")
        print("3. Buscar socio")
        print("4. Eliminar socio")
        print("5. Actualizar socio")
        print("6. Vaciar socios")
        print("7. Exportar excel de socios")
        print("8. Regresar al menú principal")

        # Valida con re que solo sea del 1 al 8
        opcion_ok = False
        while opcion_ok == False:
            opcion = input("Selecciona una opción: ").strip()
            if re.fullmatch(r"[1-8]", opcion): # regex del 1 al 8
                opcion_ok = True
            else:
                print("Opción no válida, solo 1-8")

        # Llama a las funciones
        match opcion:
            case "1":
             insertarSocio()
            case  "2":
             consultarSocios()
            case "3":
             buscarSocios()
            case "4":
             eliminarSocio()
            case "5":
             actualizarSocio()
            case "6":
             vaciarSocio()
            case  "7":
             exportarExcelsocios()
            case "8":
             input("... Regresando...")
             activo = False # Apaga el menu
             return # Regresa al main
    