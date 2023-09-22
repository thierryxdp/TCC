def lingua_p(frase):
	x=0
	for  x in len(frase):
    	if frase[x] in "aeiou":
    		frase=frase[0:x+1]+"p"+"frase[x::]"+frase[x+1:]
            
    	x=x+1
	return frase