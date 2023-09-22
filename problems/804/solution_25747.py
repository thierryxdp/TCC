def filtra_pares(t):
    pares=()
    if t[0]%2==0:
        return pares==pares+(t[0],)
    elif t[1]%2==0:
        return pares==pares+(t[1],)
    elif t[2]%2==0:
        return pares==pares+(t[2],)
    elif t[3]%2==0:
        return pares==pares+(t[3],)
    else:
        return pares==pares+()