def filtra_pares(x):
    """Recebe quatro inteiros e retorna apenas os pares.
    int int int int -> int pares"""
    
   pares = ()
    
    if x[0] % 2 == 0:
        pares += (x[0],)
    elif x[1] % 2 == 0:
        pares += (x[1],)
    elif x[2] % 2 == 0:
        pares += (x[2],)
    elif x[3] % 2 == 0:
        pares += (x[3],)
    return pares