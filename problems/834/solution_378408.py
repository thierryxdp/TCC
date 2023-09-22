def media_matriz(matriz):
    med=round(soma/comp,2)
    comp=0
    soma=0
    for i in matriz:
        comp=comp+len(i)
        soma=soma+sum(i)
    return med