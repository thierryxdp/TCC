def melhor_volta(matriz):
    '''retorna a volta mais rapida da corrida
    list(list) -> int'''
    melhor_tempo = matriz[0][0]
    for i in range(len(matriz)):
        tempos_do_corredor = matriz[i]
        tempo_corredor = min(tempos_do_corredor)
        if tempo_corredor <= melhor_tempo:
            melhor_tempo = tempo_corredor
            melhor_corredor = i
    volta = list.index(matriz(melhor_corredor), melhor_tempo)
    return melhor_corredor + 1, melhor_tempo, volta + 1