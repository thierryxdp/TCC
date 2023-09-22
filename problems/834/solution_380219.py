def media_matriz(matriz_int):
    '''Dada uma matriz de inteiros não vazia, retorna a media de todos os números da matriz'''
    nlinhas=len(matriz_int)
    ncolunas=len(matriz_int[0])
    nelem= nlinhas*ncolunas
    soma=0
    for i in range (nlinhas):
        for j in range (ncolunas):
            soma+=matriz[i][j]
    return round (soma/nelementos,2)