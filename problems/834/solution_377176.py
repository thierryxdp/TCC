def media_matriz(matriz:list) ->str:
    '''Recebe uma matriz e retorna a média dos valores de todos os elementos'''
    soma = 0
    for lista in matriz:
        for elemento in lista:
            soma += elemento
    media = soma/(len(matriz)*len(matriz[0]))
    return f'{media:.2f}'