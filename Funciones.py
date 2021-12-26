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
            contraseña = input(f"Introduce la contraseña para {datos[0]}: ")
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
    time.sleep(.1)
    print(f"\tRegistrarse\n")
    time.sleep(.1)
    usuario = input(f"Introduce tu nombre de usuario: ").strip()
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
            encontrado = False
            mail = input('Ingresa su correo: ')
            try:
                with open('listado_usuarios.txt') as f:
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
                        f = open('listado_usuarios.txt','a')
                        contraseña = input(f"Introduce una contraseña para {usuario}: ")
                        contraseña2 = input(f'Vuelva a ingresar la contraseña: ')
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
        print(f'{datos[0]}\t\t\t{datos[6]}\t\t\t{datos[8]}\t\t\t{datos[10]}\t\t\t{100*PG/PT}')


def marcador0():
    os.system(var)
    partida = 0
    while partida < 6:
        print('\t\nMarcador\n')
        partida = partida + 1
        player1 = 0
        player2 = 0
        P1 = 0
        P2 = 0
        if P1 > P2:
            player1 = player1 + 1
        else:
            pleyer2 = player2 + 1

        condition = True
        
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
    print('\t\nMarcador\n')
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


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

global nuevoGrupo
def crearGrupo():
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
            print('Ese nombre de grupo ya existe, por favor elija otro nombre de grupo')
            stop = input("\tPulsa enter...")
        else:
            condicion = True
            while condicion:
                contraseña = input('Crea una contraseña: ')
                contraseña2 = input('Ingresa de nuevo la contraseña: ')
                if contraseña == contraseña2:
                    e = open('grupos.txt', 'a')
                    e.write(f'{nuevoGrupo}:CONTRASEÑA:{contraseña}')
                    continuar = input()
                    e.close()
                    condicion = False
                else:
                    print('\nLas contraseñas no coinciden, por favor vulve a introducirlas.\n')
                

def unirseGrupo(usuario):
        print(usuario[1][0])
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
                ga = open('grupos.txt', 'a')
                ga.write(f'\n{grupo}:CONTRASEÑA:{contraseña}:usuario:{usuario[1][0]}')
                #texto = str(f'{grupo}:CONTRASEÑA:{contraseña}:usuario:{usuario}')
                #replace_line('grupos.txt', a, texto)
                g.close()
                continuar = input()
            else:
                print('Esa contraseña no coincide con el grupo.')
                continuar = input()
        else:
            print('Ese grupo no existe.')
            continuar = input()




def main(usuario):
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