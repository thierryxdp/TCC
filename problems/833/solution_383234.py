def conta_numero(numero,matriz):
    Vezes = 0
    if matriz == []:
        return Vezes
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] == numero:
                Vezes +=1
    return Vezes