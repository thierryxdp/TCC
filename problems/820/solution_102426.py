def posLetra(frase,letra,n):
	x=0
	y=0
	while x<len(frase):
    	if y==n:
        if frase[x]==letra:
        	y=y+1
    	
       		return frase.index(frase[x])
		x=x+1
	return -1