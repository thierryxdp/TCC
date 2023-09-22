def filtraMultiplos(ls,n):
    r = []
    i = 0
    while i < len(ls):
    	if ls[i]%n==0: 
            list.append(r,ls[i])
        elif ls[i]%n!=0:
            return r
    i = i + 1
	return r