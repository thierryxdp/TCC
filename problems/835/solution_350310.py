def melhor_volta(matriz_tempos):
    '''função que recebe matriz de voltas 
    com tempos e verifica quem fez a melhor volta, com que
    tempo e em que volta, e retorna tupla com dados nessa ordem
    list--> tuple'''

    tupla = (0, float('inf'), 0)

    for volta in range(6):
        for tempo in range(10):
            if matriz_tempos[volta][tempo] < tupla[1]:

                tupla = (volta + 1, matriz_tempos[volta][tempo], tempo+1) 

    return tupla