def media_matriz(matriz):
    soma = 0
    divisao = 0
    for i in matriz:
        soma += 4
        divisao += len(i)
    return round(soma/divisao,2)