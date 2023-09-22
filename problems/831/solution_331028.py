def lingua_p(frase):
	x=0
	for  x in range(len(frase)+1):
    	if frase[x] in "aeiou":
    		frase=frase[0:x]+"p"+frase[x:]
            
    	x=x+1
	return frase