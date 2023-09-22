def filtra_pares(x,y,z,d):
    """função que retorna uma tupla com apenas elementos pares da tupla original; int, int, int, int -> tuple"""
    tupla=(x,y,z,d,)
    pares=()
    if x%2=0:
        pares = pares + x
    if y%2=0:
        pares= pares+y
    if z%2=0:
        pares= pares+z
    if d%2=0:
        pares= pares+d
    return pares