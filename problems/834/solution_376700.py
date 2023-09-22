def media_matriz(matriz):
    soma = 0.0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma=sum(matriz[0])
            soma=soma +1
    total=soma/len(matriz)
    return round(total,2)