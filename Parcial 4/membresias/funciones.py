from conexion import conectar_bd 
from datetime import date, timedelta
import re 

# Lista en memoria para guardar las membresias agregadas en esta sesión
lista_membresias_memoria = []

# Funciones basicas
def accionExitosa():
    print("... ✅ ACCION REALIZADA CON EXITO ✅...")

def teclaEspera():
    input("...: 🌨️ PRESIONA UNA TECLA PARA CONTINUAR 🌨️ :...")

def borrarPantalla():
    print("\033c") 

def membresiaExitosa():
    print("...✅ ¡MEMBRESIA AGREGADA CON EXITO! ✅...")

def sinMembresias():
    print("... ❌ NO HAY MEMBRESIAS ❌...")

def noExisteId():
    print("...❌ NO EXISTE ESTE ID, VERIFIQUE ❌...")

def agregarMembresia():
    conexionBD = conectar_bd() 
    cursor = conexionBD.cursor()
    try:
        # Flag 
        continuar = True
        while continuar: 
            borrarPantalla()
            print("... AGREGAR MEMBRESIA...")
            id_valido = False
            while id_valido == False: 
                entrada_id = input("ID del socio: ").strip()
                # re.fullmatch valida que solo sean numeros y no empiece en 0
                if not re.fullmatch(r"[1-9][0-9]*", entrada_id):
                    print("Error: Pon solo numeros mayores a 0")
                else:
                    id_socio = int(entrada_id)
                    cursor.execute("SELECT id FROM socios WHERE id = %s", (id_socio,))
                    if cursor.fetchone(): # Si si lo encuentra
                        id_valido = True # Rompe el ciclo de validacion
                    else:
                        noExisteId()
                        teclaEspera()
                        return # Regresa al menu si no existe
            # --- VALIDACION DE TIPO CON REGEX ---
            patron_tipo = r"^(dia|semanal|mensual|trimestral|anual)$" # Solo acepta esos 5 tipos
            tipo_ok = False 
            while tipo_ok == False:
                tipo = input("Tipo (dia/semanal/mensual/trimestral/anual): ").lower().strip()
                if re.fullmatch(patron_tipo, tipo): # Si cumple el patron de re
                    tipo_ok = True
                else:
                    print("Error: Solo dia, semanal, mensual, trimestral y anual")
            # Diccionario con precios y dias de duracion
            precios = {
                "dia": (50, 1),
                "semanal": (200, 7),
                "mensual": (500, 30),
                "trimestral": (1300, 90),
                "anual": (4500, 365)
            }
            precio, dias = precios[tipo] # Saca precio y dias segun el tipo
            fecha_inicio = date.today() # Fecha de hoy
            fecha_fin = fecha_inicio + timedelta(days=dias) # Fecha de vencimiento
            print(f"\n\tPrecio: ${precio} - Vence: {fecha_fin}")
            # tabla membresia
            cursor.execute("INSERT INTO membresia(id_socio, tipo, precio, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s, %s)",(id_socio, tipo, precio, fecha_inicio, fecha_fin))
            conexionBD.commit() 
            # Agregamos tambien a la lista en memoria
            lista_membresias_memoria.append({
                "id_socio": id_socio,
                "tipo": tipo,
                "precio": precio,
                "inicio": str(fecha_inicio),
                "fin": str(fecha_fin)
            })
            membresiaExitosa()
            #VALIDACION DE SI/NO CON REGEX 
            resp_ok = False
            while resp_ok == False:
                opc = input("¿ Deseas agregar otra? (si/no): ").lower().strip()
                if re.fullmatch(r"^(si|no)$", opc): # Solo acepta si o no
                    resp_ok = True
                    if opc == "no":
                        continuar = False 
                else:
                    print("Error: Solo si o no")
        accionExitosa()
        teclaEspera()
    finally:
        conexionBD.close() # Siempre cierra la conexion al final

# --- CATALOGO ---
def catalogoMembresias():
    borrarPantalla()
    print("... CATALOGO DE MEMBRESIAS...")
    print("┌──────────────────────────────┬─────────────┬")
    print("│ Tipo de Membresía │ Duración │ Precio      │")
    print("├──────────────────────────────┼─────────────┼")
    print("│ 1. Diaria         │ 1 Día    │ $50.00      │")
    print("│ 2. Semanal        │ 7 Días   │ $200.00     │")
    print("│ 3. Mensual        │ 30 Días  │ $500.00     │")
    print("│ 4. Trimestral     │ 90 Días  │ $1300.00    │")
    print("│ 5. Anual          │ 365 Días │ $4500.00    │")
    print("└──────────────────────────────┴─────────────┴")
    teclaEspera() # Para que no se borre rapido

