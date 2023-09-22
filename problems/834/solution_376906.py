def media_matriz(m):
    '''Retorna a média aritmética dos números de uma matriz
list -> float'''
    soma = 0
    n = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            soma += m[i][j]
            n += 1
    return round(soma/n,2)