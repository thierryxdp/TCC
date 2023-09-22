def media_matriz(matriz):
    soma = 0
    count = 0
    for m in matriz:
        for i in m:
            count += 1
            soma += i
    return soma/count