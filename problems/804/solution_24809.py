def filtra_pares (t):
    if ((t[0])%2==0):
        par =(t[0],)
    if ((t[1])%2==0):
        par = par +(t[1],)
    if ((t[2])%2==0):
        par = par + (t[2],)
    if ((t[3])%2==0):
        par = par + (t[3],)
    return par