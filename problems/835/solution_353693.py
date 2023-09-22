def melhor_volta(matriz):
    '''a função lê a matriz com os tempos de volta dos corredores e retorna o melhor corredor, o melhor tempo e a melhor volta. Matriz->tuple'''
    melhor_tempo = matriz[0][0]
    melhor_corredor = 0
    melhor_volta = 0
    for i in range(6):
        tempos_corredor = matriz[i]
        tempo_corredor = min(tempos_corredor)
        if tempo_corredor < melhor_tempo:
            melhor_tempo = tempo_corredor
            melhor_corredor = i
    melhor_volta = list.index(matriz[melhor_corredor], melhor_tempo)
    return melhor_corredor + 1, melhor_tempo, melhor_volta +1