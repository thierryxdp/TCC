def melhor_volta(M):
    """ dada uma matriz 6x10 (6 competidores, 10 voltas), função
    retorna jogador com melhor volta, em que volta e melhor tempo. """

    tupla = (0,0,0)
    for i in range(6):
        for j in range(10):
            if M[i][j] < tupla[1]:
                tupla = (i+1,1,j+1)

    return tupla