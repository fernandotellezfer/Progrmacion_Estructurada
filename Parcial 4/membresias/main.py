import re
from .funciones import agregarMembresia, verMembresia, borrarPantalla, catalogoMembresias, eliminarMembresias, verificarVencimientoMembresias, actualizarMembresia
from utils.exportar import exportarExcelmembresia
def menuMembresias():
    activo = True
    while activo == True:
        borrarPantalla()
        print("\n--- MENÚ DE MEMBRESIAS ---")
        print("1. Agregar membresia")
        print("2. Consultar membresias")
        print("3. Catalogo")
        print("4. Eliminar todas las membresias")
        print("5. Verificar vencimiento de membresias")
        print("6. Actualizar membresias")
        print("7. Exportar excel de membresias")
        print("8. Regresar al menu principal")

        opcion_ok = False
        while opcion_ok == False:
            opcion = input("Selecciona: ").strip()
            if re.fullmatch(r"[1-8]", opcion):
                opcion_ok = True
            else:
                print("Solo 1-8")

        match opcion:
         case "1":
            agregarMembresia()
         case "2":
            verMembresia()
         case "3":
            catalogoMembresias()
         case "4":
            eliminarMembresias()
         case "5":
            verificarVencimientoMembresias()
         case "6":
            actualizarMembresia()
         case "7":
            exportarExcelmembresia()
         case"8":
            input("... Regresando...")
            activo = False # Apaga el menu
            return # Regresa al main
           