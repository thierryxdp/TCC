def par(x):
    return x%2 ==0
def filtra_pares(a):
    p = ()
  	if par(a[0]):
        return p + (a[0],)
    elif par(a[1]):
        return p + (a[1],)
    elif par(a[2]):
        return p + (a[2],)
    elif par(a[3]):
        return p + (a[a],)
    return p