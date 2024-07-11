import os , time , csv 
from funciones import *


while True:
    print("MENÚ DE OPCIONES")
    print("1. Asignar sueldos aleatorios: ")
    print("2. Clasificar sueldos: ")
    print("3. Ver estadisticas: ")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in (1,2,3,4,5):
                break
            else:
                print("Ingrese opción correcta!!")
        except:
            print("Ingrese una opción con números enteros!")

    if opc ==1:
        Asignar_sueldos()
    elif opc==2:
        Clasificar_sueldos()
    elif opc ==3:
        ver_estadisticas()
    elif opc ==4:
        Reporte_sueldos()
    elif opc ==5:
        salir_programa()
    else:
        print("Adios vuelva pronto!")
        time.sleep(3)


