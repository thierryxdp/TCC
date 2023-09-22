def conta_numero(numero,matriz):
    vezes = 0
    for x in range((len(matriz))*(len(matriz[0]))):
        for y in range((len(matriz))*(len(matriz[0]))):
            if numero in matriz[x][y]:
                vezes += 1
    return vezes