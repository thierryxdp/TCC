def posLetra(string,letra,n):
    L=[]
    for i in range(len(string)):
	    if i==letra:
		    L.append(i)
    return L[n]