def par(x):
    return x%2 ==0
def filtra_pares(a):
    p = ()
    if par(a[0]):
        p = p + (a[0],)
    if par(a[1]):
        p = p + (a[1],)
    return p