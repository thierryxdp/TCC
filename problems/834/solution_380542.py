def media_matriz(matriz):
    '''
    função que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz;
    list(list) -> float
    '''
    soma = 0
    total_elem = len(matriz) * len(matriz[0])
    for linha in matriz:
        for aij in linha:
            soma =soma + aij
    return soma/total_elem