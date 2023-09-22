def filtra_pares(a,b,c,d):
    ''' funcao que dada uma tupla não vazia de inteiros, retorna uma tupla com os
    inteiros pares da tupla original, mantida a ordem.
    tuple --> tuple'''
    pares = ()
    proximo = 0
    while proximo < len(t):
        if t[proximo] % 2 == 0:
            pares = pares + (t[proximo])
        proximo = proximo + 1
    return pares