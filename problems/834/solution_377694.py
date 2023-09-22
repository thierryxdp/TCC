def media_matriz(matriz):
    '''
    Função que dada uma matriz de inteiros não vazia, retorna
    a média de todos os números com exatamente duas casas
    decimais de precisão.
    
    list -> float
    '''
    a = 0
    for b in matriz:
        a = a + sum(b)
    q = len(matriz)*len(matriz[0])
    return round(a/q, 2)