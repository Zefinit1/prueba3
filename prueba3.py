
import json


nombre = ""

apellido = ""

mesero = ""

cargo = ""

cocinero = ""

cajero = ""

sueldo_bruto = 0

sueldo_liquido = 0

descuento_salud = 0

descuento_AFP = 0
opc = 0


while True:
    print("menu")
    print("1. Registrar trabajador")
    print("2. Listar trabajadores")
    print("3. Imprimir planilla")
    print("4. Salir")


    opc = int(input("ingrese opcion: "))

    if opc == 1:
        nombre = input("ingrese su nombre: ")
        apellido = input("ingrese su apellido: ")
        print("menu")
        print("1. mesero")
        print("2. cocinero")
        print("3. cajero")
        cargo = input("ingrese su cargo: ")
            
        sueldo_bruto = int(input("ingrese su sueldo bruto: "))

        descuento_salud = sueldo_bruto * 0.7
        print("el descuento de salud es: ", descuento_salud)

        descuento_AFP = sueldo_bruto * 0.10
        print("el descuento de afp es: ", descuento_AFP)

        sueldo_liquido = sueldo_bruto + descuento_AFP - descuento_salud
        print("su sueldo liquido es: ", sueldo_liquido)    

    elif opc == 2:
        print(nombre)
        print(apellido)
        print(cargo)
        print(sueldo_bruto)
        print(descuento_salud)
        print(descuento_AFP)
        print(sueldo_liquido)

    elif opc == 3:
        print("1. mesero")
        print("2. cocinero")
        print("3. cajero")

        cargo = input(cargo)
        if opc == 1:
            print(nombre)
            print(apellido)
            print(cargo)
            print(sueldo_bruto)
            print(descuento_salud)
            print(descuento_AFP)
            print(sueldo_liquido)

        if opc == 2:
            print(nombre)
            print(apellido)
            print(cargo)
            print(sueldo_bruto)
            print(descuento_salud)
            print(descuento_AFP)
            print(sueldo_liquido)
        if opc == 3:
            print(nombre)
            print(apellido)
            print(cargo)
            print(sueldo_bruto)
            print(descuento_salud)
            print(descuento_AFP)
            print(sueldo_liquido)        

    elif opc == 4:
        print("Has salido")
        break    





