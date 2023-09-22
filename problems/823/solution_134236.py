def faltante(L):
    list.sort(L)
    indice=0
    if len(L)==1 and L[0]!=1:
        return L[0]-1
    elif len(L)==1 and L[0]==1:
        return 2
    else:
    	while indice<len(L):
        	if L[indice]-L[indice-1]==1:
        		indice=indice+1
        	elif L[indice]-L[indice-1]==2:
            	return L[indice]+L[indice-1]/2