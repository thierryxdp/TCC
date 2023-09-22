def filtra_pares(tup):
    """retorna uma nova tupla contendo apenas os elementos pares da tupla original que contem 4 elementos inteiros.
    int,int,int,int-> tupla"""
    if tup[0]%2==0:
        return (tup[0],)
    elif tup[1]%2==0:
        return (tup[0]) + (tup[1],)
    elif tup[2]%2==0:
        return (tup[0],) + (tup[1],) + (tup[2],)
    elif tup[4]%2==0:
        return (tup[0],) + (tup[1],) + (tup[2],) + (tup[3])
    else:
        return ()