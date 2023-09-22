def media_matriz(matriz):
    """Dado uma matriz não vazia, retorna a media dos seus elementos:
    list(list)-->float"""
    linha_matriz=len(matriz)
    coluna_matriz=len(matriz[0])
    soma=0
    for i in range(linha_matriz):
        for j in range(coluna_matriz):
            soma+=matriz[i][j]
    return round(soma/(linha_matriz*coluna_matriz),2)