def lingua_p (frase):
    frase = frase.lower()
    i = -1
    for l in frase:
        i = i + 1
		if l in "aeiou":
        	frase = frase[:i] + "p" + frase[i:]
            
    return frase