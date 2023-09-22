def lingua_p(frase):
	x=0
	for  x in (frase):
    	if frase[x] in "aeiou":
    		frase=frase[0:x+1]+"p"+frase[x+2:]        
	return frase