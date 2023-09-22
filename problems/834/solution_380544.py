def media_matriz(m):
    """ Funçao que dada uma matriz de inteiros nao vazia, retorna a média
    de todos os numeros da matriz """
    nlin = len(matriz)
    ncol = len(matriz[0])
    nelem = nlin * ncol
    soma = 0
    
    for i in range(nlin):
        for j in range(ncol):
            soma += matriz[i][j]
            
    return round(soma/nelem,2)