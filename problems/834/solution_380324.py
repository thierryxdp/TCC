def media_matriz(matriz):
    soma=0
    num=0
    for x in matriz:
        num=num+len(x)
        soma=soma+sum(x)
    return soma/num