def faltante(L):
    i=0
    while i<len(L):
        if L[i]!=(i+1):
            del L[i+1:]
            num_falt=(L[i-1]+L[i])/2
        i=i+1
    	return num_falt