def media_matriz(matriz):
    """Dado uma matriz de inteiros nao vazia, retorna a media dos numeros
    list->int"""
    nlin=len(matriz)
    ncol=len(matriz[0])
    numeros=0
    soma=0
    for i in range(nlin):
        for j in range(ncol):
            soma=soma+matriz[i][j]
            numeros=numeros+1
    return round(soma/numeros,2)