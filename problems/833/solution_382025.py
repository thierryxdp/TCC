def conta_numero(numero,matriz):
    vezes = 0
    linha = len(matriz)
    coluna = len(matriz[0])
    for x in range(linha):
        for y in range(coluna):
            if x in linha:
                vezes += 1
            if y in coluna:
                vezes += 1
    return vezes