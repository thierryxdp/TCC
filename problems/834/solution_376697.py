def media_matriz(matriz):
    soma = 0.0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma=sum(matriz[i][j])
            soma=soma+1
    total=total+soma/len(matriz)*len(matriz[0])
    return round(soma/elementos,2)