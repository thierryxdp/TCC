def media_matriz(matriz):
    '''Calcula e retorna a média dos elementos de uma matriz
    com 2 casas de precisão
    mat->float'''
    soma=0
    qtd=0
    for lin in matriz:
        for elemento in lin:
            soma=soma+elemento
            qtd=qtd+1
    return round(soma/qtd,2)