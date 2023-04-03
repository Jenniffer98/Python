# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 09:42:12 2022

@author: Jenniffer
"""

from conexion_oracle import conexion_bd_oracle


def get_value(trama, campo, separador):

    dummy = ""
    #posicion_inicial = trama.index(campo + '=', 0, len(trama))
    posicion_inicial = trama.find(campo + '=')

    if posicion_inicial > 0:
        dummy = trama[posicion_inicial:]
        posicion_final = dummy.find(separador)

        if posicion_final > 0:
            dummy = dummy[0: posicion_final]

        dummy = dummy[dummy.index('=')+1:]

    return dummy


def registrarCliente():
    cedula = input("Ingrese Identificacion:")
    nombre = input("Ingrese Nombre:")
    apellido = input("Ingrese Apellido:")
    direccion = input("Ingrese Direccion:")
    fecha_nac = input("Ingresa Fecha Nacimiento:")
    telefono = input("Ingresa telefono:")
    email = input("Ingresa correo:")
    categoria = input("Ingresa Categoria:")

    client = ("Los datos Ingresados son:"+cedula, nombre, apellido, direccion,
              fecha_nac, telefono, email, categoria)
    print(client)
    conn, cursor = conexion_bd_oracle('BSCS', 'sysadm', 'sysadm')
    sql = "SELECT CLK_DETALLE_FACTURA_CLIENTE.CLF_INGRESA_CLIENTE('"+cedula+''+nombre+''+apellido+''+direccion+''+fecha_nac+''+telefono+''+email+''+categoria+"') AS RESPUESTA FROM DUAL"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)


def consultar(identificacion):

    conn, cursor = conexion_bd_oracle('BSCS', 'sysadm', 'sysadm')
    sql = "SELECT CLK_DETALLE_FACTURA_CLIENTE.CLF_CONSULTA_CLIENTE('" +identificacion+"')  FROM DUAL"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)


def eliminar():
    identificacion = input('Ingrese la Cedula para consultar:')
    conn, cursor = conexion_bd_oracle('BSCS', 'sysadm', 'sysadm')
    sql = "SELECT CLK_DETALLE_FACTURA_CLIENTE.CLF_ELIMINA_CLIENTE('" + \
        identificacion+"') AS RESPUESTA FROM DUAL"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    print("Se elimino el cliente")


def actualizar():
    identificacion = input('Ingrese la Cedula para consultar: ')
    print("Ingrese el campo a actualizar")
    direccion = input("Ingrese Direccion si va actualizar:")
    telefono = input("Ingresa telefono si va a actualizar:")
    categoria = input("Ingresa Categoria si va actualizar:")
    conn, cursor = conexion_bd_oracle('BSCS', 'sysadm', 'sysadm')
    sql = "SELECT CLK_DETALLE_FACTURA_CLIENTE.CLF_UPDATE_CLIENTE('" + \
        identificacion+"') AS RESPUESTA FROM DUAL"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)


def menu():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while (not opcionCorrecta):
            print("===MENÚ PRINCIPAL====")
            print("1.- Consultar")
            print("2.- Registrar")
            print("3.- Actualizar")
            print("4.- Eliminar")
            print("5.- Salir")
            print("================")
            opcion = int(input("Selecciona una opcion:"))
            if opcion < 1 or opcion > 5:
                print("Opcion incorrecta, ingrese nuevamente:")
            elif opcion == 1:
                identificacion = input('/nIngrese la Cedula para consultar: ')
                consultar(identificacion)
                
            elif opcion == 2:
               registrarCliente()
            elif opcion == 3:
               actualizar()
            elif opcion == 4:
               eliminar()
            elif opcion == 5:
                continuar = False
                print("Gracias por usar el sistema")
                break
            else:
                opcionCorrecta = True


def ejecutarOpcion(opcion):
    print(opcion)


if __name__ == '__main__':
    try:
        menu()

    except Exception as e:
        print("Error : " + str(e))
