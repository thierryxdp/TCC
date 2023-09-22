def melhor_volta(matriz):
    minimos = []
    corridas_min = []
    for i in len(matriz):
        minimos.append(min(matriz[i]))
        corridas_min.append(index(min(matriz[i])))
    menor_tempo = min(minimos)
    melhor_corrida = corridas_min[index(min(minimos))] + 1
    return (menor_tempo, melhor_corrida)