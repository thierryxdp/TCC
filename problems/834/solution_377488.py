def media_matriz(matriz):
    '''Funcao que dada uma matriz de inteiros nao vazia retorna a 
    media de todos os numeros da matriz com precisao de duas casas
    decimais; list->float'''
    soma=0
    divisor=0
    for i in matriz:
        soma+=sum(i)
        divisor+=len(i)
    return round(soma/divisor,2)