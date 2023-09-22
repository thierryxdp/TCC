def media_matriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma=soma+sum(matriz[i])
        elem=len(matriz)*len(matriz[0])
    total= soma/elem
    return round(total,2)