def conta_numero(numero,matriz):
    vezes = 0
    linha = len(matriz)
    coluna = len(matriz[0])
    for x in range(coluna):
        if numero in matriz[x][y]:
            vezes += 1
    return vezes