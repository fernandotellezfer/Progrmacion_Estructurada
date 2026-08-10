from conexion import conectar_bd
import re
from datetime import date, timedelta

# Lista en memoria
lista_socios_memoria = []

def borrarPantalla():
    print("\033c")

def teclaEspera():
    input("...🌨️ PRESIONA UNA TECLA PARA CONTINUAR 🌨️...")

def insertarSocio():
    borrarPantalla()
    print("\n--- REGISTRAR NUEVO SOCIO ---")
    # Validar nombre con re
    nombre_ok = False
    while nombre_ok == False:
        nombre = input("Nombre completo: ").strip()
        if re.fullmatch(r"[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+", nombre):
            nombre_ok = True
        else:
            print("❌ [Error] Solo letras")
    # Validar edad con re
    edad_ok = False
    while edad_ok == False:
        edad = input("Edad: ").strip()
        if re.fullmatch(r"[1-9][0-9]*", edad):
            edad = int(edad)
            edad_ok = True
        else:
            print("❌ [Error] Solo numeros mayores a 0")
    # Validar peso
    peso_ok = False
    while peso_ok == False:
        peso = input("Peso (ej: 70.0): ").strip()
        if re.fullmatch(r"[0-9]+(\.[0-9]+)?", peso):
            peso = float(peso)
            if peso > 0:
                peso_ok = True
            else:
                print("❌ [Error] Mayor a 0")
        else:
            print("❌ [Error] Solo numeros")
    # Validar estatura
    est_ok = False
    while est_ok == False:
        estatura = input("Estatura (ej 1.70): ").strip()
        if re.fullmatch(r"[0-9]+(\.[0-9]+)?", estatura):
            estatura = float(estatura)
            if estatura > 0:
                est_ok = True
            else:
                print(" ❌[Error] Mayor a 0")
        else:
            print(" ❌ [Error] Solo numeros")

    # Expresion algoritmica 1: Calculo IMC
    imc = peso / (estatura * estatura)

    # Menu membresia
    print("\n--- MEMBRESIA ---")
    print("1. Diario $50")
    print("2. Semanal $200")
    print("3. Mensual $500")
    print("4. Trimestral $1300")
    print("5. Anual $4500")

    opc_ok = False
    while opc_ok == False:
        opc = input("Elige (1-5): ").strip()
        if re.fullmatch(r"[1-5]", opc):
            opc_ok = True
        else:
            print("❌ Opcion invalida")

    if opc == "1":
        tipo = "Diario"
        precio = 50
        dias = 1
    elif opc == "2":
        tipo = "Semanal"
        precio = 200
        dias = 7
    elif opc == "3":
        tipo = "Mensual"
        precio = 500
        dias = 30
    elif opc == "4":
        tipo = "Trimestral"
        precio = 1300
        dias = 90
    else:
        tipo = "Anual"
        precio = 4500
        dias = 365
    fecha_inicio = date.today()
    fecha_fin = fecha_inicio + timedelta(days=dias)
    # Guarda en BD
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO socios (nombre, edad, peso, estatura, imc) VALUES (%s, %s, %s, %s, %s)", (nombre, edad, peso, estatura, imc))
    id_socio = cursor.lastrowid
    cursor.execute("INSERT INTO membresia (id_socio, tipo, precio, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s, %s)", (id_socio, tipo, precio, fecha_inicio, fecha_fin))
    conexion.commit()
    conexion.close()

    print(f"✅ Socio {nombre} registrado | IMC: {round(imc,2)} | {tipo}")
    teclaEspera()

def consultarSocios():
    borrarPantalla()
    print("--- CONSULTAR SOCIOS CON ESTADO DE MEMBRESIA ---\n")
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)
    
    cursor.execute("SELECT s.id, s.nombre, m.fecha_fin FROM socios s LEFT JOIN membresia m ON s.id = m.id_socio")
    registros = cursor.fetchall()
    
    if registros:
        for r in registros:
            if not r['fecha_fin']:
                print(f"{r['id']} - {r['nombre']} | SIN MEMBRESIA")
                continue

            from datetime import date
            dias_restantes = (r['fecha_fin'] - date.today()).days

            if dias_restantes < 0:
                print(f"{r['id']} - {r['nombre']} | {r['fecha_fin']} | !!! VENCIDA hace {-dias_restantes} dias -> SE QUITARA ACCESO !!!")
            elif dias_restantes <= 3:
                print(f"{r['id']} - {r['nombre']} | {r['fecha_fin']} | !! AVISO !! Quedan {dias_restantes} dias")
            else:
                print(f"{r['id']} - {r['nombre']} | {r['fecha_fin']} | Vigente ({dias_restantes} dias)")
    else:
        print("❌ No hay socios")
        
    conexion.close()
    teclaEspera()

