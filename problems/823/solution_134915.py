def faltante (n):
	nCrescent=list.sort(n)
    i=0
    while i < range(len(nCrescent)):
        if i+1 != nCrescent:
        	return i+1