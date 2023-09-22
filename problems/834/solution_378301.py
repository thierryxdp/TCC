def media_matriz(matriz):
    '''Coloque uma matriz e o resultado será a média aritmética de todos os elementos dela
       list->float'''
    num=0
    contador=0
    for i in matriz:
        for aij in i:
            num = num + aij
            contador=contador + 1
    return round(num/contador, 2)