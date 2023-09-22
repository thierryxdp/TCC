def filtra_pares(e1,e2,e3,e4):
    """..."""
    tup = (e1,e2,e3,e4)
    pares = filter(lambda x: x%2==0, tup)
    
    return pares