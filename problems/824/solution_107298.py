def uppCons(frase):
    vogais = 0
    proximo = 0
	while proximo<(len(frase)):
        if frase[proximo] not in "AEIOUaeiou":
            vogais = vogais + 1
        proximo = proximo + 1
    return vogais