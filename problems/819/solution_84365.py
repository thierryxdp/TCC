def filtraMultiplos(l,n):
	proximo = 0
    nl= []
   	while proximo <len(l):
    	if l[proximo]/2:
        	nl = nl + (l[proximo],)
     	proximo = proximo +1
    return nl