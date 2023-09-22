def freq_palavras(frase):
    qnt = {}
	frase = frase.split()
	for i in range(len(frase)):
        if frase[i] not in qnt:
            qnt[str(frase[i])] = 1
        else:
            qnt[str(frase[i])] += 1
    return qnt