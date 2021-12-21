partida = 0
while partida < 6:
    partida = partida + 1
    player1 = 0
    player2 = 0

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
