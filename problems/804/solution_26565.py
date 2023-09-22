#Start your python function here
def filtra_pares(t):
    ''' retorna uma tupla com os
    inteiros pares da tupla original
    tuple --> tuple'''
    pares = ()
    for proximo in t:
        if proximo%2 == 0:
            pares = pares + (proximo,)
    return pares