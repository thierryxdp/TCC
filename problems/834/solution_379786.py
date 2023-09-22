def media_matriz(matriz:list)->float:
    'recebe uma matriz e retorna a média de todos os seus números'
    soma = 0
    total = 0
    for i in matriz:
        for j in i:
            soma += j
        total += len(i)
    return round (soma/total,2)