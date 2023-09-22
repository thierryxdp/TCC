def par(n):
    return n%2 == 0

def filtra_pares(t):
    r = ()
    if par(t[0]):
        r = r+(t[0],)
    if par(t[1]):
        r = r+(t[1],)
    if par(t[2]):
        r = r+(t[3],)
    if par(t[4]):
        r = r+(t[4],)
    return r