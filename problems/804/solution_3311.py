def filtra_pares(e1,e2,e3,e4):
    """..."""
    tup = (e1,e2,e3,e4)
    tupnova = ()

    analise_e1 = not(bool(e1%2))
    analise_e2 = not(bool(e2%2))
    analise_e3 = not(bool(e3%2))
    analise_e4 = not(bool(e4%2))
    return filter(filtra_pares,tup)