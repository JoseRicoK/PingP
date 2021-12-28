import os
import time



if os.name == "posix":
    var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"


def login():
    os.system(var)
    time.sleep(.1)
    print(f"\tIniciar sesión\n")
    time.sleep(.1) 
    global usuario
    usuario = input("Introduce tu nombre de usuario: ").strip()
    existe = False
    try:
        with open('usuarios.txt') as f:
            for linea in f:
                datos = linea.split(":")
                if datos[0] == usuario:
                    existe = True
                    break
        f.close()
    except:
            print("Ha ocurrido un error")
    else:
        if existe == True:
            contraseña = input(f"Introduce la contraseña para {datos[0]}: ").strip()
            if datos[2] == contraseña:
                print(f"\nHa iniciado sesión {usuario}\n")
                d = open('Otros.txt', 'w')
                d.write('iniciadoT')
                iniciado = True
                datU = [iniciado, datos]
                return datU
            else:
                print(f"Usuario o contraseña erróneo\n")
                iniciado = False
                return usuario
        else:
            print(f"\nUsuario no encontrado\n")
            iniciado = False
            return usuario
    return usuario

def registro():
    os.system(var)
    time.sleep(.1)
    print(f"\tRegistrarse\n")
    time.sleep(.1)
    usuario = input(f"Introduce un nombre de usuario: ").strip()
    encontrado = False
    try:
        with open('usuarios.txt') as f:
            for linea in f:
                datos = linea.split(":")
                if datos[0] == usuario:
                    encontrado = True
                    break
    except:
            print(f"Ha habido un error :(")
    else:
        if encontrado == True:
            print(f"\nYa existe un usuario con ese nombre, inicia sesión o prueba con otro nombre de usuario")
            continuar = input() 
        else:
            existe = False
            mail = input('Ingresa su correo: ').strip()
            try:
                with open('usuarios.txt') as f:
                    for linea in f:
                        datos = linea.split(":")
                        if datos[4] == mail:
                            existe = True
                            break
            except:
                print('Ha ocurrido un error.')
            else:
                if existe == True:
                    print('Ese correo ya existe, prueba a iniciar sesion o registrarse con otro correo')
                    continuar = input()
                else:
                    condicion = True
                    while condicion:
                        f = open('usuarios.txt','a')
                        contraseña = input(f"Introduce una contraseña para {usuario}: ").strip()
                        contraseña2 = input(f'Vuelva a ingresar la contraseña: ').strip()
                        if contraseña == contraseña2:
                            f.write(f"{usuario}:CONTRASEÑA:{contraseña}:MAIL:{mail}:PARTIDAS JUGADAS:{0}:PARTIDAS GANADAS:{0}:PAERTIDAS PERDIDAS:{0}:\n")
                            print(f"\nUsuario registrado con éxito, inicia sesión para empezar a contar.\n")
                            f.close()
                            condicion = False
                        else:
                            print('\nLas contraseñas no coinciden, por favor vulve a introducirlas.\n')

def ranking():
    os.system(var)
    time.sleep(.4)
    print(f"\tRANKING\n")
    time.sleep(.4)
    print('Ranking Global\n')
    f = open('usuarios.txt', 'r')
    lin = f.readlines()
    print('Jugadores\tPartidas jugadas\tPartidas ganadas\tPartidas perdidas\t   % victoria')
    for linea in lin:
        datos = linea.split(":")
        PT = int(datos[6])
        PG = int(datos[8])
        print(f'{datos[0]}\t\t\t{datos[6]}\t\t\t{datos[8]}\t\t\t{datos[10]}\t\t\t{round(100*PG/PT, 2)}')
    print(' ')
    print('Ranking immune\n')
    print('Jugadores\tPartidas jugadas\tPartidas ganadas\tPartidas perdidas\t   % victoria')
    for linea in lin:
        datos = linea.split(":")
        if datos[11] == 'immune':
            PT = int(datos[6])
            PG = int(datos[8])
            print(f'{datos[0]}\t\t\t{datos[6]}\t\t\t{datos[8]}\t\t\t{datos[10]}\t\t\t{round(100*PG/PT, 2)}')



