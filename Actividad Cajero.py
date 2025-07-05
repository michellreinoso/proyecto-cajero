# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 20:19:11 2025

@author: LENOVO
"""

import numpy as np

lista_nombres = [ "Sofía", "Mateo", "Isabella", "Lucas", "Valentina", "Alejandro", "Emma", "Santiago", "Martina",
    "Sebastián", "Camila", "Nicolás", "Valeria", "Gabriel", "Antonella", "Daniel", "Lucía", "Andrés",
    "Renata", "Adrián", "Sara", "Diego", "Julieta", "Joaquín", "Paula", "Leonardo", "Victoria", "Benjamín",
    "María", "Samuel", "Elia", "David", "Elena", "Maximiliano", "Montserrat", "Ángel", "Regina", "Tomás",
    "Jimena", "Cristóbal", "Fernanda", "Bruno", "Ana", "Ricardo", "Ximena", "Gael", "Andrea", "Matías", "Carolina",
    "Thiago", "Daniela", "Emilio", "Alicia", "Jerónimo", "Natalia", "Dylan", "Claudia", "Iker", "Patricia",
    "Iván", "Alejandra", "Alan", "Laura", "Franco", "Gabriela", "Jesús", "Mariana", "Rodrigo", "Lorena", "Martín",
    "Melissa", "Juan", "Paola", "Carlos", "Diana", "Pedro", "Carmen", "Miguel", "Rosa", "Jorge", "Gloria", "Luis",
    "Silvia", "Antonio", "Isabel", "José", "Esther", "Manuel", "Beatriz", "Francisco", "Raquel", "Javier", "Susana",
    "Raúl", "Pilar", "Alberto", "Eva", "Enrique", "Dolores", "Sergio", "Mercedes", "Óscar", "Cristina", "Julio",
    "Rosario"]

dict_users = { i: np.random.randint(10000, 500000) for i in lista_nombres }
dict_claves = {i: i + "123" for i in lista_nombres}

# Con un arreglo
#for i_name in lista_nombres:
#    dict_users[i_name.lower()] = [ np.random.randint(10000, 500000), f'{i_name.lower}_1']

str_nombre = ''

for enu, i_name in enumerate(lista_nombres):
    str_nombre = str_nombre + f'\n{enu}: ' + i_name
    
while True:
    try:
        seleccion = int(input(f'¿Usted quién es?: {str_nombre}\n105: SALIR\n'))
    
    except:
        print('Ingreso una seleccion no valida') 
        continue
        
    seleccion_cliente = lista_nombres[seleccion]
    print(f' Bienvenido(a) {seleccion_cliente}')
    
    intentos = 2
    while intentos > 0:
        clave_ingresada = input('Ingrese su clave: ')
        if clave_ingresada == dict_claves[seleccion_cliente]:
            print("Acceso concedido.")
            break
        else:
            intentos -= 1
            print(f"Clave incorrecta. Le quedan {intentos} intentos.")

    if intentos == 0:
        print("Clave ingresada erronea. Adios")
        break

    if seleccion in range(len(lista_nombres)):

        while True:
            operaciones = int(input('¿Qué quiere hacer?:\n0: Ver\n1: Retirar\n2: Consignar\n3: SALIR\n'))

            saldo_cuenta_usuario = dict_users[seleccion_cliente]

            # Ver
            if operaciones == 0:
                print(saldo_cuenta_usuario)

            # Retirar
            elif operaciones == 1:
                valor_retiro = int(input('¿Cuánto quiere retirar: '))

                if valor_retiro <= saldo_cuenta_usuario:
                    print('Retiro exitoso')
                    dict_users[seleccion_cliente] = saldo_cuenta_usuario - valor_retiro
                    print('Su saldo es: ', dict_users[seleccion_cliente])

            # Consignar
            elif operaciones == 2:
                valor_consignar = int(input('¿Cuánto quiere consignar: '))
                dict_users[seleccion_cliente] = saldo_cuenta_usuario + valor_consignar

            else:
                break

    elif seleccion == 105:
        break

    else:
        print('Error: no seleccionó una opción válida')
        


