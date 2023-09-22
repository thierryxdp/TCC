def filtra_pares(a=[],b=[],c=[],d=[]):
    """Informando quatro inteiros para a lista de tuplas 
    retorna os elementos nas posições pares."""
    x=(a,b,c,d)
    y=(list(x))
    if (len(y))==4:
        return (b,d)
    elif (len(y))==3:
        return x[1]
    elif (len(y))==2:
        return x[1]