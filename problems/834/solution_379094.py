def media_matriz(matriz):
    total = 0
    soma = 0
    for i in matriz:
        for j in i:
            soma +=j
        total += len(i)
    return round(soma/total,2)