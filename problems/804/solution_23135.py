def par(x):
    return x%2 ==0
def filtra_pares(a):
    p = ()
    if par(a[1]):
    	p = p + (a[1],)
    if par(a[2]):
       	p = p + (a[2],)
    if par(a[3]):
       	p = p + (a[3],)
    if par(a[4]):
        p = p + (a[4],)
    	return p