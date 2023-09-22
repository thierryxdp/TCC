def conta_numero (numero,matriz):
    '''função que dada uma matriz e um número inteiro, retorna
       quantas vezes esse número aparece na matriz.
       : int, list -> int
    '''
    nlin = len(matriz)
    ncol = len(matriz[0])
    qtd_numero = 0
    
    for i in range(nlin):
        for j in range(ncol):
            if j == numero:
                qtd_numero += 1
    return qtd_numero