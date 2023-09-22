def melhor_volta(matriz):
    ''' Essa função tem como objetivo buscar a melhor volta, quem foi o corredor, e
    e em que volta dado os resultados em uma matriz, contendo os tempos de cada um.'''
    '''list(list) -> tuple'''
    melhor_tempo = matriz[0][0]
    
    for i in range(len(matriz)):
        tempos_corredor = matriz[1]
        tempo_corredor = min(tempos_corredor)
        if tempo_corredor <= melhor_tempo:
            melhor_corredor = 1 
    volta = list.index(matriz[melhor_corredor], melhor_tempo)
    return melhor+corredor +1, melhor_tempo,volta+1