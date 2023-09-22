def lingua_p(frase):
	x=0
	for  x in range(len(frase)+1):
    	if frase[x] in "aeiou":
    		frase[0:x+1]+"p"+=frase[x+1:]
            
    	x=x+1
	return frase