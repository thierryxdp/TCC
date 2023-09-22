def filtra_pares(p):
    """Funcao que recebe uma tupla e retorna uma nova tupla contendo apenas pares da tupla
    original, na mesma ordem em que se encontravam. tupla->tupla."""
    p = x, y, w, z
    s= ()
    if x%2==0:
        s=s+(x,)
    if y%2==0:
        s=s+(y,)
    if w%2==0:
        s=s+(w,)
    if z%2==0:
        s=s+(z,)
    return s