def melhor_volta(matriz):
    '''Retorna uma tupla informando quem foi o vencedor da prova.
    list-->tuple'''
    melhor_tempo=matriz[0][0]
    corredor=0
    for i in range(len(matriz)):  
        melhor_tempo_novo=min(matriz[i])
        if melhor_tempo_novo < melhor_tempo:
            melhor_tempo=melhor_tempo_novo
            corredor=i + 1
    volta= volta.index(matriz[corredor,melhor_tempo])+1
    return corredor,melhor_tempo,volta