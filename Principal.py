import Funciones
import time
import os

if os.name == "posix":
    var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"

while True:
    os.system(var)
    print('\nBienvenidos a Ping Point\n')
    print('1. Iniciar sesión ')
    time.sleep(.1)
    print('2. Registro ')
    time.sleep(.1)
    print('3. Partida Rápida ')
    time.sleep(.1)
    opcion = input('\nQue desea hacer: ')
    if opcion == '1' or opcion == 'Iniciar sesion':
        usuario = Funciones.login()
        condicion = True
        while condicion:
            condicion = False
            Funciones.main(usuario)
            a = input('\n\nDesea continuar (S/N): ')
            if a == 's' or a == 'S':
                condicion = True
    elif opcion == '2' or opcion == 'Registro':
        Funciones.registro()
    elif opcion == '3' or opcion == 'Juego libre':
        Funciones.marcador0()