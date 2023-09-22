def filtra_pares(t):
    l=list(t)
    j=list(t)-list(t%2==0)
    l.remove(j)
    return l