def media_matriz(matriz):
    comp=0
    sma=0
    for i in matriz:
        comp=comp+len(i)
        soma=soma+sum(i)
    return round(soma/comp, 2)