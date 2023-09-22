def lingua_p(frase):
	x=0
	while x<len(frase):
    	if frase[x] in "aeiou":
            if x==0:
    			frase=frase[0:x+1]+"p"+frase[x+1:]
            if x!=0:
                frase=frase[0:x+1]+"p"+frase[x:]
    	x=x+1
	return frase