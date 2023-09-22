def media_matriz(matriz):
    soma1=0
    e=0
    for c in range(len(matriz)):
        soma=0
        for i in range(len(matriz[c])):
            soma=soma+matriz[c][i]
            e=e+1
        soma1=soma1+soma
    return round(((soma1)/e),2)