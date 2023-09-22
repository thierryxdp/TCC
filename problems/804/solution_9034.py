def filtra_pares(tup):
    '''Função que, dada uma tupla qualquer, retorna essa mesma tupla contendo apenas os elementos pares.
tuple --> tuple'''
    tup_nova = ()
    n = 0
    while n<len(tup):
        if tup[n]%2 == 0:
            tup_nova = tup_nova + (tup[n],)
        n = n+1
    return tup_nova