def filtra_pares(t):
    tup=()     
    if par(t[0]):
        return tup+(t[0],)
    if par(t[1]):
        return tup+(t[1],)
    if par(t[2]):
        return tup+(t[2],)
    if par(t[3]):
        return tup+(t[3],)