def freq_palavras(frases):
    r = str.split(frases, " ")
    D = {}
	for x in r:
        if x in frases:
            D[x] = 0 + 1
	return D