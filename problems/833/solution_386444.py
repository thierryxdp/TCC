def conta_numero(numero,matriz):
    soma=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j]==numero:
                soma+=1
    return soma