def conta_numero(numero,matriz):
    Vezes = 0
    linha = len(matriz)
    coluna = len(matriz[0])
    if matriz == []:
        return Vezes
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] == numero:
                Vezes +=1
    return Vezes