def marcador0():
    os.system(var)
    partida = 0
    player1 = 0
    player2 = 0
    condicion0 = True
    while condicion0:
        print('\t\nMarcador\n')
        partida = partida + 1

        P1 = 0
        P2 = 0

        condition = True
        
        PM = 10
        while condition:
            if P1 == PM:
                if P2 == PM:
                    PM = PM + 1
            print('Jugador 1 vs Jugador 2')
            print(f'    {P1}          {P2}\n')
            if P1 == (PM + 1):
                if P2 < PM:
                    player1 = player1 + 1
                    print('\nHa ganado el Jugador 1\n')
                    print(f'El Jugador 1 lleva ganando {player1} de {partida}')
                    condition = False
                    a = input('Desea continuar (S/N): ')
                    if a == 's' or a == 'S':
                        if partida < 6:
                            condicion0 = True
                    else:
                        condicion0 = False
            if P2 == (PM + 1):
                if P1 < PM:
                    player2 = player2 + 1
                    print('\nHa ganado el Jugador 2\n')
                    print(f'El Jugador 2 lleva ganando {player2} de {partida}')
                    condition = False
                    a = input('Desea continuar (S/N): ')
                    if a == 's' or a == 'S':
                        if partida < 6:
                            condicion0 = True
                    else:
                        condicion0 = False
            if condition == True:
                puntos = input('Añada punto: ')
            for i in '12345qwertasdfgzxcv':
                if puntos == i:
                    P1 = P1 + 1
            for j in 'yuiophjklñbnm67890':
                if puntos == j:
                    P2 = P2 + 1




