def filtra_pares(a, b, c, d):
    """Recebe quatro inteiros e retorna apenas os pares.
    int int int int -> int pares"""
    
    pares = ()
    
    if a % 2 == 0:
        return pares + (a,)
    if b % 2 == 0:
        return pares + (b,)
    if c % 2 == 0:
        return pares + (c,)
    if d % 2 == 0:
        return pares + (d,)