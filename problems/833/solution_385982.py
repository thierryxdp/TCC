def conta_numero(n,m):
    '''
    retorna quantas vezes o numero em questao aparece na matriz
    int,list -> int
    '''
    nlin = len(m)
    ncol = len(m[0])
    qtd_elem1 = 0
    for i in range(nlin):
        for el in range(ncol):
            if el == n:
                qtd_elem = qtd_elem + 1                     
    return qtd_elem