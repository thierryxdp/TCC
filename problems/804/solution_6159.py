def filtra_pares(n,m,d,c):
    """função que retorna uma tupla com apenas elementos pares da tupla original; int, int, int, int -> tuple"""
    tupla=(n,m,d,c)
    pares=()
    if x%2==0:
        pares = pares +('x',)
    if y%2==0:
        pares= pares+('y',)
    if z%2==0:
        pares= pares+('z',)
    if d%2==0:
        pares= pares+ ('d',)
    return pares