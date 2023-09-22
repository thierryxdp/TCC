def conta_numero(n,m):
    '''
    retorna quantas vezes o numero em questao aparece na matriz
    int,list -> int
    '''
    nlin = len(m)
    ncol = len(m[i])
    qtd_elem = 0
    for i in range(nlin):
        ncol = len(m[i])
        for el in range(ncol):
            if m=[]:
                qtd_elem = 0
            if m[i][el] == n:
                qtd_elem = qtd_elem + 1
    return qtd_elem