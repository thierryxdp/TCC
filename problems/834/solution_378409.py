def media_matriz(matriz):
    comp=0
    soma=0
    med=round(soma/comp,2)
    for i in matriz:
        comp=comp+len(i)
        soma=soma+sum(i)
    return med