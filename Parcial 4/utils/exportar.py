from conexion import conectar_bd 
import csv #libreria estandar para exportar a csv, no requiere instalacion ni internet

def teclaEspera():
    input("... PRESIONA CUALQUIER TECLA PARA SALIR ...")

def borrarPantalla():
    print("\033c")

import csv

def exportarExcelmembresia():
    conexion = None
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, id_socio, tipo, precio, fecha_inicio, fecha_fin FROM membresia")
        datos = cursor.fetchall()

        with open("membresias.csv", "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["ID", "ID Socio", "Tipo", "Precio", "Fecha Inicio", "Fecha Fin"])
            writer.writerows(datos)

        borrarPantalla()
        print("--- EXPORTAR ARCHIVO ---")
        input("¡Archivo membresias.csv creado con éxito!")
        teclaEspera()

    except Exception as e:
        input(f"Error: {e}")
        teclaEspera()
    finally:
        if conexion:
            conexion.close()


def exportarExcelsocios():
    conexion = None
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, edad, peso, estatura, imc FROM socios")
        datos = cursor.fetchall()
#crea archivo llamado socios.csv
        with open("socios.csv", "w", newline="", encoding="utf-8-sig") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["ID", "Nombre", "Edad", "Peso", "Estatura", "IMC"])
            writer.writerows(datos)

        borrarPantalla()
        print("--- EXPORTAR ARCHIVO ---")
        input(f"¡{len(datos)} socios exportados a socios.csv!")
        input("Excel generado correctamente")
        teclaEspera()

    except Exception as e:
        input(f"Error: {e}")
        input("Presiona enter para continuar...")
    finally:
        if conexion:
            conexion.close()