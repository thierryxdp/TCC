def lingua_p (frase):
    frase = frase.lower()
    i = 0
    for i,l in enumerate(frase):
        
		if l in "aeiou":
        	frase = frase[:i] + "p" + frase[i:]
            
    return frase