def conta_numero(numero,matriz):
    soma=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in linha:
        for j in coluna:
            if matriz[i][j]==numero:
                soma+=1
    return soma