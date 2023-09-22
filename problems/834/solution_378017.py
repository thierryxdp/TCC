def media_matriz(matriz):
    soma = 0
    divisao = 0
    for x in matriz:
        soma = soma + sum(x)
        divisao  = divisao + 1
    return round(soma/divisao,2)