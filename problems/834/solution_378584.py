def media_matriz(matriz):
    '''Função que, dada uma matriz de inteiros (não vazia)
    retorna a média de todos os números da matriz com duas
    casas decimais de precisão;
    list->float'''
    comp=0
    soma=0
    for i in matriz:
        comp=comp+len(i)
        soma=soma+sum(i)
    return round(soma/comp,2)