def filtra_pares(n,m,d,c):
    """função que retorna uma tupla com apenas elementos pares da tupla original; int, int, int, int -> tuple"""
    tupla=(n,m,d,c)
    pares=()
    if x%2==0:
        pares = pares +('n',)
    if y%2==0:
        pares= pares+('m',)
    if z%2==0:
        pares= pares+('d',)
    if d%2==0:
        pares= pares+ ('c',)
    return pares