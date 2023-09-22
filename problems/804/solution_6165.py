def filtra_pares(n,m,d,c):
    """função que retorna uma tupla com apenas elementos pares da tupla original; int, int, int, int -> tuple"""
    original=(n,m,d,c,)
    pares=()
    if n%2==0:
        pares = pares +('n',)
    if m%2==0:
        pares= pares+('m',)
    if d%2==0:
        pares= pares+('d',)
    if c%2==0:
        pares= pares+ ('c',)
        return pares