def verMembresia():
    borrarPantalla()
    print("... VER MEMBRESIAS ACTIVAS...")
    # Muestra primero lo de la lista en memoria
    if lista_membresias_memoria:
        print("--- En memoria ---")
        for m in lista_membresias_memoria:
            print(m)
        print("-" * 30)
    conexionBD = conectar_bd()
    cursor = conexionBD.cursor()
    try:
        cursor.execute("SELECT * FROM membresia") # Trae todas de la BD
        registros = cursor.fetchall()
        if registros:
            print("--- En BD ---")
            for reg in registros:
                print(f"ID: {reg[0]} | Socio: {reg[1]} | Tipo: {reg[2]} | Precio: ${reg[3]} | Inicio: {reg[4]} | Fin: {reg[5]}")
                print("-" * 30)
        else:
            if not lista_membresias_memoria: # Si tampoco hay en memoria
                sinMembresias()
        teclaEspera()
    finally:
        conexionBD.close() 

def eliminarMembresias():
    borrarPantalla()
    print("\n--- ELIMINAR TODAS LAS MEMBRESIAS ---")
    print("¡CUIDADO! Esto borrara TODAS las membresias y socios")
    confirmar = input("Escribe SI para borrar todo: ").strip()
    
    if confirmar == "SI" or confirmar == "si":
        conexion = None
        try:
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM membresia")
            cursor.execute("DELETE FROM socios")
            cursor.execute("ALTER TABLE membresia AUTO_INCREMENT = 1")
            cursor.execute("ALTER TABLE socios AUTO_INCREMENT = 1")
            conexion.commit()
            print(f"✅ Se borraron todas las membresias y socios. ID reiniciado a 1")
        except Exception as e:
            print(f"❌ [Error] No se pudo borrar: {e}")
        finally:
            if conexion:
                conexion.close()
    else:
        print("\n...❌ Operacion cancelada ❌...")
    teclaEspera()

def verificarVencimientoMembresias():
    borrarPantalla()
    print("\n--- ALERTA DE MEMBRESIAS VENCIDAS ---\n")
    conexion = None
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor(dictionary=True)
        # Trae socios con su fecha fin
        cursor.execute("SELECT s.id, s.nombre, m.fecha_fin FROM socios s INNER JOIN membresia m ON s.id = m.id_socio")
        socios = cursor.fetchall()
        hoy = date.today()
        hay_alertas = False
        for socio in socios:
            fecha_fin = socio['fecha_fin']
            dias_restantes = (fecha_fin - hoy).days
            # ALERTA 1: YA VENCIÓ
            if dias_restantes < 0:
                print(f"!! ALERTA!! Socio {socio['id']} - {socio['nombre']} | VENCIDA el {fecha_fin} -> Se quitara su membresia")
                hay_alertas = True
            # ALERTA 2: ESTA POR VENCER
            elif dias_restantes <= 3:
                print(f"!! AVISO!! Socio {socio['id']} - {socio['nombre']} | Vence en {dias_restantes} dias ({fecha_fin})")
                hay_alertas = True
        if not hay_alertas:
            print("... ✅ No hay membresias por vencer, todo en orden...")
    except Exception as e:
        print(f"❌ [Error] No se pudo verificar vencimientos: {e}")
    finally:
        if conexion:
            conexion.close()

    teclaEspera()

def actualizarMembresia():
    borrarPantalla()
    print("\n--- ACTUALIZAR MEMBRESIA ---")
    conexionBD = conectar_bd()
    if not conexionBD:
        return
    cursor = conexionBD.cursor()
    try:
        id_txt = input("ID del socio a actualizar: ").strip()
        if not re.fullmatch(r"[1-9][0-9]*", id_txt):
            print("Error: Pon solo numeros mayores a 0")
            return
        id_socio = int(id_txt)
        # Busca si tiene membresia
        cursor.execute("SELECT id, tipo, fecha_fin FROM membresia WHERE id_socio = %s", (id_socio,))
        mem = cursor.fetchone()
        if not mem:
            noExisteId()
            print("Ese socio no tiene membresia activa.")
            return
        print(f"Membresia actual: {mem[1]} - Vence: {mem[2]}")
        # Validacion del nuevo tipo
        patron_tipo = r"^(dia|semanal|mensual|trimestral|anual)$"
        nuevo_tipo = ""
        while True:
            nuevo_tipo = input("Nuevo tipo (dia/semanal/mensual/trimestral/anual): ").lower().strip()
            if re.fullmatch(patron_tipo, nuevo_tipo):
                break
            print("Error: Solo dia, semanal, mensual, trimestral y anual")
        # Calcula la nueva fecha fin
        hoy = date.today()
        precios = {
            "dia": 1,
            "semanal": 7,
            "mensual": 30,
            "trimestral": 90,
            "anual": 365
        }
        dias = precios[nuevo_tipo]
        nueva_fin = hoy + timedelta(days=dias)
        cursor.execute("UPDATE membresia SET tipo = %s, fecha_inicio = %s, fecha_fin = %s WHERE id_socio = %s",
                       (nuevo_tipo, hoy, nueva_fin, id_socio))
        conexionBD.commit() 
        if cursor.rowcount > 0:
            print("✅ Membresia actualizada correctamente.")
        else:
            print("No se actualizo nada.")
        teclaEspera()
    finally:
        cursor.close()
        conexionBD.close() 