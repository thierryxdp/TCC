def lingua_p (frase):
    frase = frase.lower()
    
    for i,l in enumerate(frase):
        
		if l in "aeiou":
        	frase = frase[:i] + "p"+ l + frase[i+1:]
            
    return frase