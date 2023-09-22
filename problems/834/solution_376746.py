def media_matriz(matriz):
    soma = 0.0
    for i in range(len(matriz)):
        soma=soma+sum(matriz[i])
    total=soma/len(matriz)*len(matriz[0])
    return round(total,2)