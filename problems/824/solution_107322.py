def uppCons(frase):
    proximo = 0
    final = ""
	while proximo<(len(frase)):
        if frase[proximo] in "AEIOUaeiou":
            final+(frase[proximo])
        else:
            final+str.upper(frase[proximo])
        proximo = proximo + 1
    return final