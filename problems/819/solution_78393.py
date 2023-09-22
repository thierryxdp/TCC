def filtraMultiplos(l,n):
    lp = []
    for i in range(len(l)-1):
        if (l[i-1])%n == 0:
        	lp.append(l[i])
	return lp