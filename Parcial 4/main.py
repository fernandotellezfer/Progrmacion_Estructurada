import re
from socios.main import menuSocios
from membresias.main import menuMembresias

NOMBRE_SISTEMA = "GYM POWERFIT SYNC"
VERSION = "2.5"

def borrarPantalla():
    print("\033c") 

def teclaEspera():
    input("...🌨️ PRESIONA UNA TECLA PARA CONTINUAR 🌨️...")

def principal():
    # Flags 
    activo = True
    intentos_fallidos = 0
    contador_operaciones = 0

    while activo == True: # Mientras activo sea True sigue el menu principal
        borrarPantalla()
        print(f".::. {NOMBRE_SISTEMA} v{VERSION}.::.")
        print("1. Gestionar Socios")
        print("2. Gestionar Membresías")
        print("3. Salir del Sistema")

        entrada = input("\nElige una opción: ").strip()

        # Validacion con re, solo permite 1, 2 , 3, 
        patron = r"^(1|2|3)$"
        entrada_ok = False
        while entrada_ok == False:
            if re.fullmatch(patron, entrada):
                entrada_ok = True
            else:
                intentos_fallidos += 1
                print(f"[Error] Opción no válida. Intentos: {intentos_fallidos}/3")
                if intentos_fallidos >= 3:
                    print("\nDemasiados intentos fallidos. Saliendo...")
                    activo = False
                    return # Sale del programa
                teclaEspera()
                borrarPantalla()
                print(f".::. {NOMBRE_SISTEMA} v{VERSION}.::.")
                print("1. Gestionar Socios")
                print("2. Gestionar Membresías")
                print("3. Salir del Sistema")
                entrada = input("\nElige una opción: ").strip()

        # Reinicia intentos si la opcion fue valida
        intentos_fallidos = 0
        contador_operaciones += 1

        # Opciones del menu principal
        match entrada:
            case  "1":
              borrarPantalla()
              menuSocios() # Va al submenu de socios
            case "2":
              borrarPantalla()
              menuMembresias() # Va al submenu de membresias
              teclaEspera()
            case "3":
              borrarPantalla()
              print(f"\nOperaciones totales en sesión: {contador_operaciones}")
              print("Saliendo del sistema...")
              activo = False # Apaga el menu
              return
 

# Este es el que se ejecuta primero
if __name__ == "__main__":
    principal()