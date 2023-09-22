def uppCons(frase):
    proximo = 0
	while proximo<(len(frase))+1:
        if frase[proximo] in "aeiou":
            str.upper(frase[proximo])
        proximo = proximo + 1
    return frase