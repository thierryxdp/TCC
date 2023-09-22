def melhor_volta(matriz6por10):
    '''função que recebe uma matriz 6x10 e retorna uma tupla
       com de quem foi a melhor volta, com qual tempo e em que
       volta.
       list(list) ---> tuple '''
    voltas = len(matriz6por10)
    melhor_tempo = matriz6por10[0][0]
    melhor_corredor = 0
    for a in range(6):
        b = 0
        tempo_corredor = matriz6por10[a]
        tempo_min_corredor = min(tempo_corredor)
        if tempo_min_corredor < melhor_tempo:
            melhor_tempo = tempo_min_corredor
            melhor_corredor = a + 1
        while b < voltas:
            melhor_volta = list.index(matriz6por10[melhor_corredor], melhor_tempo)        
    return (melhor_corredor, melhor_volta, melhor_tempo)