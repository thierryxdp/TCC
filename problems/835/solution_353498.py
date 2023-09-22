def melhor_volta(matriz6por10):
    '''função que recebe uma matriz 6x10 e retorna uma tupla
       com de quem foi a melhor volta, com qual tempo e em que
       volta.
       list(list) ---> tuple '''
    melhor_tempo = matriz6por10[0][0]
    melhor_corredor = 0
    melhor_volta = 0
    for a in range(6):
        tempo_corredor = matriz[a]
        tempo_min_corredor = min(tempo_corredor)
        if tempo_corredor < melhor_tempo:
            melhor_tempo = tempo_corredor