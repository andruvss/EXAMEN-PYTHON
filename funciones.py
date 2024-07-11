import random , csv , time, os

lista_trabajadores = []
trabajadores = ["Juan Pérez", "María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
aleatorio = random.choice(trabajadores)
numeroaleatorio = random.randint(300000,2500000)





def Asignar_sueldos():
    print("Asignar sueldos")
    os.system('cls')
    for t in range(len(trabajadores)):
        Sueldo = numeroaleatorio
        Descuento_salud = int(7*Sueldo/100)
        Descuento_afp = int(12*Sueldo/100)
        Sueldo_liquido1 = Descuento_afp-Sueldo
        Sueldo_liquido2 = Descuento_salud-Sueldo_liquido1
        Trabajador = {"Nombre": trabajadores[t], "Sueldo": Sueldo, "Descuento AFP": Descuento_afp, "Descuento SALUD": Descuento_salud , "Sueldo liquido": Sueldo_liquido2}
        lista_trabajadores.append(Trabajador)

        print("Asignando sueldos a los trabajadores")
        time.sleep(1)
        print("Cargando..")
        time.sleep(1)
        print("Guardado exitosamente")
        for t in trabajadores:
            print("Trabajador",t,numeroaleatorio)
        break
        

        


   


def Clasificar_sueldos():
    print("Clasificar sueldos de los trabajadores!")
    print("Sueldos menores a  800.000$ | Total 1: ")
    for t in lista_trabajadores:
        if t["Sueldo"] <= 800000:
            print(f"Nombre{t['trabajadores']}\nSueldo {t['Sueldo']}\n")
        elif t["Sueldo"] >= 800000 and 2000000: 
            print("Sueldos entre 800.000$ y 2.000.000$ TOTAL 1:")
            for t in lista_trabajadores:
                print(f"Nombre{t['trabajadores']}\nSueldo {t['Sueldo']}\n")
        elif t["Sueldo"] >= 2000000:
            print("Sueldos superiores a 2000000: TOTAL 1: ")
            for t in lista_trabajadores:
                print(f"Nombre{t['trabajadores']}\nSueldo {t['Sueldo']}\n")
                print("TOTAL: ")


    



    






def Reporte_sueldos():
    for t in lista_trabajadores:
        print(f"Nombre {t['trabajadores']}\nSueldo base {t['Sueldo']}\nDescuento Salud {t['Descuento_salud']}\nDescuento AFP {t['Descuento_afp']}\nSueldo liquido {t['Sueldo_liquido']}\n")
        with open("archivo.csv","x",newline="")as archivo:
            escritor = csv.DictWriter(archivo["Nombre","Sueldo","Descuento SALUD","Descuento AFP","Sueldo liquido"])
            escritor.writeheader()
            print("El archivo se ha guardado exitosamente!")

        

    

def ver_estadisticas():
    print("VER ESTADISTICAS")
    for t in lista_trabajadores:
        print("AQUI ESTAN LAS ESTADISTICAS DE CADA TRABAJADOR!")
        print("Sueldo más bajo: ")
        print(f"TRABAJADOR {t['sueldo']}")
        print("Sueldo mas alto:")
        print(f"TRABAJADOR: {t['sueldo']}")
        print("El promedio de los sueldos es: ")
        print(sum())




    
def salir_programa():
    os.system('cls')
    print("FINALIZANDO PROGRAMA....")
    time.sleep(3)
    print("Desarrollado por Sergio castillo")
    print("RUT 21.755.224-9")
    