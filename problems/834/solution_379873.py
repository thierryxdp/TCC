def media_matriz (matriz):
    soma = 0
    total = 0
    for i in matriz:
        for j in i:
            soma += j
    total += len(i)
    return round(soma/total, 2)