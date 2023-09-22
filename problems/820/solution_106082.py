def posLetra (f,l,n):
    if str.count(f,l) < n:
        return -1
    else:
    	return str.find(f,l,n)