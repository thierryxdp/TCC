def media_matriz(matriz):
    soma=0
    numero=0
    for i in range(len(matriz)):
        soma=soma+sum(matriz[i])
        numero=numero+len(matriz[i])
    media=soma/numero
    return media