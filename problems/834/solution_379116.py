def media_matriz (matriz):
    '''função que dada uma matriz, retorna a média de todos os
       números da matriz.
       : list -> float
    '''
    nlin = len(matriz)
    ncol = len(matriz[0])
    soma = 0
    elem = nlin*ncol
    for i in range(nlin):
        for j in range(ncol):
            soma = soma + j
    resultado = soma/elem
    return round(resultado),2