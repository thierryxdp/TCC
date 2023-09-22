def media_matriz(matriz):
    '''função responsável por somar a média dos números da matriz escolhida,(matriz)'''
    comp=0
    soma=0
    for i in matriz:
        comp=comp+len(i)
        soma=soma+sum(i)
    return round(soma/comp,2)