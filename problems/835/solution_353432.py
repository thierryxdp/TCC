def melhor_volta(matriz):
    tempo = numVolta = melhorV = 1000
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            if min(matriz[v][t], menor_tempo) == matriz[v][t]:
                tempo = min(matriz[v][t], melhorV)
                melhorV = v + 1
                numVolta = t + 1

    return melhorV, tempo, numVolta