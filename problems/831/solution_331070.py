def lingua_p(frase):
	x=0
	for  x in (frase):
    	if frase in "aeiou":
    		frase=frase[x:x+1]+"p"+frase[x:x+1]        
	return frase