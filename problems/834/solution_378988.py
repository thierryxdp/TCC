def media_matriz(matriz):
    """função que recebe uma matriz e retorna a média de todos
       os números da matriz
       list->float"""
    nlin=len(matriz)
    ncol=len(matriz[0])
    numeros=0
    soma=0
    for i in range(nlin):
        for j in range(ncol):
            soma=soma+matriz[i][j]
            numeros=numeros+1
    return round(soma/numeros,2)