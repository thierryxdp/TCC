def conta_numero(n,m):
    '''
    retorna quantas vezes o numero em questao aparece na matriz
    int,list -> int
    '''
    nlin = len(m)
    ncol = len(m[0])
    qtd_elem = 0
    vazia=[]
    for i in range(nlin):
        for el in range(ncol):
            if m[i][el] == n:
                qtd_elem = qtd_elem + 1
            elif m=vazia:
                qtd_elem = 0
    return qtd_elem