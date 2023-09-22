def uppCons(frase):
    proximo = 0
    final = ""
	while proximo<(len(frase)):
        if frase[proximo] not in "AEIOUaeiou":
            final = str.upper(frase[proximo])
        else:
            final = frase[proximo]
        proximo = proximo + 1
    return final