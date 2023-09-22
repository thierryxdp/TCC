def conta_numero(numero, matriz):
    linha = len(matriz)
    if linha == 0:
        return 0
    coluna = len(matriz[0])
    quantidade = 0
    for i in range(linha):
        for j in range(coluna):
            elemento = matriz[i][j]
            if numero == elemento:
                quantidade = quantidade + 1
    
    return quantidade