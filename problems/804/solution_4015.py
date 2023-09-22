def filtra_pares(a, b, c, d):
    """Recebe quatro inteiros e retorna apenas os pares.
    int int int int -> int pares"""
    
    pares = ()
    
    if a % 2 == 0:
        pares = pares + (a,)
    elif b % 2 == 0:
        pares = pares + (b,)
    elif c % 2 == 0:
         pares = pares + (c,)
    elif d % 2 == 0:
          pares = pares + (d,)
    return pares