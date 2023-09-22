def uppCons(frase):
    proximo = 0
    maiusc = str.upper(frase[proximo])
	while proximo<(len(frase)):
        if frase[proximo] not in "AEIOUaeiou":
            list(frase)
            str.upper(frase[proximo])
        proximo = proximo + 1
    return frase