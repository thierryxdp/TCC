def faltante(L):
    i=0
    while i<len(L):
        if L[i]+2==L[i+1]:
            i=i+1
    	return L[i]+L[i+1]/2