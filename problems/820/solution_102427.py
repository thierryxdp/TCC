def posLetra(frase,letra,n):
	x=0
	y=0
	while x<len(frase):
    	if y==n:
            return frase.index(frase[x])
        if frase[x]==letra:
        	y=y+1
    	
       		
		x=x+1
	return -1