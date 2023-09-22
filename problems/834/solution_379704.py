def media_matriz(matriz):
    '''
    Função que dada uma matriz de inteiros não vazia, retorna a média
    de todos os números da matriz
    '''
    qtdnumeros = len(matriz)*len(matriz[0])
    soma=0
    linhas=0
    for linha in matriz:
        for numero in matriz[linhas]:
            soma += numero
        linhas+=1
    return round(soma/qtdnumeros,2)