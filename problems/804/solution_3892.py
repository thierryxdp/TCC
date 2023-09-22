def filtra_pares(a, b, c, d):
    """Recebe quatro inteiros e retorna apenas os pares.
    int int int int -> int pares"""
    
    
    pares = ()
    
    if a % 2 == 0:
        return pares + (a,)
    elif b % 2 == 0:
        return pares + (b,)
    elif c % 2 == 0:
        return pares + (c,)
    elif d % 2 == 0:
        return pares + (d,)