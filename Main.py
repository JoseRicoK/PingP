import Funciones
import time

while True:
    print('\nBienvenidos a Ping Count\n')
    print('1. Iniciar sesión ')
    time.sleep(.3)
    print('2. Registro ')
    time.sleep(.5)
    print('3. Partida Rápida ')
    time.sleep(.7)
    opcion = input('\nQue desea hacer: ')
    if opcion == '1' or opcion == 'Iniciar sesion':
        Funciones.login()
        
    elif opcion == '2' or opcion == 'Registro':
        Funciones.registro()
    elif opcion == '3' or opcion == 'Juego libre':
        pass