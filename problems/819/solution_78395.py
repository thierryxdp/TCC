def filtraMultiplos(l,n):
    lp = []
    for i in range(len(l)-1):
        if (l[i])%n == 0:
        	lp.append(l[i])
	return lp