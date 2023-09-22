def filtraMultiplos(ls,n):
    r = []
    i = 0
    while i < len(ls):
    	if ls[i]%n==0: 
            r = r.append(ls[i])
    		i = i + 1
        else:
            i = i + 1
	return r