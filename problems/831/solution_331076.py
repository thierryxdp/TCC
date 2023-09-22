def lingua_p(frase):
	x=0
	for  x in (frase):
    	if frase in "aeiou":
    		frase[x:]+"p"+frase[x+1:x+2]        
	return frase