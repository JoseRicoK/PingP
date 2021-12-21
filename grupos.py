grupos = {'Immuners':'schoola','prudencio':'spendtime'}

print('1.Ingresar a grupo ')
print('2.Crear grupo ')
opcion = int(input('¿Qué desea hacer? '))
if opcion == 1:
    grupo = input('Ingrese nombre del grupo ')
    if grupo in grupos:
        contraseña = input('Ingrese contraseña ')
        if contraseña in grupos[grupo]:
            print('bacon')
        else:
                print('No son nadie. ')
    else:
        print('No existen en mi vida')
elif opcion == 2:
    nuevo_grupo = input('Crea nombre del grupo ')
    contraseña = input('Crea contraseña ')
    


