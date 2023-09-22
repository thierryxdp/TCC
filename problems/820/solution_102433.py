def posLetra(frase,letra,n):
	x=0
	y=0
	while x<len(frase):
    	if frase[x]==letra:
        	y=y+1
    	if y>n:
       		return frase.index(frase[x])
		x=x+1
	return -1