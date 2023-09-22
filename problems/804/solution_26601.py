def filtra_pares (tup):
    if tup[0]%2==0 and tup[1]%2==0:
        return tuple((tup[0],tup[1]))
    if tup[0]%2==0:
        return tuple([tup[0]])
    else:
        return ()