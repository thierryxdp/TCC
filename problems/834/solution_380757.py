def media_matriz(matriz):
    '''Função que dada uma matriz de número inteiros, retorna
    a média de todos os números da matriz;
    list->list'''
    comp=0
    soma=0
    for i in matriz:
        comp=comp+len(i)
        soma=soma+sum(i)
    return round(soma/comp,2)