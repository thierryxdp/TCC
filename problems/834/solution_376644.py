media_matriz(matriz):
    soma = 0
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in linha:
        for j in coluna:
            soma = soma + matriz[i][j]
    
    return soma/(i*j)