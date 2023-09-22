def melhor_volta(matriz):
    menor_tempo = 0
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            menor_tempo = min(matriz[t])

    return menor_tempo