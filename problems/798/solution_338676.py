def freq_palavras(frases):
    frases.sort()
    r = str.split(frases, " ")
    D = {}
	for x in r:
        if x in frases:
            D[x] = 1
	return D