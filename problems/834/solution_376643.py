def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros não vazia, calcula e retorna a médi
    dos elementos da matriz(com 2 casas de precisão). Entrada:list. Saída: float.'''
    lista1=[]
    n_elementos=0
    soma=0
    for L in range(len(matriz)):
        for C in range(len(matriz[L])):
            soma+=matriz[L][C]
            n_elementos = n_elementos + 1
    return round(soma/n_elementos,2)