def filtra_pares(numeros4: tuple):
    """Filtra uma tupla com 4 elementos, retornando apenas
    os elementos pares na ordem que se encontram inicialmente.
    tuple -> tuple
    """
    n1, n2, n3, n4 = numeros4[0], numeros4[1], numeros4[2], numeros4[3]
    
    pares = tuple ()
    
    if n1%2 == 0:
        pares += (n1,)
    if n2%2 == 0:
        pares += (n2,)
    if n3%2 == 0:
        pares += (n3,)
    if n4%2 == 0:
        pares += (n4,)
        
    return pares