def lingua_p(frase):
	x=0
	for  x in range(len(frase)+1):
    	if frase[x] in "aeiou":
    		frase=frase[0:x+1]+"p"+frase[x:]        
	return frase