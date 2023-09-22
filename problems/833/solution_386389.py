def conta_numero(n,m):
    '''
    retorna quantas vezes o numero em questao aparece na matriz
    int,list -> int
    '''
    nlin = len(m)
    qtd_elem = 0
    for i in range(nlin):
        for el in range(ncol):
            ncol = len(m[i])
            if m[i][el] == n:
                qtd_elem = qtd_elem + 1
            elif m=vazia:
                qtd_elem = 0
    return qtd_elem