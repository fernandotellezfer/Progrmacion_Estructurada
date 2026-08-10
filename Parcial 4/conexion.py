import mysql.connector
def conectar_bd():
    try:
       conexion= mysql.connector.connect (
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_Powerfit"
    )
       return conexion
    except Exception as e:
        print("Error al conectar a la base de datos: ", e)
        return None




