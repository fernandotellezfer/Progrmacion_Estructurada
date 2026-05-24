def borrarPantalla():
    print("\033c")

def sueldoBase(h,s):
    sb=h*s
    return sb

opc="S"
trabajadores=0
acum_suel_neto=0

while opc=="S":
    borrarPantalla()

    nombre=input("Nombre: ")
    horas_trab=int(input("Horas trabajadas: "))
    sueldo=float(input("Sueldo por Horas trabajadas: "))

    sueldo_base= sueldoBase(horas_trab, sueldo)

    aumento=0
    if horas_trab==10:
        aumento=0.20
    elif horas_trab==15:
        aumento=0.30
    elif horas_trab==20:
        aumento=0.15  
    elif horas_trab>25:
        aumento=0.08
            
    aumento_pagar=aumento*sueldo_base
    suel_neto=sueldo_base+aumento_pagar
     
    trabajadores+=1  
    acum_suel_neto+=suel_neto
     
    print(f"El aumento es: {aumento_pagar}\n Y el sueldo neto cobrado es: {suel_neto}")
    opc=input("¿Deseas realizar otra vez (S/N)?: ").upper().strip()
print(f"El total de trabajadores es: {trabajadores}\n Y el sueldo neto acumulado es: {acum_suel_neto}")