def par(x):
    return x%2 ==0
def filtra_pares(a):
    p = ()
    if par(a[0]):
    	p1 = p + (a[0],)
    elif par(a[1]):
       	p2 = p1 + (a[1],)
    elif par(a[2]):
       	p3 = p2 + (a[2],)
    elif par(a[3]):
        p4 = p3 + (a[3],)
    	return p