def media_matriz(matriz):
    '''função que dada uma matriz de números inteiros retorna
    a média dos valores da matriz
    list->int'''
    if matriz==[] and numero==0:
                return 0
    linhas=len(matriz)
    colunas=len(matriz[0])
    soma=0
    for i in range(linhas):
        for j in range(colunas):
             soma+=matriz[i][j]
             media=soma/(linhas*colunas)
    return round(media,2)