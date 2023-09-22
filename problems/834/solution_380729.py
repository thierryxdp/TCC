def media_matriz(x):
    'Faz a média de todos os números de uma matriz x. list -> float'
    i = 0
    soma = 0
    total = 0
    while i<len(x):
        for j in x[i]:
            soma = soma + j
            total = total + 1
        i = i + 1
    nfinal = soma/total
    return round(nfinal,2)