def filtra_pares(a=[]):
    """Informando quatro inteiros para a lista de tuplas 
    retorna os elementos nas posições pares."""
    y=(list(a))
    if (len(y))==4:
        return a[1,3]
    elif (len(y))==3:
        return a[1]
    elif (len(y))==2:
        return a[1]