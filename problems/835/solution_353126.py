def melhor_volta(matriz):
    tempo = matriz[0][0]
    
    for i in range(len(matriz)):
        melhor_tempo = min(matriz[i])
        if matriz[i] < tempo:
            tempo = melhor_tempo
        corredor = i

    volta = list.index(matriz[corredor], tempo)

    return corredor + 1, tempo, volta + 1