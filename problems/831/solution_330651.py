def lingua_p (frase):
    frase = frase.lower()
    i=0
    for l in frase:
        if l in "aeiou":
        	frase = frase[:i+1] + "p"+l + frase[i:]
            i = +2
		else:
			i = +1
    return frase