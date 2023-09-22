def uppCons(frase):
    proximo = 0
    final = []
	while proximo<(len(frase)):
        if frase[proximo] not in "AEIOUaeiou":
            final.insert(str.upper(frase[proximo]),proximo)
        else:
            final.insert(frase[proximo],proximo)
        proximo = proximo + 1
    return str(final)