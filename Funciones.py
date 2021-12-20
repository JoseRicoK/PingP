import sqlite3

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()

def registro():
    existe = False
    ruta = 'archivo.txt'
    f = open(ruta, 'w')
    archivo = f.readlines()
    f.close()

    usuario = input('Ingresa tu nombre se usuario: ').strip()

    for linea in archivo:
        datos_usuario = linea.split(":")
        if datos_usuario[0] == usuario:
            existe = True
    if existe == True:
        print('Ese usuario ya existe.')
    else:
        existe = False
        archivo = open('archivo.txt')
        mail = input('Ingresa su mail: ').lower().strip()
        for linea in archivo:
            datos_usuario = linea.split(":")
            print(datos_usuario)
            print(datos_usuario[1])
            if datos_usuario[1] == mail:
                existe = True
        if existe == True:
            print('Ese correo ya existe, ingrese otro.')
        else:
            contraseña = input('Ingrese su contraseña: ').strip()
            archivo = open('archivo.txt', 'a')
            archivo.write(f'{usuario}:{mail}:{contraseña}\n')
    archivo.close()

registro()