import os
import time

if os.name == "posix":
    var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"

def login():
    os.system(var)
    time.sleep(.4)
    print(f"\t\t\t\tIniciar sesión\n")
    time.sleep(.4)
    usuario = input(f"Introduce tu nombre de usuario: ").strip()
    encontrado = False
    try:
        with open('listado_usuarios.txt') as f:
            for linea in f:
                datos_usuario = linea.split(":")
                if datos_usuario[0] == usuario:
                    encontrado = True
                    break
        f.close()
    except:
            print("Ha ocurrido un error")
    else:
        if encontrado == True:
            contraseña = input(f"Introduce la contraseña para {datos_usuario[0]}:\t")
            valores_usuario = datos_usuario[1].split(":")
            
            if datos_usuario[2] == contraseña:
                print(f"\nBienvenido {usuario}, has iniciado sesión satisfactoriamente!!\n")
                stop = input("Pulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 
                logged = True
                logged_User = [logged, datos_usuario]
                return logged_User
            else:
                print(f"Usuario o contraseña erróneo\n")
                stop = input("Pulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 
                logged = False
                logged_User = [logged, datos_usuario]
                return logged_User
        else:
            print(f"\nUsuario no encontrado\n")
            stop = input("Pulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 
            logged = False
            datos_usuario = []
            logged_User = [logged, datos_usuario]
            return logged_User

def registro():
    os.system(var)
    time.sleep(.4)
    print(f"\t\t\t\tRegistrarse\n")
    time.sleep(.4)
    usuario = input(f"Introduce tu nombre de usuario: ").lower().strip()
    encontrado = False
    try:
        with open('listado_usuarios.txt') as f:
            for linea in f:
                datos_usuario = linea.split(":")
                if datos_usuario[0] == usuario:
                    encontrado = True
                    break
    except:
            print(f"Ha habido un error :(")
    else:
        if encontrado == True:
            print(f"\nYa existe un usuario con ese nombre, inicia sesión o prueba con otro nombre de usuario")
            stop = input("Pulsa enter...") 
        else:
            encontrado = False
            mail = input('Ingresa su correo: ')
            try:
                with open('listado_usuarios.txt') as f:
                    for linea in f:
                        datos_usuario = linea.split(":")
                        if datos_usuario[4] == mail:
                            encontrado = True
                            break
            except:
                print('Ha ocurrido un error.')
            else:
                if encontrado == True:
                    print('Ese correo ya existe, prueba a iniciar sesion o registrarse con otro correo')
                    stop = input("\tPulsa enter...")
                else:
                    condicion = True
                    while condicion:
                        f = open('listado_usuarios.txt','a')
                        contraseña = input(f"Introduce una contraseña para {usuario}: ")
                        contraseña2 = input(f'Vuelva a ingresar la contraseña: ')
                        if contraseña == contraseña2:
                            f.write(f"{usuario}:CONTRASEÑA:{contraseña}:MAIL:{mail}:\n")
                            print(f"\nUsuario registrado con éxito, inicia sesión para empezar a contar.\n")
                            stop = input("Pulsa enter...")
                            f.close()
                            condicion = False
                        else:
                            print('\nLas contraseñas no coinciden, por favor vulve a introducirlas.\n')
