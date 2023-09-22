def media_matriz(matriz):
    soma = 0
    count = 0
    for m in matriz:
        count += m
        for i in m:
            soma += i
    return soma/count