def marcador():
    os.system(var)
    print('\t\tMARCADOR\n')
    jugador1 = input('Que jugador va a jugar: ')
    jugador2 = input('Que otro jugador va a jugar: ')
    partida = 0
    a = 0
    player1 = 0
    player2 = 0
    while partida < 6:
        partida = partida + 1


        P1 = 0
        P2 = 0

        condition = True
        while condition:
            os.system(var)
            PM = 10 + a
            if P1 == PM:
                if P2 == PM:
                    a += 1

            print('\t\tMARCADOR\n')
            print(f'\t{jugador1}\t vs \t{jugador2}')
            print(f'\t{P1}\t\t{P2}\n')
            if P1 == (PM + 1):
                if P2 < PM:
                    a=0
                    player1 = player1 + 1
                    print(f'\nHa ganado {jugador1}\n')
                    print(f'{jugador1} lleva ganando {player1} de {partida}')
                    condition = False
                    f = open('usuarios.txt','r')
            
                    contenido_linea = []
                    for linea in f:
                        datos_usuario = linea.split(":")
            
                        if datos_usuario[0] == jugador1:
                            datos_usuario[8] = int(datos_usuario[8]) + 1
                            datos_usuario[6] = int(datos_usuario[6]) + 1
                            insertamos = f"{jugador1}:{datos_usuario[0]}:{datos_usuario[1]}:{datos_usuario[2]}:{datos_usuario[3]}:{datos_usuario[4]}:{datos_usuario[5]}:{datos_usuario[6]}:{datos_usuario[7]}:{datos_usuario[8]}:{datos_usuario[9]}:{datos_usuario[10]}:\n"
                            User_dates = insertamos.split(":")
                        else:
                            insertamos = linea
                        contenido_linea.append(insertamos)
                    f.close()
        
                    f = open('usuarios.txt','w')
                    for ind, val in enumerate(contenido_linea):
                        f.writelines(contenido_linea[ind])
            
                    f.close()



                    f = open('usuarios.txt','r')
            
                    contenido_linea = []
                    for linea in f:
                        datos_usuario = linea.split(":")
            
                        if datos_usuario[0] == jugador2:
                            datos_usuario[10] = int(datos_usuario[10]) + 1
                            datos_usuario[6] = int(datos_usuario[6]) + 1
                            insertamos = f"{datos_usuario[0]}:{datos_usuario[1]}:{datos_usuario[2]}:{datos_usuario[3]}:{datos_usuario[4]}:{datos_usuario[5]}:{datos_usuario[6]}:{datos_usuario[7]}:{datos_usuario[8]}:{datos_usuario[9]}:{datos_usuario[10]}:\n"
                            User_dates = insertamos.split(":")
                        else:
                            insertamos = linea
                        contenido_linea.append(insertamos)
                    f.close()
        
                    f = open('usuarios.txt','w')
                    for ind, val in enumerate(contenido_linea):
                        f.writelines(contenido_linea[ind])
            
                    f.close()

                    return User_dates
            if P2 == (PM + 1):
                if P1 < PM:
                    a=0
                    player2 = player2 + 1
                    print(f'\nHa ganado {jugador2}\n')
                    print(f'El {jugador2} lleva ganando {player2} de {partida}')
                    condition = False
                    f = open('usuarios.txt','r')
            
                    contenido_linea = []
                    for linea in f:
                        datos_usuario = linea.split(":")
            
                        if datos_usuario[0] == jugador2:
                            datos_usuario[8] = int(datos_usuario[8]) + 1
                            datos_usuario[6] = int(datos_usuario[6]) + 1
                            insertamos = f"{datos_usuario[0]}:{datos_usuario[1]}:{datos_usuario[2]}:{datos_usuario[3]}:{datos_usuario[4]}:{datos_usuario[5]}:{datos_usuario[6]}:{datos_usuario[7]}:{datos_usuario[8]}:{datos_usuario[9]}:{datos_usuario[10]}:\n"
                            User_dates = insertamos.split(":")
                        else:
                            insertamos = linea
                        contenido_linea.append(insertamos)
                    f.close()
        
                    f = open('usuarios.txt','w')
                    for ind, val in enumerate(contenido_linea):
                        f.writelines(contenido_linea[ind])
            
                    f.close()



                    f = open('usuarios.txt','r')
            
                    contenido_linea = []
                    for linea in f:
                        datos_usuario = linea.split(":")
            
                        if datos_usuario[0] == jugador1:
                            datos_usuario[10] = int(datos_usuario[10]) + 1
                            datos_usuario[6] = int(datos_usuario[6]) + 1
                            insertamos = f"{datos_usuario[0]}:{datos_usuario[1]}:{datos_usuario[2]}:{datos_usuario[3]}:{datos_usuario[4]}:{datos_usuario[5]}:{datos_usuario[6]}:{datos_usuario[7]}:{datos_usuario[8]}:{datos_usuario[9]}:{datos_usuario[10]}:\n"
                            User_dates = insertamos.split(":")
                        else:
                            insertamos = linea
                        contenido_linea.append(insertamos)
                    f.close()
        
                    f = open('usuarios.txt','w')
                    for ind, val in enumerate(contenido_linea):
                        f.writelines(contenido_linea[ind])
            
                    f.close()
                    stop = input("Pulsa enter...")
                    return User_dates
            if condition == True:
                puntos = input('Añada punto: ')
            for i in '12345qwertasdfgzxcv':
                if puntos == i:
                    P1 = P1 + 1
            for j in 'yuiophjklñbnm67890':
                if puntos == j:
                    P2 = P2 + 1




def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

