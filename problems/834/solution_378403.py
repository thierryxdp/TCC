def media_matriz(m):
    '''Retorna a média de todos os valores da matriz.
    list -> int'''
    soma = 0
    for i in range(len(m)):
        for j in m[i]:
            soma += j
    return round(soma / (len(m) * len(m[0])),2)