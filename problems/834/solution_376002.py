def media_matriz(matriz):
    '''
    A função retorna a media de todos
    os valores.
    list -> float
    '''
    media = 0
    soma =0
    linha = len(matriz)
    coluna = len(matriz[0])
    for l in range(linha):
        for c in range(coluna):
            soma += matriz[l][c]
            media = round(soma/(linha+coluna),2)
    return media