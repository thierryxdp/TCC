def filtra_pares(t):
    ''' funcao que dada uma tupla não vazia de inteiros, retorna uma tupla com os
    inteiros pares da tupla original, mantida a ordem.
    tuple --> tuple'''
    pares = ()
    i = 0
    while i < len(t):
        pares = (i for i in t if i % 2 == 0)
        i += 1
    return pares