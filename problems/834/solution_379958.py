def media_matriz(matriz):
    '''retorna a media de uma matriz de numeros inteiros nao vazia
    list->float'''
    divisor=len(matriz)*len(matriz[0])
    soma = 0
    for i in matriz:
        for j in i:
            soma += j
    return round(soma/divisor,2)