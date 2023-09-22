def uppCons(frase):
    maiusc = str.upper(frase[proximo])
    proximo = 0
	while proximo<(len(frase)):
        if frase[proximo] not in "AEIOUaeiou":
            return maiusc
        proximo = proximo + 1
    return frase