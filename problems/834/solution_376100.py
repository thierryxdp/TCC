def media_matriz(matriz):
    soma1=0
    e=0
    media=0
    for c in range(matriz):
        soma=0
        for i in range(matriz[c]):
            soma=soma+i
            e=e+1
        soma1=soma1+soma
    return media=(soma1)/e