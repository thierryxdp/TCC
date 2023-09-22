def melhor_volta (matriz):
    minimo = []
    for n in range (len(matriz)):
        minimo += [min(matriz[n])]
    melhor = list.index (minimo,min(minimo))
    volta = list.index (matriz[melhor],min(minimo))
    return melhor + 1, min(minimo), volta + 1