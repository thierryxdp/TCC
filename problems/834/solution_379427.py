def media_matriz(matriz):
    'dada uma matriz, é calculada a media aritimetica de todos os termos dela list->float'
    soma = 0
    ndetermos = len(matriz)*len(matriz[0])
    for i in range(len(matriz)):
        soma = soma + sum(matriz[i])
    return round(soma/ndetermos,2)