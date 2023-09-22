def media_matriz(matriz):
    '''Calcula a média da soma dos valores de uma matriz com
    a quantidade de termos'''
    '''List -> float'''
    soma = 0
    total = 0
    for i in matriz:
        for j in i:
            soma += j
        total += len(i)
    return round(soma/total, 2)