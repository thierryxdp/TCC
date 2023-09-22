def media_matriz(m):
    '''função que calcula e retorna a média de todos os números da matriz. list(list)->float'''
    soma = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            soma = soma + m[i][j]
    n = len(m)*len(m[0])
    m = soma/n
    return round(m,2)