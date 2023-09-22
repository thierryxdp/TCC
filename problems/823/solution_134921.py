def faltante (n):
	nCrescent=sorted(n)
    i=0
    while i in range(len(nCrescent)):
        if i+1 != nCrescent[i]:
        	return i+1