global nuevoGrupo
def crearGrupo():
    os.system(var)
    encontrado2 = False
    global nuevoGrupo
    nuevoGrupo = input('\nCrea un nombre de grupo: ')
    try:
        with open('grupos.txt') as e:
            for linea in e:
                datos_grupos = linea.split(":")
                if datos_grupos[0] == nuevoGrupo:
                    encontrado2 = True
                    break
    except:
        print('Ha ocurrido un error.')
    else:
        if encontrado2 == True:
            print('\nEse nombre de grupo ya existe, por favor elija otro nombre de grupo')

        else:
            condicion = True
            while condicion:
                contraseña = input('Crea una contraseña: ')
                contraseña2 = input('Ingresa de nuevo la contraseña: ')
                if contraseña == contraseña2:
                    e = open('grupos.txt', 'a')
                    e.write(f'{nuevoGrupo}:CONTRASEÑA:{contraseña}')

                    e.close()
                    condicion = False
                else:
                    print('\nLas contraseñas no coinciden, por favor vulve a introducirlas.\n')
                

def unirseGrupo(usuario):
    os.system(var)
    existe = False
    grupo = input('Ingrese el nombre del grupo: ')
    g = open('grupos.txt', 'r')
    gr = open('usuarios.txt', 'r')
    lin = g.readlines()
    a = 0
    for linea in lin:
        a += 1
        datos = linea.split(":")
        if datos[0] == grupo:
            existe = True
            break
    if existe == True:
        contraseña = input('Ingrese la contraseña: ').strip()
        if datos[2] == contraseña:
            print(f'\nEstás en el grupo {grupo}')
            f = open('usuarios.txt','r')
            
            contenido_linea = []
            for linea in f:
                datos_usuario = linea.split(":")
            
                if datos_usuario[0] == usuario:
                    datos_usuario[11] = grupo
                    insertamos = f"{usuario}:{datos_usuario[0]}:{datos_usuario[1]}:{datos_usuario[2]}:{datos_usuario[3]}:{datos_usuario[4]}:{datos_usuario[5]}:{datos_usuario[6]}:{datos_usuario[7]}:{datos_usuario[8]}:{datos_usuario[9]}:{datos_usuario[10]}:{datos_usuario[11]}:\n"
                    User_dates = insertamos.split(":")
                else:
                    insertamos = linea
                contenido_linea.append(insertamos)
            f.close()
        
            f = open('usuarios.txt','w')
            for ind, val in enumerate(contenido_linea):
                f.writelines(contenido_linea[ind])
            
            f.close()

        else:
            print('Esa contraseña no coincide con el grupo.')
            continuar = input()
    else:
        print('Ese grupo no existe.')





def main(usuario):
        os.system(var)
        print('1 - Partida')
        time.sleep(.1)
        print('2 - Ranking')
        time.sleep(.1)
        print('3 - Juegos')
        time.sleep(.1)
        print('4 - Unirse a un grupo')
        time.sleep(.1)
        print('5 - Crear Grupos')
        time.sleep(.1)
        opcion = input('\nQue desea hacer: ').lower()
        if opcion == '1' or opcion == 'partida':
            marcador()
        elif opcion == '2' or opcion == 'ranking':
            ranking()
        elif opcion == '3' or opcion == 'juegos':
            pass
        elif opcion == '4' or opcion == 'unirse a un grupo':
            unirseGrupo(usuario)
        elif opcion == '5' or opcion == 'crear grupo':
            crearGrupo()


def main1():
    try:
        with open('Otros.txt') as o:
            for linea in o:
                datos = linea.split(":")
                if datos[0] == 'loggedT':
                    iniciadoS = True
                    break
    except:
            print(f"Ha ocurrido un ")
    else:
        if iniciadoS == True:
            print('1 - Partida')
            time.sleep(.1)
            print('2 - Ranking')
            time.sleep(.1)
            print('3 - Juegos')
            time.sleep(.1)
            print('4 - Unirse a un grupo')
            time.sleep(.1)
            print('5 - Crear Grupos')
            time.sleep(.1)
            opcion = input('\nQue desea hacer: ').lower()
        if opcion == '1' or opcion == 'partida':
            pass
        elif opcion == '2' or opcion == 'ranking':
            pass
        elif opcion == '3' or opcion == 'juegos':
            pass
        elif opcion == '4' or opcion == 'unirse a un grupo':
            pass
        elif opcion == '5' or opcion == 'crear grupo':
            pass