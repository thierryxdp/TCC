def filtra_pares (t):
    p = ()
    if ((t[0])%2==0):
        p = p + (t[0],)
        return p
    if ((t[1])%2==0):
        p = p + (t[1],)
        return p
    if ((t[2])%2==0):
        p = p + (t[2],)
        return p
    if ((t[3])%2==0):
        p = p + (t[3],)
        return p
    else:
        return ()