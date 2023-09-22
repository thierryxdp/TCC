def conta_numero(numero,matriz):
    vezes = 0
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            if numero in matriz[x]:
                vezes += 1
    return vezes