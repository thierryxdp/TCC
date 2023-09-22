def lingua_p (frase):
    frase = frase.lower()
    i=0
    for l in frase:
        if l in "aeiou":
        	frase = frase[:i] + "p"+l + frase[i:]
            i = +1
		else:
			i = +1
    return frase