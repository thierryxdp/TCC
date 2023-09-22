def melhor_volta(matriz):
    melhor_tempo = matriz[0][0]
    
    for i in range(len(matriz)):
        melhor_tempo = min(matriz[i], melhor_tempo)
        corredor = i

    volta = list.index(matriz[corredor], melhor_tempo)

    return corredor + 1, melhor_tempo, volta + 1