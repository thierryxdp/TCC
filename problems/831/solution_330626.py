def lingua_p (frase):
    frase = frase.lower
    for l in frase:
        if l in "aeiou":
        	frase = frase[:l] + "p" + frase[l:]
    return frase