def buscarSocios():
    borrarPantalla()
    print("\n---- BUSCAR SOCIO ----")
    try:
        id_b = input("ID a buscar: ")
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM socios WHERE id = %s", (id_b,))
        res = cursor.fetchone()
        print(res if res else " ❌ No encontrado")
        conexion.close()
    except Exception as e:
        print(" ❌Error al buscar:", e)
    teclaEspera()
    
def eliminarSocio():
    borrarPantalla()
    activo=True
    while activo:
         print("\n--- ELIMINAR SOCIO ---")
         id_socio = input("ID del socio a eliminar: ").strip()
         if re.fullmatch(r"\d+", id_socio):
            break
         else:
            print("ID inválido, solo números")
    conexion = None
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM socios WHERE id = %s", (id_socio,))
        socio = cursor.fetchone()
        if not socio:
            print("\n...❌ ID no encontrado ❌...")
        else:
            cursor.execute("DELETE FROM membresia WHERE id_socio = %s", (id_socio,))
            cursor.execute("DELETE FROM socios WHERE id = %s", (id_socio,))
            conexion.commit()
            print(f"\n ✅ Socio {id_socio} eliminado correctamente")
    except Exception as e:
        print(" ❌Error al eliminar:", e)
    finally:
        if conexion:
            conexion.close()
    teclaEspera()

def actualizarSocio():
    borrarPantalla()
    print("== ACTUALIZAR SOCIO ==")
    id_socio = input("ID del socio a actualizar: ").strip()
    if not re.fullmatch(r"\d+", id_socio):
        print("ID inválido, solo números")
        teclaEspera()
        return
    nombre_ok = False
    while nombre_ok == False:
        nombre = input("Nuevo nombre: ").strip()
        if re.fullmatch(r"[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+", nombre):
            nombre_ok = True
        else:
            print("Nombre inválido, solo letras")
    edad_ok = False
    while edad_ok == False:
        edad = input("Nueva edad: ").strip()
        if re.fullmatch(r"\d+", edad):
            edad = int(edad)
            edad_ok = True
        else:
            print("Edad inválida, solo números")
    peso_ok = False
    while peso_ok == False:
        peso = input("Nuevo peso (ej: 60.0): ").strip()
        if re.fullmatch(r"\d+(\.\d+)?", peso):
            peso = float(peso)
            peso_ok = True
        else:
            print("Peso inválido, solo números")
    estatura_ok = False
    while estatura_ok == False:
        estatura = input("Nueva estatura (ej: 1.70): ").strip()
        if re.fullmatch(r"\d+(\.\d+)?", estatura):
            estatura = float(estatura)
            estatura_ok = True
        else:
            print("Estatura inválida, solo números")
    imc = peso / (estatura * estatura)
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        valores = (nombre, edad, peso, estatura, imc, id_socio)
        cursor.execute("UPDATE socios SET nombre=%s, edad=%s, peso=%s, estatura=%s, imc=%s WHERE id=%s", valores)
        conexion.commit()
        if cursor.rowcount > 0:
            print("✅ Socio actualizado correctamente")
        else:
            print("❌ No se encontró el ID")
    except Exception as e:
        print("❌ Error al actualizar:", e)
    finally:
        if 'conexion' in locals() and conexion:
            conexion.close()
    teclaEspera()

def vaciarSocio():
    borrarPantalla()
    print("\n--- VACIAR TABLA SOCIOS ---")
    
    # Validacion si/no con regex como las demas funciones
    resp_ok = False
    while resp_ok == False:
        opc = input("¿Estas seguro de vaciar socios? (si/no): ").lower().strip()
        if re.fullmatch(r"^(si|no)$", opc):
            resp_ok = True
            if opc == "no":
                print("...❌ Operacion cancelada ❌...")
                teclaEspera()
                return
        else:
            print("Error: Solo si o no")

    conexion = None
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        # Desactivar llaves foraneas
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute("TRUNCATE TABLE membresia")
        cursor.execute("TRUNCATE TABLE socios")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        conexion.commit()
        print("✅ Tabla socios y membresias vaciadas correctamente. ID reiniciado a 1")
    except Exception as e:
        print(f"❌ Error al vaciar la tabla: {e}")
    finally:
        if conexion:
            conexion.close()
    teclaEspera()






