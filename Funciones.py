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
                d = open('Otros.txt', 'w')
                d.write('loggedT')
                logged = True
                logged_User = [logged, datos_usuario]
                return logged
            else:
                print(f"Usuario o contraseña erróneo\n")
                stop = input("Pulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 
                logged = False
                logged_User = [logged, datos_usuario]
                return logged
        else:
            print(f"\nUsuario no encontrado\n")
            stop = input("Pulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 
            logged = False
            datos_usuario = []
            logged_User = [logged, datos_usuario]
            return logged

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
                            f.write(f"{usuario}:CONTRASEÑA:{contraseña}:MAIL:{mail}:PARTIDAS JUGADAS:{0}:PARTIDAS GANADAS:{0}:PAERTIDAS PERDIDAS:{0}:\n")
                            print(f"\nUsuario registrado con éxito, inicia sesión para empezar a contar.\n")
                            stop = input("Pulsa enter...")
                            f.close()
                            condicion = False
                        else:
                            print('\nLas contraseñas no coinciden, por favor vulve a introducirlas.\n')

def ranking():
    os.system(var)
    time.sleep(.4)
    print(f"\t\t\t\tRANKING\n")
    time.sleep(.4)
    print('Ranking Global\n')
    f = open('listado_usuarios.txt', 'r')
    lin = f.readlines()
    print('Jugadores\tPartidas jugadas\tPartidas ganadas\tPartidas perdidas\t % victoria')
    for linea in lin:
        datos_usuario = linea.split(":")
        PT = int(datos_usuario[6])
        PG = int(datos_usuario[8])
        print(f'{datos_usuario[0]}\t\t\t{datos_usuario[6]}\t\t\t{datos_usuario[8]}\t\t\t{datos_usuario[10]}\t\t\t{100*PG/PT}')


def marcador0():
    os.system(var)
    partida = 0
    while partida < 6:
        partida = partida + 1
        player1 = 0
        player2 = 0
        if P1 > P2:
            player1 = player1 + 1
        else:
            pleyer2 = player2 + 1

        condition = True
        P1 = 0
        P2 = 0
        PM = 10
        PM = 10
        while condition:
            print('Jugador 1 vs Jugador 2')
            print(f'    {P1}          {P2}\n')
            if P1 == (PM + 1):
                if P2 < PM:
                    print('\nHa ganado el Jugador 1\n')
                    condition = False
                    stop = input('Pulsa enter para continuar...\n')
            if P2 == (PM + 1):
                if P1 < PM:
                    print('\nHa ganado el Jugador 2\n')
                    condition = False
                    stop = input('Pulsa enter para continuar...\n')
            if condition == True:
                puntos = input('añada punto ')
            for i in '12345qwertasdfgzxcv':
                if puntos == i:
                    P1 = P1 + 1
            for j in 'yuiophjklñbnm67890':
                if puntos == j:
                    P2 = P2 + 1

        if P1 == PM:
            if P2 == PM:
                PM = PM + 1


def marcador():
    os.system(var)
    jugador1 = input('Que jugador va a jugar: ')
    jugador2 = input('Que otro jugador va a jugar: ')
    partida = 0
    while partida < 6:
        partida = partida + 1
        player1 = 0
        player2 = 0
        if P1 > P2:
            player1 = player1 + 1
        else:
            player2 = player2 + 1

        condition = True
        P1 = 0
        P2 = 0
        PM = 10
        PM = 10
        while condition:
            print(f'\t{jugador1}\t vs \t{jugador2}')
            print(f'\t{P1}\t\t{P2}\n')
            if P1 == (PM + 1):
                if P2 < PM:
                    print('\nHa ganado el Jugador 1\n')
                    condition = False
                    stop = input('Pulsa enter para continuar...\n')
            if P2 == (PM + 1):
                if P1 < PM:
                    print('\nHa ganado el Jugador 2\n')
                    condition = False
                    stop = input('Pulsa enter para continuar...\n')
            if condition == True:
                puntos = input('añada punto ')
            for i in '12345qwertasdfgzxcv':
                if puntos == i:
                    P1 = P1 + 1
            for j in 'yuiophjklñbnm67890':
                if puntos == j:
                    P2 = P2 + 1

        if P1 == PM:
            if P2 == PM:
                PM = PM + 1


def main():
        os.system(var)
        print('1 - Partida')
        time.sleep(.5)
        print('2 - Ranking')
        time.sleep(.5)
        print('3 - Juegos')
        time.sleep(.5)
        print('4 - Unirse a un grupo')
        time.sleep(.5)
        print('5 - Crear Grupos')
        time.sleep(.5)
        opcion = input('\nQue desea hacer: ').lower()
        if opcion == '1' or opcion == 'partida':
            pass
        elif opcion == '2' or opcion == 'ranking':
            ranking()
        elif opcion == '3' or opcion == 'juegos':
            pass
        elif opcion == '4' or opcion == 'unirse a un grupo':
            pass
        elif opcion == '5' or opcion == 'crear grupo':
            pass
def main1():
    try:
        with open('Otros.txt') as o:
            for linea in o:
                datos = linea.split(":")
                if datos[0] == 'loggedT':
                    iniciadoS = True
                    break
    except:
            print(f"Ha habido un error")
    else:
        if iniciadoS == True:
            print('1 - Partida')
            time.sleep(.5)
            print('2 - Ranking')
            time.sleep(.5)
            print('3 - Juegos')
            time.sleep(.5)
            print('4 - Unirse a un grupo')
            time.sleep(.5)
            print('5 - Crear Grupos')
            time.sleep(.5)
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