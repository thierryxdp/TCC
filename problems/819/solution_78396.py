def filtraMultiplos(l,n):
    lp = []
    for i in range(len(l)):
        if (l[i])%n == 0:
        	lp.append(l[i])
	return lp