def melhor_volta(matriz):
    tempos = []
    for i in range(len(matriz)):
        tempo = 0
        for j in range(len(matriz[0])):
            tempo += matriz[i][j]
        list.append(tempos,tempo)
    melhor_tempo = min(tempo)
    return melhor_tempo