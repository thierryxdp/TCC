def media_matriz(matriz):
    soma=0
    divisor=0
    for i in matriz:
        soma+=sum(i)
        divisor+=len(i)
    return soma/divisor