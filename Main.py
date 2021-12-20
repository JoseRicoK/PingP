import Funciones
import time

usuarios = {'gaboss':'tumama', 'jositomac':'orroy'}
print('Bienvenidos a Ping Count')
print('1. Iniciar sesión ')
time.sleep(.3)
print('2. Registro ')
time.sleep(.5)
print('3. Partida Rápida ')
time.sleep(.7)
opcion = int(input('Que desea hacer: '))
if opcion == 1:
    usuario = input('ingrese su nombre: ')
    if usuario in usuarios:
        contraseña = input('Ingresar contraseña: ')
        if contraseña in usuarios[usuario]:
            print('jamon')
        else:
            print('No eres nadie')
    else:
        print('no existes en mi vida')
elif opcion == 2:
    nuevo_usuario = input('Ingrese su nombre: ')
    if nuevo_usuario not in usuarios:
        mail = input('Ingrese su correo: ')

       