def filtraMultiplos(L, n):
    r = []
    for e in L:
        if e%n==0:
        	r=r+[e]
	return r