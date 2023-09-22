def posLetra(frase,x,n):
    i=0
    k=0
    if str.find(frase,x)<n:
        return -1
    else:
		while i<len(frase):
    		if frase(i)==x:
    			k=k+1
        		if k==n:
            		return i
        		else:
            		i=i+1